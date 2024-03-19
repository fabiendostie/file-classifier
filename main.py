import os
import shutil
import time
import re
import logging
from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import download_folder, classification_rules, GREEN, RESET, log_filename, DAYS_BEFORE_ARCHIVE, ARCHIVE_ACTION, ARCHIVE_FOLDER
from tqdm import tqdm

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ask_sorting_preference():
    print("Do you want to sort files into subfolders based on their dates? (yes/no)")
    user_input = input().strip().lower()
    return user_input == "yes"

def ask_for_new_extension_category(unknown_extension):
    print(f"New file extension detected: {unknown_extension}. Into which category should it be sorted?")
    category = input().strip()
    return category

def update_classification_rules(extension, category):
    if category in classification_rules:
        classification_rules[category].append(extension)
    else:
        classification_rules[category] = [extension]
    with open("config.py", "w") as config_file:
        config_content = 'classification_rules = {\\n'
        for cat, extensions in classification_rules.items():
            extensions_str = ', '.join([f'"{ext}"' for ext in extensions])
            config_content += f'    "{cat}": [{extensions_str}],\\n'
        config_content += '}\\n'
        config_file.write(config_content)

def classify_and_move_existing_files_and_folders(sorting_preference_date_based):
    script_created_dirs = [os.path.join(download_folder, category) for category in classification_rules.keys()]
    if sorting_preference_date_based:
        today = datetime.today().strftime('%Y-%m-%d')
        script_created_dirs += [os.path.join(dir, today) for dir in script_created_dirs]
    
    folders_path = os.path.join(download_folder, "Folders")
    script_created_dirs.append(folders_path)
    
    if not os.path.exists(folders_path):
        os.makedirs(folders_path)
    
    for item in os.listdir(download_folder):
        item_path = os.path.join(download_folder, item)
        if os.path.isfile(item_path):
            file_name = os.path.basename(item_path)
            file_extension = os.path.splitext(file_name)[1].lower()
            destination_category = None
            for category, extensions in classification_rules.items():
                if file_extension in extensions:
                    destination_category = category
                    break
            if destination_category is None:
                destination_category = "Uncategorized"
            destination_path = os.path.join(download_folder, destination_category)
            if sorting_preference_date_based:
                destination_path = os.path.join(destination_path, today)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.move(item_path, os.path.join(destination_path, file_name))
            print(f"Moved file {file_name} to {destination_path}")
        elif os.path.isdir(item_path) and item_path not in script_created_dirs:
            shutil.move(item_path, os.path.join(folders_path, item))
            print(f"Moved folder {item} to {folders_path}")

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            self.process(event.src_path)
    
    def process(self, file_path):
        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_name)[1].lower()
        if file_extension not in {ext for exts in classification_rules.values() for ext in exts}:
            destination_category = ask_for_new_extension_category(file_extension)
            update_classification_rules(file_extension, destination_category)
        print(f"File {file_name} processed.")

def main():
    sorting_preference_date_based = ask_sorting_preference()
    print("Organizing existing files and folders...")
    classify_and_move_existing_files_and_folders(sorting_preference_date_based)
    
    print("Starting file monitoring...")
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path=download_folder, recursive=True)
    observer.start()
    print("Monitoring started. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Monitoring stopped.")

if __name__ == '__main__':
    main()
