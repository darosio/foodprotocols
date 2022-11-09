AUTHOR = "daniele arosio"
SITENAME = "Food protocols"
SITESUBTITLE = "il cibo che cucino"
SITEURL = "https://darosio.github.io/foodprotocols"

PATH = "content"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "it"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Title menu options
MENUITEMS = [("Archives", "archives.html")]

STATIC_PATHS = ["images", "figures", "downloads"]

THEME = "pelican-octopress-theme/"

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = [
    "org_pandoc_reader",
    "summary",
    "liquid_tags.include_code",
    "liquid_tags.literal",
    "render_math",
]
