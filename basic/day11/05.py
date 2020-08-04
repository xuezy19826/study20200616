# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          05
# Description:   将字典或列表以JSON格式保存到文件中
# Author:        xuezy
# Date:          2020/7/28 17:40
# --------------------------------------------------------------
import json


def main():
    mydict = {
        'name': '测试',
        'age': 33,
        'qq': 1378234,
        'friends': ['王大锤', '李元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320},
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')


if __name__ == '__main__':
    main()
