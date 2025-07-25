import sys, os, os.path
is_production = True if os.getenv("DOCS_IS_PRODUCTION", "").lower() in ('1', 'yes', 'true') else False

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "software"))
import glasgow

html_title = project = "Glasgow Interface\u00a0Explorer"
release = version = ""
copyright = "2020—%Y, Glasgow Interface Explorer contributors"

extensions = [
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinxcontrib.autoprogram",
]

highlight_language = "text"

todo_include_todos = True
todo_emit_warnings = True

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ |> "
copybutton_copy_empty_lines = False

html_use_modindex = False
html_use_index = False

html_theme = "furo"
html_baseurl = "https://glasgow-embedded.org/latest/"
html_static_path = ["_static"]
html_css_files = [
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]
html_theme_options = {
    "top_of_page_button": "edit",
    "source_repository": "https://github.com/GlasgowEmbedded/glasgow/",
    "source_branch": "main",
    "source_directory": "docs/manual/src/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/GlasgowEmbedded/glasgow/",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}
if is_production:
    html_theme_options.update({
        "light_css_variables": {
            "color-announcement-background": "#56bf62",
            "color-announcement-text": "#094a05",
        },
        "dark_css_variables": {
            "color-announcement-background": "#1c4808",
            "color-announcement-text": "#64cc69",
        },
        "announcement":
            "Production units are being shipped by Mouser. "
            "<a href='https://crowdsupply.com/1bitsquared/glasgow'>Order yours now!</a>"
    })
else:
    html_theme_options.update({
        "light_css_variables": {
            "color-announcement-background": "#ffdf76",
            "color-announcement-text": "#664e04",
        },
        "dark_css_variables": {
            "color-announcement-background": "#604b2b",
            "color-announcement-text": "#eee388",
        },
        "announcement":
            "This documentation page has been built as a preview. It may be outdated or incorrect "
            "compared to <a href='https://glasgow-embedded.org/'>the official version</a>."
    })

linkcheck_ignore = [
    r"^http://127\.0\.0\.1:8000$",
    # Doesn't like the linkcheck User-Agent.
    r"^https://mouser\.com/",
    # For unknown reasons, is (mostly) unreachable from GitHub CI runners.
    r"^https://chaos\.social/",
    # As above.
    r"^https://en\.uesp\.net/",
    # As above.
    r"^https://www\.gnu\.org/",
    # Part of applet option help.
    r"^tcp:",
]

linkcheck_anchors_ignore_for_url = [
    r"^https://matrix\.to/",
    r"^https://web\.libera\.chat/",
    # GitHub is a React-based SPA; even README content is included as a JSON payload.
    r"^https://github\.com/",
]

# Attempt to keep linkcheck times manageable.
linkcheck_retries = 5
linkcheck_timeout = 5
linkcheck_workers = 50
