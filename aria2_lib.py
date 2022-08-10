import aria2p
import os.path
import re


def batch_del_downloads(keyword: str):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret="hcy1997912"
        )
    )
    for download in aria2.get_downloads():
        if keyword in download.name:
            res = download.remove()
            if res:
                print(f'{download.gid}:删除成功。')


def batch_add_magnets(magnets: dict):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret="hcy1997912"
        )
    )
    episode_list = get_episode_list(r'/home/chinatsu1124/disk2/影视/剧集/Uncle from Another World (2022)/Season 1')
    for key, value in magnets.items():
        if key in episode_list:
            print(f'第{key}集已存在。')
        else:
            aria2.add_magnet(value)
            print(f'成功添加第{key}集下载任务。')

# 获取已下载集列表
def get_episode_list(path: str):
    episode_list = []
    for file_name in os.listdir(path):
        episode = re.search(r'S01E(\d{2})', file_name).group(1)
        episode_list.append(episode)
    print(episode_list)
    return episode_list
