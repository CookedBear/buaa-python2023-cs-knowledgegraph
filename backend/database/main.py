from cnmooc import cnmooc_search
from icourse163 import icourse163_search
from icourses import icourses_search
from imooc import imooc_search
from bilibili import bilibili_search
from study163 import study163_search

if __name__ == '__main__':
    keyword = input('keyword')
    icourse163 = icourse163_search(keyword)
    imooc = imooc_search(keyword)
    bilibili = bilibili_search(keyword)
    icourses = icourses_search(keyword)
    cnmooc = cnmooc_search(keyword)
    study163 = study163_search(keyword)
