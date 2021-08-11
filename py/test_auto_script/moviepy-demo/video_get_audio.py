from importlib.metadata import version
if version('moviepy') < '1.0.0':
    import imageio
    imageio.plugins.ffmpeg.download()

from moviepy.editor import *

audio = VideoFileClip('./av54781227.blv').audio

audio.write_audiofile('./av54781227.mp3')
