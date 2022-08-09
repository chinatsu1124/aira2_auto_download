import aria2p
import magnet_scrapy as ms

# initialization, these are the default values
aria2 = aria2p.API(
    aria2p.Client(
        host="http://chinatsu1124.imwork.net",
        port=6800,
        secret="hcy1997912"
    )
)

keyword_url = 'https://share.dmhy.org/topics/rss/rss.xml?keyword=【喵萌奶茶屋】+异世界舅舅+1080+简日双语'
item_dict = ms.analyse_text(ms.get_magnets(keyword_url).text)
for key in item_dict:
    aria2.add_magnet(item_dict[key])
