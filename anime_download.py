import aria2p

# initialization, these are the default values
aria2 = aria2p.API(
    aria2p.Client(
        host="http://chinatsu1124.imwork.net",
        port=6800,
        secret="hcy1997912"
    )
)

# list downloads
downloads = aria2.get_downloads()

for download in downloads:
    print(download.name, download.download_speed)

http_uri = "https://img.alicdn.com/imgextra/i4/O1CN01sBgsI61EaaWZghWN9_!!6000000000368-2-tps-484-316.png"

download = aria2.add(http_uri, {'out': '123.png'})
