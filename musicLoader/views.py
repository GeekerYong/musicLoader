# -*- coding:utf-8 -*-
import json
import md5
import urllib2

from django.shortcuts import render_to_response

import models


def queSongIndex(request):
    return render_to_response("song.html")

def queSong(request):
    songId = request.POST['songId']
    if songId!='':
        id = models.getId(songId)
        song = GetSongDetail(id)
        returnList = {
            'Title':song.title,
            'Name':song.name,
            'Id':song.songID,
            'Quesuccess':1
        }
    return render_to_response('song.html',returnList)

def playMusic(request):
    id = request.path.split('/')[2]
    id.encode('utf-8')
    song = GetSongDetail(id)
    returnList = {
        "Title":song.title,
        "AlbumPic":song.albumPic,
        "Name":song.title,
        "Artists":song.artists,
        "Album":song.album,
        "Url":song.url
    }
    return render_to_response("music.html",returnList)




#https://github.com/yanunon/NeteaseCloudMusic/
def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
    byte2 = bytearray(id)
    byte1_len = len(byte1)
    for i in xrange(len(byte2)):
        byte2[i] = byte2[i]^byte1[i%byte1_len]
    m = md5.new()
    m.update(byte2)
    result = m.digest().encode('base64')[:-1]
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result

def GetSongDetail(songId):
    song = models.Song()
    page = urllib2.urlopen("http://music.163.com/api/song/detail/?id=" + songId + "&ids=%5B" + songId + "%5D")
    jdata = json.load(page)
    song.__init__()
    song.title = jdata['songs'][0]['name']
    song.name = jdata['songs'][0]['artists'][0]['name']
    song.songID = int(songId)
    song.album = jdata['songs'][0]['album']['name']
    song.albumId = jdata['songs'][0]['album']['id']
    song.albumPic = jdata['songs'][0]['album']['picUrl']
    song.url = getUrl(jdata,songId,song.albumId)
    return song


def getUrl(jdata,songId,albumId):
    try:
        dfsId = int(jdata['songs'][0]['hMusic']['dfsId'])
        if dfsId == 0:
            dfsId = int(jdata['songs'][0]['mMusic']['dfsId'])
        else:
            if dfsId == 0:
                int(jdata['songs'][0]['mMusic']['lfsId'])
    except:
        url = albumGetUrl(albumId,songId)
        return url
    song_dfsId = str(dfsId)
    print song_dfsId
    encrypted_song_id = encrypted_id(song_dfsId)
    url = "http://m1.music.126.net/" + encrypted_song_id + "/" + song_dfsId + ".mp3"
    return url


def albumGetUrl(albumId,songId):
    print albumId
    req = urllib2.Request("http://music.163.com/api/album/" + str(albumId) + "?id=" + str(albumId))
    req.add_header("Cookie","appver=1.5.0.75771")
    req.add_header("Referer", "http://music.163.com/")
    page = urllib2.urlopen(req)
    jdata = json.load(page)
    url = ''
    for i in range(len(jdata['album']['songs'])):
        id = int(jdata['album']['songs'][i]['id'])
        sid = int(songId)
        print "id"
        print id
        print "sid"
        print sid
        if id == sid:
            print "匹配成功！"
            dfsId = int(jdata['album']['songs'][i]['hMusic']['dfsId'])
            if dfsId == 0:
                dfsId = int(jdata['album']['songs'][i]['mMusic']['dfsId'])
            else:
                if dfsId == 0:
                    int(jdata['album']['songs'][i]['mMusic']['lfsId'])
            song_dfsId = str(dfsId)
            print song_dfsId
            encrypted_song_id = encrypted_id(song_dfsId)
            url = "http://m1.music.126.net/" + encrypted_song_id + "/" + song_dfsId + ".mp3"
    print "收费歌曲url:"
    print url
    return url