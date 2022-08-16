import aria2p
import os
import re
import shutil

__aria2__ = aria2p.API(
    aria2p.Client(
        host="http://127.0.0.1",
        port=6800,
        secret="hcy1997912"
    )
)


def batch_add_magnets(anime_name: str, anime_dir: str, anime_season, magnets: dict):
    anime_dir = f'/home/chinatsu1124/disk2/影视/剧集/{anime_dir}/Season {int(anime_season)}'
    episode_list = get_episode_list(anime_dir)
    move_dict = {}
    for key, value in magnets.items():
        if key in episode_list:
            print(f'{anime_name}:第{key}集已存在。')
        else:
            download = __aria2__.add_magnet(value)
            move_dict[download.gid] = os.path.join(anime_dir, f'{anime_name} S{anime_season}E{key}.mp4')
            print(f'{anime_name}:成功添加第{key}集下载任务。')
    return move_dict


# 获取已下载集列表
def get_episode_list(path: str):
    episode_list = []
    for file_name in os.listdir(path):
        episode = re.search(r'E(\d{2})', file_name).group(1)
        episode_list.append(episode)
    return episode_list


def get_follow_progress_by_gid(gid):
    download = __aria2__.get_download(gid)
    try:
        follow_download = download.followed_by[0]
        print(f'{follow_download.name}:{follow_download.progress}')
        return follow_download.gid, follow_download.progress
    except IndexError:
        print(f'{download.gid}:未完成METADATA下载')
        return '0', 0


def place_on_file(gid, save_path):
    download = __aria2__.get_download(gid)
    download_path = download.files[0].path
    download.remove()
    try:
        shutil.move(download_path, save_path)
        return 1
    except FileNotFoundError:
        return 0


def get_is_complete(gid):
    download = __aria2__.get_download(gid)
    return download.is_complete


def batch_del_downloads(keyword: str):
    for download in __aria2__.get_downloads():
        if keyword in download.name:
            res = download.remove()
            if res:
                print(f'{download.gid}:删除成功。')
