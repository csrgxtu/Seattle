#!/usr/bin/env python
# coding=utf-8
# AUthor: Archer
# File: SongInfoFromCsvToSqlite.py
# Date: 8/Mar/2017
# Desc: 将网上搜集来的data/neteaseutf8.csv导入数据库sqlite
import csv
import os
import sqlite3

csv_filename = '../data/neteaseutf8.csv'
db_filename = '../data/netease.db'
schema_filename = '../data/netease.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creating schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'Inserting initial data'
        f = open(csv_filename, 'rt')
        try:
            index = 1
            reader = csv.reader(f)
            for row in reader:
                sid = row[0]
                sname = row[1]
                ssinger = row[2]
                sneteaseUrl = row[3]
                smp3Url = row[4]

                sql = "insert into songs (id, sid, name, singer, neteaseUrl, mp3Url) values (" + str(index) + ", '" + sid.replace('\'', '\'\'') + "', '" + sname.replace('\'', '\'\'') + "', '" + ssinger.replace('\'', '\'\'') + "', '" + sneteaseUrl.replace('\'', '\'\'') + "', '" + smp3Url.replace('\'', '\'\'') + "')"
                # sql = "insert into songs (id, name, singer, neteaseUrl, mp3Url) values (?, ?, ?, ?, ?)"
                # conn.execute(sql, (sid, sname, ssinger, sneteaseUrl, smp3Url))
                # print sql
                conn.execute(sql)
                index = index + 1
                print sid
        finally:
            f.close()
        # with open(csv_filename, 'r') as f:
    else:
        print 'Database exists, assume schema does, too.'
