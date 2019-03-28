import json
import collections as cl
import googlemaps

def add_search(data):

    for key in data.keys():
        if isinstance(data[key], dict):
            add_search(data[key])
        if isinstance(data[key], list):
            break
        else:
            if (key == "text"):
                add_shop_name(split_name(data[key]))

res = cl.OrderedDict()
n = 0
def add_shop_name(name):
    global n
    n += 1
    res[n] = name

def split_name(value):
    list = value.split("\n")
    return list[0]

def append_shop(res, data):
    auth_key = "your-key"
    gmaps = googlemaps.Client(key=auth_key)

    for n in data.keys():
        geo_result = gmaps.geocode(res[int(n)])
        lat = geo_result[0]["geometry"]["location"]["lat"]
        lng = geo_result[0]["geometry"]["location"]["lng"]
        dic = data[n]
        dic["geocode"] = {"lat" : lat, "lng" : lng}

    for n in data.keys():
        dic = data[n]
        dic["shopname"] = res[int(n)]
    # shopnameを追加したjsonを保存する
    with open("data/json/add_shopname_tanreisan.json", 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    with open('data/json/parsed_tanreisan.json', encoding = 'utf-8') as f:
        data = json.load(f)
        add_search(data)
        append_shop(res, data)