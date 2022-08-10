import magnet_scrapy as ms
import aria2_lib as aria2

ANIME_DICT = {
    'Lycoris Recoil (2022)': 'https://share.dmhy.org/topics/rss/rss.xml?keyword=【喵萌奶茶屋】+莉可丽丝+1080+简体',
    'Uncle from Another World (2022)': 'https://share.dmhy.org/topics/rss/rss.xml?keyword=【喵萌奶茶屋】+异世界舅舅+1080+简日双语'
}

for anime_name, anime_url in ANIME_DICT.items():
    xml = ms.get_magnets(anime_url)
    if xml != 0:
        item_dict = ms.analyse_xml(xml)
        aria2.batch_add_magnets(anime_name, item_dict)
