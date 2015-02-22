#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import path

import datetime
TODAY = datetime.date.today()

SETTINGS_DIR_PATH = path.dirname(path.abspath(__file__))

AUTHOR = u'Chris Erickson'
SITENAME = u'Chris Erickson'
SITETAGLINE = u'Not like the phone.'
SITEURL = ''

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATHS = [
    'pelican-plugins'
]
PLUGINS = ['assets']
ASSET_CONFIG = (
    ('LESS_BIN', path.join(SETTINGS_DIR_PATH, 'node_modules/less/bin/lessc')),
    ('CLEANCSS_BIN', path.join(SETTINGS_DIR_PATH, 'node_modules/clean-css/bin/cleancss')),
    ('UGLIFYJS_BIN', path.join(SETTINGS_DIR_PATH, 'node_modules/uglify-js/bin/uglifyjs')),
)

# Feed Generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 10

# Content
THEME = 'theme'
PATH = 'content'
TYPOGRIFY = True

# Static Files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# URLs
DEFAULT_DATE_FORMAT = "%B %-m, %Y"
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}.html"
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Social
GITHUB_URL = "https://github.com/chris-erickson"
TWITTER_URL = "https://www.twitter.com/chriserickson"
