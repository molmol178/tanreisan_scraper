import json
import collections as cl


def search(data):
    for key in data.keys():
        if isinstance(data[key], dict):
            search(data[key])
        if isinstance(data[key], list):
            for item in data[key]:
                if isinstance(item, dict):
                    search(item)
                else:
                    has_target(key, data[key], res)
                    break
                    
        else :
            has_target(key, data[key], res)

    with open("data/json/parsed_tanreisan.json", 'w') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)

res = cl.OrderedDict()
n = 0
child_res = cl.OrderedDict()

def has_target(key, value, res):
    if (key == "__typename"):
        global n
        global child_res

        child_res = cl.OrderedDict()
        n += 1
        res[n] = None

    elif (key == "display_url" or key == "text" or key == "tags" or key == "edge_media_preview_like" or key == "shortcode"):
        child_res[key] = value
        res[n] = child_res

if __name__ == "__main__":
    with open('data/json/tanreisan.json', encoding = 'utf-8') as f:
        data = json.load(f)
        search(data)
