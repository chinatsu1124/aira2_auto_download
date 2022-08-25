import requests
import re
import xml.etree.ElementTree as ET


def get_magnets(url):
    i = 0
    while True:
        try:
            with requests.get(url, timeout=10, stream=True) as r:
                if r.status_code == 200:
                    print('获取xml成功')
                    return r.text
                else:
                    print(f'网络错误代码为{r.status_code}')
                    return 0
        except requests.exceptions.ConnectTimeout:
            print(f'网络连接超时,重试第{i}次')
        except requests.exceptions.ReadTimeout:
            print(f'网络连接读取超时,重试第{i}次')
        finally:
            i += 1
    return 0


def analyse_xml(xml):
    item_dict = {}
    root = ET.fromstring(xml)
    for item in root.iter('item'):
        r = re.search(r"\[(\d{2})]", item.find('title').text).group(1)
        # 因为资源是从新到旧,所以后续如果有重复集即舍弃
        if r not in item_dict:
            item_dict[r] = item.find('enclosure').get('url')
        else:
            print(item.find('title').text + ':重复,已舍弃。')
    return item_dict
