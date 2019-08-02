from pathlib import Path
import matplotlib.pyplot as plt
import jieba
from jieba import analyse
from wordcloud import WordCloud

with open(Path(__file__).parent.joinpath('1.txt'), encoding='utf-8') as f:
    text=f.read()

seg_list = jieba.cut(text, cut_all=False)

tfidf = analyse.extract_tags(' '.join(seg_list), topK=100, withWeight=True, allowPOS=())

wc = WordCloud(font_path='simhei.ttf', background_color="white", width=800, height=800)
wc.generate_from_frequencies(dict(tfidf))

plt.imshow(wc)
plt.axis("off")
plt.show()