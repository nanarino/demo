"""
每【10】秒访问一次指定页面
【3】秒内无响应就会发起警报
警报的音频为同级目录下的【835686.mp3】
"""
import requests
import time

from playsound import playsound
playsound('835686.mp3')
# termcolor模块不适用与win10以下版本 这里使用colorama模块
#from termcolor import colored
from colorama import init, Fore
init(autoreset=True)

while 1:
    try:
        r = requests.get('http://192.168.10.4:8076/front_index/goLogin',
                         timeout=3)
        sc = r.status_code
    except Exception:
        sc = 500
    finally:
        if not sc == 200:
            playsound('835686.mp3')
            #print(time.strftime("%Y-%m-%d %X") + "\t 状态码：" + colored(str(sc), "red"))
            print(
                time.strftime("%Y-%m-%d %X") + "\t 状态码：" + Fore.RED + str(sc) +
                Fore.RESET)
        else:
            print(
                time.strftime("%Y-%m-%d %X") + "\t 状态码：" + Fore.GREEN +
                str(sc) + Fore.RESET)
            time.sleep(10)

playsound('835686.mp3')