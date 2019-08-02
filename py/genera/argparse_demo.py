"""
cmd中测试：

python -argparse_demo.py -s

python -argparse_demo.py -a

"""

import argparse

parser = argparse.ArgumentParser(description='argparse tester')

parser.add_argument("-s", "--shutdown", help="设置一小时后关机", action="store_true")

parser.add_argument("-a", "--annul", help="取消关机计划", action="store_true")

args = parser.parse_args()

import subprocess
if args.shutdown:
    s = subprocess.Popen("shutdown -s -t 3600", shell=True)
    s.wait()
    print("设置成功")

if args.annul:
    s = subprocess.Popen("shutdown -a", shell=True)
    s.wait()
    print("取消成功")