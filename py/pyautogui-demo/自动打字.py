
import time
time.sleep(5)

import pyautogui
secs_between_keys = 0.01



#https://10fastfingers.com/typing-test/english
#f12 console : JSON.stringify(row1_string.match(/\w*(?=<\/span>)/g).filter((v)=>(v!="")))

h=["should","live","down","school","head","where","word","began","more","until","of","want","had","point","night","form","below","made","car","write","as","many","must","list","people","long","men","kind","home","example","seem","his","well","has","high","open","name","still","would","being","with","still","end","America","an","every","feet","no","mountain","always","study","boy","air","can","like","America","me","those","there","own","second","another","when","him","earth","hard","new","let","soon","people","would","below","tell","down","got","read","story","no","move","song","did","right","their","idea","in","form","something","here","different","those","under","at","little","begin","away","the","after","know","name","small","before","part","only","learn","last","sound","through","tree","while","said","first","even","said","you","America","ask","day","time","thought","turn","mean","children","number","saw","could","almost","eat","set","went","she","his","can","talk","her","will","car","enough","sentence","seem","out","later","never","run","then","his","being","almost","do","picture","large","do","both","to","ask","great","put","example","open","old","my","think","light","boy","does","way","for","then","man","over","is","the","mother","well","stop","our","always","very","soon","list","work","young","face","thing","side","which","find","say","river","last","does","about","picture","come","where","on","each","think","close","her","side","it","left","question","point","only","we","very","letter","food","between","oil","line","not","place","work","should","quite","another","cut","song","found","an","use","talk","on","call","river","by","list","another","long","sentence","carry","found","really","move","after","mother","food","up","family","quick","keep","use","when","face","between","may","really","word","not","much","an","together","miss","she","one","live","s","something","day","there","they","took","city","old","begin","important","each","white","own","some","city","boy","above","try","will","he","night","time","stop","you","saw","world","oil","really","know","often","let","important","life","soon","took","are","young","want","city","had","follow","time","again","just","went","paper","something","sometimes","often","later","so","while","side","year","great","are","spell","big","then","once","start","way","grow","who","been","give","turn","learn","its","let","we","were","some","follow","near","letter","mile","animal","study","any","pl"]

for i in h:
    pyautogui.typewrite(i, interval=secs_between_keys)
    pyautogui.typewrite(['space'], interval=secs_between_keys)

