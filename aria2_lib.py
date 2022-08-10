import aria2p


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


def batch_add_magnets(magnets: list):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret="hcy1997912"
        )
    )
    for magnet in magnets:
        aria2.add_magnet(magnet)
