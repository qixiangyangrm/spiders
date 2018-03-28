import requests
from lxml import etree

url_list = ['https://bj.lianjia.com/ershoufang/haidian/',
 "https://bj.lianjia.com/ershoufang/tongzhou/",
 "https://bj.lianjia.com/ershoufang/fengtai/",
 "https://bj.lianjia.com/ershoufang/dongcheng/",
 "https://bj.lianjia.com/ershoufang/xicheng/",
 "https://bj.lianjia.com/ershoufang/changping/",
 "https://bj.lianjia.com/ershoufang/shijingshan/",
 "https://bj.lianjia.com/ershoufang/daxing/",
 "https://bj.lianjia.com/ershoufang/chaoyang/",
 "https://bj.lianjia.com/ershoufang/fangshan/",
 "https://bj.lianjia.com/ershoufang/huairou/",
 "https://bj.lianjia.com/ershoufang/yizhuangkaifaqu/",
 "https://bj.lianjia.com/ershoufang/mentougou/",
 "https://bj.lianjia.com/ershoufang/pinggu/",
 "https://bj.lianjia.com/ershoufang/miyun/",
 "https://bj.lianjia.com/ershoufang/shunyi/",
 "https://bj.lianjia.com/ershoufang/yanqing/",
 "https://lf.lianjia.com/xiaoqu/yanjiao/",
 "https://lf.lianjia.com/xiaoqu/xianghe/"]

for url in url_list:
    response = requests.get(url).text
    html = etree.HTML(response)

    url_list = html.xpath('//div[@data-role="ershoufang"]/div[2]/a')
    print(len(url_list))
    for p in url_list:
        url_ = p.xpath('@href')[0]
        region_name = p.xpath('text()')[0]
        print(url_,region_name)