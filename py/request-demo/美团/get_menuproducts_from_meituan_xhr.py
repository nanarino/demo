import json, csv
XHR_file = './h5.waimai.meituan.com.har'
csv_file = './h5.waimai.meituan.com.csv'
table = []
with open(XHR_file,encoding='utf-8') as har: # https://h5.waimai.meituan.com/waimai/mindex/menu?utm_source=5913&mtShopId=990717024543786
    xhr_entries = json.loads(har.read())["log"]["entries"]
    xhr_entries = filter(lambda xhr : 'menuproducts' in xhr["request"]['url'], xhr_entries)
    res_entries = map(lambda xhr : xhr["response"]["content"]['text'], xhr_entries)
    for data in res_entries:
        for i in json.loads(data)["data"]["spuList"]:
            table.append(tuple([i["spuName"], i["spuId"], i["tag"], i["saleVolume"], i["originPrice"], i["currentPrice"], i["sellStatus"], i["skuList"][0]["skuId"], i["skuList"][0]["spec"], i["skuList"][0]["soldStatus"], i["skuList"][0]["realStock"], i["skuList"][0]["skuPromotionInfo"]]))

with open(csv_file, "w", encoding='utf-8', newline='') as csvFile:
    writer = csv.writer(csvFile)
    fileHeader = ("spuName", "spuId", "tag", "saleVolume", "originPrice", "currentPrice", "sellStatus", "skuId", "spec", "soldStatus", "realStock", "skuPromotionInfo")
    writer.writerow(fileHeader)
    for i in table:
        try:
            writer.writerow(i)
        except UnicodeEncodeError as e:
            print(e)