import json
lst = [
    1, 2, 3, 7, 5, 1, 4, 5, 6, 1, 4, 6, 2, 5, 3, 1, 5, 6, 3, 8, 5, 6, 4, 1, 5,
    3, 7, 1, 4, 2, 7, 1, 3, 9, 4, 5
]

from collections import Counter
print(
    json.dumps(dict(Counter(lst)),
               sort_keys=True,
               indent=2,
               separators=(',', ':'),
               ensure_ascii=False))

from functools import reduce
dic = reduce(lambda r, x: r.update({x: r.get(x, 0) + 1}) or r, lst, dict())
"""由JavaScript的 arr.reduce((x,y)=>((x[y]?x[y]++:x[y]=1),x),{}) 魔改而成"""
print(
    json.dumps(dic,
               sort_keys=True,
               indent=2,
               separators=(',', ':'),
               ensure_ascii=False))
