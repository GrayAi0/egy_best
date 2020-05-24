import requests
from fake_headers import Headers
from .exceptions import BotDetectedException

class Settings:
	""" main settings stored in this class """
	site = 'https://egy.best'
	AUTO_INIT = False # better false for speed
	headers = Headers('chrome', 'win').generate()
	proxy = None
	classes = dict(
			movie='Movie',
			actor='Actor',
			series='Serie',
			season='Season',
			episode='Episode',
		)

	@classmethod
	def mainsite(cls) -> str:
		""" return a website that can be used to browser movies,
		or raise Exception if the bot detcted or due the geolocation
		restriction
		"""
		r = requests.get(cls.site, headers=cls.headers, proxies=cls.proxy)
		if 'egy' in r.url:
			return r.url
		raise BotDetectedException
