from bilibili import bilibili_search
from cnmooc import cnmooc_search
from icourse163 import icourse163_search
from icourses import icourses_search
from imooc import imooc_search
from study163 import study163_search

if __name__ == '__main__':
    keyword = '操作系统'
    # icourse163_search(keyword)
    # imooc_search(keyword)
    # bilibili_search(keyword)
    # icourses_search(keyword)
    cnmooc_search(keyword)
    # study163_search(keyword)
