# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'UnitedHealthcare Provider Login Portal'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "UnitedHealthcare Provider Login – Access Claims, Eligibility & More"

# Optional short title (e.g., for nav bar)
html_short_title = "UHC Provider Login"

# Favicon (place favicon.ico in _static folder)
html_favicon = 'favicon.ico'

# Theme to use for HTML pages
html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files (for SEO/meta tags, buttons, etc.)
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'collapse_navigation': False,
    'style_nav_header_background': '#005EB8',  # UHC-like color
    'navigation_depth': 4,
    'titles_only': False,
    'show_powered_by': False,
}

# Paths to templates and static files
# templates_path = ['_templates']
# html_static_path = ['_static']

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
