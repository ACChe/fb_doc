# -*- coding: utf-8 -*-

# Scrapy settings for crab_soccer project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crab_soccer'

SPIDER_MODULES = ['crab_soccer.spiders']
NEWSPIDER_MODULE = 'crab_soccer.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crab_soccer (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.70 Safari/537.17'

ITEM_PIPELINES=[
                'crab_soccer.pipelines.JsonWriterPipeline',
#                 'crab_soccer.pipelines.DBPipeline',
                ]

import sys

reload(sys) 
sys.setdefaultencoding('utf8')  # @UndefinedVariable
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../..")))
os.environ['DJANGO_SETTINGS_MODULE'] = 'soccer.settings'
