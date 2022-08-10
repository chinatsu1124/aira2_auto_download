import magnet_scrapy as ms
import aria2_lib as aria2
from anime import Anime

animes = [Anime(name='Lycoris Recoil',
                year='2022',
                keyword='【喵萌奶茶屋】+莉可丽丝+1080+简体'),
          Anime(name='Uncle from Another World',
                year='2022',
                keyword='【喵萌奶茶屋】+异世界舅舅+1080+简日双语'),
          Anime(name='Summer Time Rendering',
                year='2022',
                keyword='【喵萌奶茶屋】+夏日重现+1080+简日')]
# ANIME_DICT = {
#     'Lycoris Recoil (2022)': '【喵萌奶茶屋】+莉可丽丝+1080+简体',
#     'Uncle from Another World (2022)': '【喵萌奶茶屋】+异世界舅舅+1080+简日双语',
#     'Summer Time Rendering (2022)': '【喵萌奶茶屋】+夏日重现+简日+1080'
# }

for anime in animes:
    dmhy_url = 'https://share.dmhy.org/topics/rss/rss.xml?keyword='
    xml = ms.get_magnets(dmhy_url+anime.keyword)
    if xml != 0:
        item_dict = ms.analyse_xml(xml)
        aria2.batch_add_magnets(anime.get_dir_name(), item_dict)
