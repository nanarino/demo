from pyquery import PyQuery as pq

import requests
try:
    r = requests.get('https://baidu.com', timeout=3)
finally:
    jquery = pq(r.text)

    src = jquery("img").eq(0).attr("src")

    print(src)
