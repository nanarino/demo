from importlib.metadata import version
if version('moviepy') < '1.0.0':
    import imageio
    imageio.plugins.ffmpeg.download()

from moviepy.editor import *
audio = AudioFileClip('./audio.m4s')
video = VideoFileClip('./video.m4s')
video.set_audio(audio).write_videofile('./av.mp4')
