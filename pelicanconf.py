#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'daniele arosio'
SITENAME = 'Food protocols'
SITESUBTITLE = u'il cibo che cucino'
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

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['org_pandoc_reader', 'summary',
           'liquid_tags.include_code',
           'liquid_tags.literal',
           'render_math']


# ORG_READER_EMACS_LOCATION = '/usr/bin/emacs'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True


#Github include settings
GITHUB_USER = 'darosio'
GITHUB_REPO_COUNT = 0
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Sharing
# TWITTER_USER = 'jakevdp'
# GOOGLE_PLUS_USER = 'jakevdp'
# GOOGLE_PLUS_ONE = True
# GOOGLE_PLUS_HIDDEN = False
# FACEBOOK_LIKE = False
# TWITTER_TWEET_BUTTON = True
# TWITTER_LATEST_TWEETS = True
# TWITTER_FOLLOW_BUTTON = True
# TWITTER_TWEET_COUNT = 3
# TWITTER_SHOW_REPLIES = 'false'
# TWITTER_SHOW_FOLLOWER_COUNT = 'true'
