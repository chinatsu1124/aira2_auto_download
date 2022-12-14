import magnet_scrapy as ms
import aria2_lib as aria2
from anime import Anime
import time

animes = [Anime(name='Lycoris Recoil',
                year='2022',
                keyword='【喵萌奶茶屋】+莉可丽丝+1080+简体',
                season='01'),
          Anime(name='Uncle from Another World',
                year='2022',
                keyword='【喵萌奶茶屋】+异世界舅舅+1080+简日双语',
                season='01'),
          Anime(name='Summer Time Rendering',
                year='2022',
                keyword='【喵萌奶茶屋】+夏日重现+1080+简日',
                season='01'),
          Anime(name='OVERLORD',
                year='2015',
                keyword='桜都字幕组+overlord+简体内嵌',
                season='04')
          ]


if __name__ == '__main__':
    for anime in animes:
        dmhy_url = 'https://share.dmhy.org/topics/rss/rss.xml?keyword='
        print(f'开始更新{anime.name}...')
        xml = ms.get_magnets(dmhy_url + anime.keyword)
        if xml != 0:
            item_dict = ms.analyse_xml(xml)
            move_dict = aria2.batch_add_magnets(anime.name, anime.get_dir_name(), anime.season, item_dict)
            if move_dict:
                print('开始等待下载完成...')
                count = len(move_dict)
                while count > 0:
                    time.sleep(20)
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    for gid, save_path in move_dict.items():
                        follow_download_gid, follow_download_progress = aria2.get_follow_progress_by_gid(gid)
                        if follow_download_progress == 100 and not aria2.get_is_complete(follow_download_gid):
                            count -= aria2.place_on_file(follow_download_gid, save_path)
                print(f'{anime.name}:番剧下载并归档完成。')
        print('-' * 40)
