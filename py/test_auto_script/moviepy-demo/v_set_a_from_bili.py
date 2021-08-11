from importlib.metadata import version
if version('moviepy') < '1.0.0':
    import imageio
    imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from pathlib import Path
import json
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
            audio = AudioFileClip(str(i / Path(d) / Path('audio.m4s')))
            video = VideoFileClip(str(i / Path(d) / Path('video.m4s')))
            video.set_audio(audio).write_videofile(f'{opt_file}')
        except Exception as e:
            print(f'出错 跳过 {opt_file}')
            print(e)

