# Set the path to your downloads folder
download_folder = '/Users/lefab/Downloads'

# Define the classification rules
classification_rules = {
    "Audio": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".aiff", ".au", ".m4a", ".mp2",
        ".mpc", ".opus", ".ra", ".raw", ".vox", ".wv", ".webm", ".8svx", ".cda", ".mid",
        ".midi", ".mod", ".mpa", ".oga", ".s3m", ".spx", ".3ga", ".aax", ".ac3", ".amr",
        ".ape", ".asf", ".ast", ".awb", ".dts", ".flp", ".gsm", ".iklax", ".ivs", ".m3u",
        ".m4b", ".m4r", ".mmf", ".msv", ".nmf", ".nsf", ".nwc", ".pcm", ".qcp", ".tta"
    ],
    "Video": [
        ".mp4", ".avi", ".flv", ".mov", ".wmv", ".mkv", ".m4v", ".mpg", ".mpeg", ".vob",
        ".rmvb", ".ogv", ".3gp", ".3g2", ".drc", ".gifv", ".m2v", ".ogx", ".svi", ".yuv",
        ".264", ".3gpp", ".asx", ".bik", ".braw", ".divx", ".dv", ".evo", ".f4v", ".flc",
        ".h264", ".hevc", ".m2ts", ".m8", ".mnv", ".mts", ".nsv", ".nuv", ".pva", ".r3d",
        ".rl2", ".roq"
    ],
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".psd", ".eps", ".ai", ".indd",
        ".raw", ".cr2", ".nef", ".orf", ".sr2", ".dwg", ".dxf", ".heif", ".ico",
        ".jng", ".jxl", ".pbm", ".pcx", ".pict", ".apng", ".avif", ".bpg", ".cgm",
        ".cmx", ".dib", ".djv", ".flif", ".hdr", ".hrz", ".ilbm", ".lbm", ".miff",
        ".niff", ".nol", ".pam", ".pcd", ".pgm", ".ppm", ".ras", ".sgi", ".tga", ".wbmp",
        ".xpm"
    ],
    "Vectorial Images": [
        ".svg", ".cdr", ".eps", ".ai", ".afdesign", ".avit", ".e2d", ".fig", ".sk", ".sk1", ".sxd", ".v2d",
        ".vml", ".wmf", ".xar", ".xcf", ".vsd", ".ppt", ".odg", ".svgz", ".drw", ".emf",
        ".gt2", ".hpgl", ".iges", ".mgcb", ".plt", ".rdp", ".sda", ".sdr", ".stl", ".svf",
        ".swf", ".tikz", ".wmz", ".xaml", ".xd", ".xmind", ".3dv", ".amf", ".art", ".asc",
        ".bvh"
    ],
    "Installers": [
        ".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".appimage", ".run", ".bat", ".cmd",
        ".bin", ".app", ".gadget", ".jar", ".wsf", ".aam", ".air", ".appx", ".awb", ".crx",
        ".ipk", ".isu", ".job", ".jse", ".tar.gz", ".tgz", ".bz2", ".lz", ".lzma", ".lzo",
        ".xz", ".z", ".7zip", ".ace", ".afa", ".alz", ".arc", ".arj", ".bz", ".cabinet",
        ".cpio", ".dar", ".dd", ".ear", ".gca", ".ha"
    ],
    "Documents": [
        ".doc", ".docx", ".pdf", ".txt", ".odt", ".rtf", ".xls", ".xlsx", ".pptx",
        ".odp", ".ods", ".md", ".epub", ".djvu", ".mobi",
        ".azw", ".azw3", ".fb2", ".ibooks", ".cbr", ".cbz", ".abw", ".ans", ".asc", ".aww",
        ".ccf", ".chm", ".clkw", ".docm", ".dot", ".dotx", ".egnt", ".fdx", ".ftm", ".ftx",
        ".gdoc", ".hwp", ".hwpml", ".log", ".lwp", ".mbp", ".me", ".nbp", ".neis", ".nq"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".apk", ".arj",
        ".cab", ".iso", ".jar", ".part", ".pea", ".s7z", ".sit",
        ".sitx", ".zipx", ".zoo", ".war", ".cdx", ".cso",
        ".dgc", ".hki", ".ice", ".j", ".lha", ".lzh",
        ".lzx", ".pak", ".rar5", ".rk", ".sen", ".sfx", ".shar", ".sqx", ".uue", ".warc"
    ],
    "Programming": [
        ".py", ".js", ".java", ".c", ".cpp", ".cs", ".php", ".rb", ".swift", ".go", ".ts",
        ".pl", ".lua", ".groovy", ".scala", ".rs", ".kt", ".m", ".dart", ".pas", ".asm",
        ".vbs", ".s", ".h", ".hpp", ".ada", ".adb", ".ads", ".agda", ".asmx", ".awk",
        ".bash", ".bsh", ".cls", ".cob", ".coffee", ".cppm", ".csx", ".cu", ".cuh",
        ".d", ".erl", ".f", ".f90", ".f95", ".fs", ".gml", ".hcl", ".json", ".hs"
    ],
    "Web": [
        ".html", ".css", ".php", ".asp", ".jsp", ".aspx", ".cgi", ".xml", ".ajax",
        ".cfm", ".html5", ".xhtml", ".rss", ".atom", ".scss", ".less", ".sass", ".wasm", ".vue",
        ".svelte", ".erb", ".haml", ".handlebars", ".hbs", ".jspf", ".liquid", ".mustache",
        ".phtml", ".rhtml", ".slim", ".tmpl", ".twig", ".volt", ".xht", ".xsl", ".yaml", ".yml",
        ".do", ".jhtm", ".jspx", ".jst", ".lda", ".rjs", ".tld"
    ],
    "Databases": [
        ".db", ".mdb", ".accdb", ".sqlite", ".dbf", ".mdf", ".ora", ".fdb", ".db2",
        ".ib", ".myd", ".myi", ".frm", ".odb", ".pdb", ".sqlitedb", ".sqlite3", ".dat", ".db3",
        ".sdb", ".s3db", ".dbk", ".dbx", ".dcb", ".fmp", ".fp5", ".fp7", ".gdb", ".kdb", ".accde",
        ".adp", ".daf", ".edb", ".fmp12", ".frx", ".itdb", ".mdbhtml", ".ndf", ".nsf", ".nv2",
        ".nyf", ".ora", ".pdm", ".prc", ".tdb"
    ],
    "Datasets": [".csv", ".xlsx", ".sql"
    ],
    "Downloader files": [".torrent", ".nzb"
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot", ".sfnt", ".font", ".pfb", ".pfm", ".afm",
        ".bin", ".cff", ".dfont", ".gst", ".pfa", ".sfd", ".std", ".svg", ".ttc", ".vfb",
        ".vfont", ".xfont", ".fon", ".fnt", ".otb", ".tfm"
    ]
}


# Automatic folder cleanup
DAYS_BEFORE_ARCHIVE = 30  # You can change this value based on your requirement
ARCHIVE_ACTION = "move"  # "move" or "delete"
ARCHIVE_FOLDER = "Archived"

# ANSI escape code for green text
GREEN = '\033[32m'
RESET = '\033[0m'

# Log filename
log_filename = 'app.log'
