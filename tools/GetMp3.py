#!/usr/bin/env python
# coding=utf-8
# Author: Archer
# File: GetMp3.py
# Date: 08/Mar/2017
# Desc: 从sqlite数据库里面读取mp3链接，然后下载到本地
import unirest
import os
import sqlite3
from time import sleep
from random import randint

db_filename = '../data/netease.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print 'database not exists'
else:
    cursor = conn.cursor()
    cursor.execute("select * from songs")
    for row in cursor.fetchall()[1:]:
        sid = row[0]
        smp3Url = row[-1]
        resp = unirest.get(smp3Url)
        if resp.code == 200:
            print 'Succ:', sid, smp3Url
            with open('../data/songs/' + sid + '.mp3', 'w') as f:
                f.write(resp.body)
        else:
            print 'Error:', sid, smp3Url

        sleep(randint(0, 10)) # slowly request, for anti-crawl policy

conn.close()
