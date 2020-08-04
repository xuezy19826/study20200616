# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          06
# Description:   使用requests模块访问网络API获取数据
# Author:        xuezy
# Date:          2020/7/28 18:01
# --------------------------------------------------------------
import requests
import json


def main():
    # 地址有问题，不能用
    res = requests.get("http://api.avatardata.cn/Aqi/CityList?key=0efe0f0cf7d742e692d7d05279d72e48")
    data_model = json.loads(res.text)
    for news in data_model['result']:
        print(news)


if __name__ == '__main__':
    main()
