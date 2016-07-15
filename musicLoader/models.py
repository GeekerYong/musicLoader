# -*- coding:utf-8 -*-
import requests
import re
import urllib2

class Song:
    int = 0
    title = ''
    name = ''
    songID = 0
    album = ''
    albumId = 0
    albumPic = ''
    artists = ''
    url = ''
    def __init__(self):
        int = 0
        title = ''
        name = ''
        songID = 0
        album = ''
        albumId = 0
        albumPic = ''
        artists = ''
        url = ''


SongRecord = {}
ListRecord = {}

def HttpGet(url):
    r = requests.get('http://httpbin.org/get')

def getId(url):
    pattern = re.compile('[1-9][0-9]{3,11}')
    print "音乐链接为:"+url
    id = pattern.findall(url)
    print "匹配结果为:"+id[0]
    return id[0]
