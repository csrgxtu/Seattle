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
from socket import *

db_filename = '../data/netease.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print 'database not exists'
else:
    cursor = conn.cursor()
    cursor.execute("select * from songs where flag = 'default'")
    for row in cursor.fetchall()[1:]:
        rid = row[0]
        sid = row[1]
        smp3Url = row[-2]
        # print rid, sid, smp3Url
        try:
            resp = unirest.get(smp3Url)
            if resp.code == 200:
                print 'Succ:', rid, sid, smp3Url
                cursor.execute("update songs set flag = 'processed' where id = " + str(rid))
                with open('../data/songs/' + sid + '.mp3', 'w') as f:
                    f.write(resp.body)
            else:
                print 'Error:', rid, sid, smp3Url
                cursor.execute("update songs set flag = 'dead' where id = " + str(rid))
        except:
            print 'Error:', rid, sid, smp3Url
            cursor.execute("update songs set flag = 'dead' where id = " + str(rid))

        conn.commit()
        sleep(randint(0, 10)) # slowly request, for anti-crawl policy

conn.close()
