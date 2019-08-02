import json
import requests
import csv

shop_id = 2233310913
csvFile = open("qs_%s.csv" % shop_id, "w")  #, encoding='utf-8')
writer = csv.writer(csvFile)
fileHeader = ('month_saled', 'month_sell', 'sale_price', 'upc', 'upc_name')
writer.writerow(fileHeader)

list_res = requests.get(
    'https://newretail.ele.me/newretail/shop/getshopcategoryinfo?shop_id=%s' %
    shop_id)
list_data = json.loads(list_res.text)['result']
list_data = filter(lambda i: i.get('cat_id', 0), list_data)


def del_dict(i, del_list: list):
    for j in del_list:
        i.update({j: ''})
        del i[j]


id_set = set()

for i in list_data:
    del_dict(i, ['is_selected', 'type', 'description'])
    if (i.get('detail', 0)):
        for j in i['detail']:
            del_dict(j, ['is_selected', 'type', 'description'])
            id_set.add(j['id'])
    else:
        id_set.add(i['id'])
'''
def pprint(data):
    pp = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
    print(pp)

print(id_set)
'''

for i in range(len(id_set)):
    id = id_set.pop()
    id_res = requests.get(
        'https://newretail.ele.me/newretail/shop/getfoodsbycategory?shop_id=%s&category_id='
        % shop_id + id + '&type=1')
    try:
        id_data = json.loads(id_res.text)['result']['detail'][0]['foods']
    except Exception:
        try:
            id_data = json.loads(id_res.text)['result']['foods']
        except Exception:
            continue

    for i in id_data:
        del_dict(i, [
            'cat1_id', 'category_ids', 'description', 'dish_activity',
            'drug_info', 'ele_food_id', 'ele_item_id', 'ele_sku_id',
            'ele_vfood_id', 'enabled', 'ext', 'height', 'illustration',
            'index', 'is_selected', 'left_num', 'length', 'photos',
            "preminus_weight", "process_detail", "process_type", "propertys",
            "purchase_limit_sku", "purchase_limit_upc", "rate",
            "rating_amount", "rtf", "sku_id", "brand_name", "cat1_name",
            "current_price", "default_sale_unit", "discount", "market_price",
            "minimum", "minimum_text", "need_ice", "original_price",
            "sale_step", "sale_unit", "sale_unit_text", "sell_text",
            "shelf_number", "sku_property", "stock_text", "weight",
            "weight_flag", "wid", "width", "summary", "upc_id", "url",
            "url_ele_hash"
        ])
        yz_data = []
        for j in fileHeader:
            yz_data.append(str(i[j]))
        try:
            writer.writerow(yz_data)
        except UnicodeEncodeError:
            pass

csvFile.close()