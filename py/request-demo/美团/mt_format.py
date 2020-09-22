import json
import csv
csvFile = open("990717024543786.csv", "w", encoding='gbk', newline='')
writer = csv.writer(csvFile)# https://h5.waimai.meituan.com/waimai/mindex/menu?utm_source=5913&mtShopId=990717024543786
fileHeader = ("spuName", "spuId", "tag", "saleVolume", "originPrice", "currentPrice", "sellStatus", "skuId", "spec", "soldStatus", "realStock", "skuPromotionInfo")
writer.writerow(fileHeader)
table = []
with open ('food.json',encoding='utf-8') as f:
    data = json.loads(f.read())["data"]["categoryList"][0]["spuList"]
    for i in data:
        table.append(tuple([i["spuName"], i["spuId"], i["tag"], i["saleVolume"], i["originPrice"], i["currentPrice"], i["sellStatus"], i["skuList"][0]["skuId"], i["skuList"][0]["spec"], i["skuList"][0]["soldStatus"], i["skuList"][0]["realStock"], i["skuList"][0]["skuPromotionInfo"]]))
with open ('menuproducts.txt',encoding='utf-8') as f:
    for line in f:
        for i in json.loads(line)["data"]["spuList"]:
            table.append(tuple([i["spuName"], i["spuId"], i["tag"], i["saleVolume"], i["originPrice"], i["currentPrice"], i["sellStatus"], i["skuList"][0]["skuId"], i["skuList"][0]["spec"], i["skuList"][0]["soldStatus"], i["skuList"][0]["realStock"], i["skuList"][0]["skuPromotionInfo"]]))
for i in table:
    try:
        writer.writerow(i)
    except UnicodeEncodeError as e:
        print(e)
csvFile.close()