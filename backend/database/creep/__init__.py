from backend.database.cnmooc import cnmooc_search
from backend.database.bilibili import bilibili_search


def bilibili(key):
    return bilibili_search(key)


def cnmooc(key):
    return cnmooc_search(key)


def imooc(key):
    return imooc(key)
