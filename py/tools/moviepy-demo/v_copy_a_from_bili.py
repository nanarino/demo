"""秒合
如果没有ffmpeg的环境变量可以用imageio的ffmpeg, get_ffmpeg_exe获取路径
>>> import imageio_ffmpeg
>>> imageio_ffmpeg.get_ffmpeg_exe()
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\imageio_ffmpeg\\binaries\\ffmpeg-win64-v4.2.2.exe'
"""

import json
from pathlib import Path
import os
os.system("")
opt_dir = Path('./opt')
opt_dir.mkdir(parents=True, exist_ok=True)
ls = [p for p in Path.cwd().iterdir() if p.is_dir() and p.name != 'opt']
for i in ls:
    with open(i / Path('entry.json'), 'r', encoding='utf-8') as entry:
        part = ''.join(s for s in json.loads(entry.read())[
                       "page_data"]['part'] if s.isalnum())
    opt_file = opt_dir / Path(f'{part}.mp4')
    if opt_file.is_file():
        print(f'已存在 跳过 {opt_file}')
    else:
        try:
            d = [p for p in i.iterdir() if p.is_dir()
                 and p.name.isdecimal()][0].name
            audio_path = i / Path(d) / Path('audio.m4s')
            video_path = i / Path(d) / Path('video.m4s')
            os.system(
                f"ffmpeg -i {audio_path} -i {video_path} -c copy {opt_file}")
        except Exception as e:
            print(f'出错 跳过 {opt_file}')
            print(e)
input('已完成')
