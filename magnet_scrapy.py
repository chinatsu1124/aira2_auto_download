import requests
import re
import xml.etree.ElementTree as ET


def get_magnets(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            print('获取xml成功')
            return r.text
        else:
            print(f'网络错误代码为{r.status_code}')
            return 0
    except requests.exceptions.ConnectTimeout:
        print('网络连接超时')
        return 0


def analyse_xml(xml):
    item_dict = {}
    root = ET.fromstring(xml)
    for item in root.iter('item'):
        r = re.search(r"\[(\d{2})]", item.find('title').text).group(1)
        item_dict[r] = item.find('enclosure').get('url')
        # item_dict[item.find('title').text] = item.find('enclosure').get('url')
    return item_dict
    # r = re.findall(r"magnet:\?xt=urn:btih:\w*", text)
    # for url in r:
    #     print(url)



