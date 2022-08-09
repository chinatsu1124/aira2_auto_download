import aria2p


def batch_del_download(keyword):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://192.168.1.100",
            port=6800,
            secret="hcy1997912"
        )
    )
    for download in aria2.get_downloads():
        if keyword in download.name:
            res = download.remove()
            if res:
                print(f'{download.gid}:删除成功。')


batch_del_download('Isekai Ojisan')
