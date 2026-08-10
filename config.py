import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
EMAIL_FROM        = os.environ.get("EMAIL_FROM")
EMAIL_PASSWORD    = os.environ.get("EMAIL_PASSWORD")
EMAIL_TO          = os.environ.get("EMAIL_TO")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
TOP_N     = 5

RSS_FEEDS = [
    # Distro e Linux generale
    ("OMG Ubuntu",        "https://www.omgubuntu.co.uk/feed"),
    ("It's FOSS News",    "https://news.itsfoss.com/rss"),
    ("LWN.net",           "https://lwn.net/headlines/rss"),
    ("Phoronix",          "https://www.phoronix.com/rss.php"),
    ("Linux Today",       "https://www.linuxtoday.com/feed/"),
    ("DebugPoint",        "https://debugpoint.com/feed/"),
    # Community
    ("r/linux",           "https://www.reddit.com/r/linux/.rss"),
    ("r/Ubuntu",          "https://www.reddit.com/r/ubuntu/.rss"),
    ("r/Fedora",          "https://www.reddit.com/r/Fedora/.rss"),
    ("r/archlinux",       "https://www.reddit.com/r/archlinux/.rss"),
    # Privacy e sicurezza
    ("r/privacy",         "https://www.reddit.com/r/privacy/.rss"),
    # Italiani
    ("Tom's Hardware IT", "https://www.tomshw.it/rss_news.xml"),
]

BOOST_KEYWORDS = [
    # Distro
    "ubuntu", "fedora", "debian", "arch linux", "linux mint",
    "opensuse", "manjaro", "pop os", "elementary",
    "cachyos", "bazzite", "nobara", "garuda",
    # Kernel e sistema
    "kernel", "linux kernel", "systemd", "wayland", "x11",
    "pipewire", "pulseaudio", "mesa", "vulkan",
    # Desktop environment
    "kde plasma", "gnome", "xfce", "lxqt", "cinnamon",
    # Aggiornamenti
    "released", "update", "version", "patch",
    "rilasciato", "aggiornamento", "versione",
    # Privacy e sicurezza
    "privacy", "security", "vulnerability", "cve",
    "sicurezza", "vulnerabilita",
    # Tool
    "terminal", "bash", "zsh", "fish", "flatpak", "snap",
    "appimage", "package manager",
]

PENALTY_KEYWORDS = [
    # Gaming
    "gaming", "steam", "proton", "giochi",
    # Hardware
    "mini pc", "gpu", "cpu benchmark",
    # Mobile
    "android", "ios", "smartphone", "iphone",
    # Fuori tema
    "nft", "crypto", "blockchain", "metaverse",
    "windows", "macos", "apple",
    "dash cam", "smart tv", "alexa",
]
