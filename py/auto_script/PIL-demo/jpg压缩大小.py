from PIL import Image
import os,re,warnings

warnings.filterwarnings("error", category=UserWarning)

folder = './out'

def o(path):
    im = Image.open(path).convert("RGB")
    width, height = im.size[0], im.size[1]
    newPath = f'{folder}/{img}'
    im.save(newPath)
    while (size := (os.path.getsize(newPath) / 1024)) >1000:
        width, height = round(width * 0.9), round(height * 0.9)
        im = im.resize((width, height), Image.ANTIALIAS)
        im.save(newPath)
  
if __name__ == '__main__':
    ls = list(filter(lambda file: not os.path.isdir(file),
                     os.listdir(os.getcwd())))
    ls = list(
        filter(lambda name: bool(re.findall(r'(^.*\.jpg$)|(^.*\.JPG$)', name)),
               ls))
    ls.sort()
    os.makedirs(folder)
    for img in ls:
        try:
            o(img)
            print(f'{img}: ok ')
        except UserWarning as e:
            print(f'{img}: {e}')
            # UserWarning: Corrupt EXIF data?
        except OSError as e:
            print(f'{img}: {e}')
            # OSError: image file is truncated?

    