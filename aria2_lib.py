import aria2p
import os
import re
import shutil


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


def batch_add_magnets(anime_name: str, anime_dir: str, magnets: dict):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret="hcy1997912"
        )
    )
    anime_dir = f'/home/chinatsu1124/disk2/影视/剧集/{anime_dir}/Season 1'
    episode_list = get_episode_list(anime_dir)
    move_dict = {}
    for key, value in magnets.items():
        if key in episode_list:
            print(f'{anime_name}:第{key}集已存在。')
        else:
            download = aria2.add_magnet(value)
            move_dict[download.gid] = os.path.join(anime_dir, f'{anime_name} S01E{key}.mp4')
            print(f'{anime_name}:成功添加第{key}集下载任务。')
    return move_dict


# 获取已下载集列表
def get_episode_list(path: str):
    episode_list = []
    for file_name in os.listdir(path):
        episode = re.search(r'S01E(\d{2})', file_name).group(1)
        episode_list.append(episode)
    print(episode_list)
    return episode_list


def show_progress_by_gid(gid):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret="hcy1997912"
        )
    )
    download = aria2.get_download(gid)
    print(f'{download.name}:{download.progress}')
    return download.progress


def place_on_file(gid, save_path):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret="hcy1997912"
        )
    )
    download = aria2.get_download(gid)
    download_path = download.files[0].path
    download.remove()
    shutil.move(download_path, save_path)
    return 1
