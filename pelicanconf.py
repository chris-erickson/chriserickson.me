#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import path

import datetime
TODAY = datetime.date.today()

SETTINGS_DIR_PATH = path.dirname(path.abspath(__file__))

AUTHOR = u'Chris Erickson'
SITENAME = u'Chris Erickson'
SITETAGLINE = u'Life is an Adventure.'
SITEURL = ''

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATHS = [
    'pelican-plugins'
]
PLUGINS = [
    'assets',
    'bootstrapify',
    'sitemap',
]
ASSET_CONFIG = (
    ('LESS_BIN', path.join(SETTINGS_DIR_PATH, 'node_modules/less/bin/lessc')),
    ('UGLIFYJS_BIN', path.join(SETTINGS_DIR_PATH, 'node_modules/uglify-js/bin/uglifyjs')),
)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

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
    'extra/favicon/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
    'extra/favicon/apple-touch-icon-60x60.png': {'path': 'apple-touch-icon-60x60.png'},
    'extra/favicon/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
    'extra/favicon/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
    'extra/favicon/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
    'extra/favicon/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
    'extra/favicon/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
    'extra/favicon/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
    'extra/favicon/apple-touch-icon-180x180.png': {'path': 'apple-touch-icon-180x180.png'},
    'extra/favicon/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/favicon/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'extra/favicon/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon/manifest.json': {'path': 'manifest.json'},
    'extra/favicon/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extra/favicon/mstile-144x144.png': {'path': 'mstile-144x144.png'},
    'extra/favicon/favicon.ico': {'path': 'favicon.ico'},
}

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# URLs
DEFAULT_DATE_FORMAT = "%B %-d, %Y"
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}.htm"
PAGE_SAVE_AS = '{slug}.htm'
PAGE_URL = '{slug}.htm'
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
TWITTER_USERNAME = "chriserickson"
TWITTER_URL = "https://www.twitter.com/{}".format(TWITTER_USERNAME)
