from importlib.metadata import version
if version('moviepy') < '1.0.0':
    import imageio
    imageio.plugins.ffmpeg.download()

from moviepy.editor import *
MP4_filename = 'うさぎさんです'
video = VideoFileClip(f"./{MP4_filename}.mp4")\
    .resize(0.5) # 适当减少该数组以适合作为表情包尺寸（<5mb）
video.write_gif(f"./{MP4_filename}.gif")
