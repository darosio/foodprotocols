#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'daniele arosio'
SITENAME = 'Food protocols'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Title menu options
MENUITEMS = [('Archives', 'archives.html')]

STATIC_PATHS = ['images', 'figures', 'downloads']

THEME = 'pelican-octopress-theme/'

PLUGIN_PATHS = ['../pelican-plugins', 'plugins']
PLUGINS = ['org_pandoc_reader', 'summary',
           'liquid_tags.include_code',
           'liquid_tags.literal',
           'ipynb.markup',
           'render_math']


# ORG_READER_EMACS_LOCATION = '/usr/bin/emacs'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
