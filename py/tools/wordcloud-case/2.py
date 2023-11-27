from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba.posseg as pseg
from jieba import analyse

with open(Path(__file__).parent.joinpath('1.txt'), encoding='utf-8') as f:
    text=f.read()

words = pseg.cut(text)
nouns = []
verbs = []
adjs = []
for word, flag in words:
    if 'n' in flag:
        nouns.append(word)
    elif 'v' in flag:
        verbs.append(word)
    elif 'a' in flag:
        adjs.append(word)
tfidf = analyse.extract_tags(' '.join(nouns+verbs+adjs), topK=100, withWeight=True, allowPOS=())

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    if word in nouns:
        return 'red'
    if word in verbs:
        return 'cyan'
    if word in adjs:
        return 'green'

wc = WordCloud(font_path='simhei.ttf', background_color="white", width=800, height=800)
wc.generate_from_frequencies(dict(tfidf))
wc.recolor(color_func=color_func)

plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
