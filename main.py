from icourse163 import icourse163_search
from imooc import imooc_search
from bilibili import bilibili_search
if __name__ == '__main__':
    keyword = input()
    icourse163_search(keyword)
    imooc_search(keyword)
    bilibili_search(keyword)
