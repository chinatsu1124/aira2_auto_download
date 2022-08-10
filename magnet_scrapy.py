import requests
import re
import xml.etree.ElementTree as ET


def get_magnets(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r
        else:
            print(f'网络错误代码为{r.status_code}')
            return 0
    except:
        print('网络连接未响应')
        return 0


def analyse_url(url):
    text = get_magnets(url).text
    item_dict = {}
    root = ET.fromstring(text)
    for item in root.iter('item'):
        r = re.search(r"\[(\d{2})]", item.find('title').text).group(1)
        item_dict[r] = item.find('enclosure').get('url')
        # item_dict[item.find('title').text] = item.find('enclosure').get('url')
    return item_dict
    # r = re.findall(r"magnet:\?xt=urn:btih:\w*", text)
    # for url in r:
    #     print(url)



