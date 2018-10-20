import json
import os
import re

from pixivpy3 import AppPixivAPI

with open('credentials.json') as cf:
    credentials = json.load(cf)

with open('urls.txt') as uf:
    urls = [u.split('/')[-1] for u in uf if 'pixiv.net' in u]

ids = [re.findall(r'\d+', id)[0] for id in urls]

api = AppPixivAPI()
api.login(credentials['email'], credentials['password'])

for id in ids:
    json_result = api.illust_detail(id)
    api.download(json_result.illust['meta_single_page']['original_image_url'])
