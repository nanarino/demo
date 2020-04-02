import json
import csv
_id = 983467099995385
csvFile = open(str(_id)+"_促销.csv", "w")#, encoding='utf-8')
writer = csv.writer(csvFile)
fileHeader = ("spuName", "spuId", "tag", "saleVolume", "originPrice", "currentPrice", "sellStatus", "skuId", "spec", "soldStatus", "realStock", "skuPromotionInfo")
writer.writerow(fileHeader)
filename = str(_id)+'_促销.json'

with open(filename, encoding="utf-8") as f:
    data = json.loads(f.read())["data"]["categoryList"][0]["spuList"]
    table = []
    for i in data:
        table.append(tuple([i["spuName"], i["spuId"], i["tag"], i["saleVolume"], i["originPrice"], i["currentPrice"], i["sellStatus"], i["skuList"][0]["skuId"], i["skuList"][0]["spec"], i["skuList"][0]["soldStatus"], i["skuList"][0]["realStock"], i["skuList"][0]["skuPromotionInfo"]]))

'''
from pprint import pprint
pprint(list(table), width=60, compact=True)
'''
for i in table:
    try:
        writer.writerow(i)
    except UnicodeEncodeError:
        pass
csvFile.close()
