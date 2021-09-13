import jwt
import datetime
import time

key = '123456'

token = jwt.encode({
    # 开始时间
    "iat": datetime.datetime.utcnow(),
    # 过期时间
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=2),
    # 签发者
    "iss": '☘',
    'data': {
        "username": "admin",
        "time": datetime.datetime.today().isoformat()
    }
}, key)

print(token)

token_decoded = jwt.decode(token, key, algorithms=["HS256"])

print(token_decoded)

time.sleep(3) #等过期

try:
    token_decoded = jwt.decode(token, key, algorithms=["HS256"])
except Exception as e:
    print(e)
