import requests
from requests_toolbelt.utils import dump
from hashlib import md5

key = "6key_cibaifanyicjbysdlove1"
q = input("请输入你要翻译的单词::")
key += q
s_md5 = md5()
s_md5.update(key.encode(encoding='utf-8'))
sign = s_md5.hexdigest()[:16]
params = {
    'c': 'trans',
    'm': 'fy',
    'client': '6',
    'auth_user': 'key_ciba',
    'sign': sign
}
data = {
    'from': "auto",
    'to': 'auto',
    'q': q
}
url = "https://ifanyi.iciba.com/index.php?"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
req = requests.post(url=url, headers=headers, params=params, data=data)
print(q,"::",req.json()["content"]["out"])
#data = dump.dump_all(req)
#print(data.decode('utf-8'))
