import magnet_scrapy as ms
import aria2_lib as aria2

keyword_url = 'https://share.dmhy.org/topics/rss/rss.xml?keyword=【喵萌奶茶屋】+异世界舅舅+1080+简日双语'
# keyword_url = 'https://share.dmhy.org/topics/rss/rss.xml?keyword=甲铁城'
item_dict = ms.analyse_url(keyword_url)
aria2.batch_add_magnets(item_dict)
