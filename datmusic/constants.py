import os

__version__ = "1.2.3"
DATMUSIC_API_ENDPOINT = os.getenv("DATMUSIC_API_ENDPOINT", "https://datmusic-api.dev/search/")
INLINE_QUERY_CACHE_TIME = 12 * 30 * 24 * 60 * 60 # 1 year

DEFAULT_HEADERS = {
	'User-Agent': os.getenv("DATMUSIC_USER_AGENT", "datmusic-telegram-bot v{}".format(__version__))
}

LINKS_MODE_SUFFIX = " /links"
