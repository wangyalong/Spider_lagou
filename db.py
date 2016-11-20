#!/usr/bin/env python
#coding=UTF-8
'''
    Created on 2014-03-08
    @author: devin
    @desc:
        数据访问
'''
import sys
import MySQLdb
#from slave import Connection
from MySQLdb.cursors import DictCursor
import datetime

# MySQL 连接信息
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'wangyalong'
MYSQL_PWD = 'wangyalong'
MYSQL_DB = 'wangyalong'


def GetConnection():
    conn = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PWD, \
                           db=MYSQL_DB, charset="utf8")
    return conn
    return Connection()

def Connect():
    conn = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PWD, \
            db=MYSQL_DB, charset="utf8")

    return conn

def ExecuteSQL(sql, args = None):
    '''
        执行SQL语句, 正常执行返回影响的行数，出错返回Flase
    '''
    ret = 0
    try:
        conn = GetConnection()
        cur = conn.cursor()

        ret = cur.execute(sql, args)
        conn.commit()
    except MySQLdb.Error, e:
        print e
        return False
    finally:
        cur.close()
        #conn.close()

    return ret

def ExecuteSQLs(sql, args = None):
    '''
        执行多条SQL语句, 正常执行返回影响的行数，出错返回Flase
    '''
    ret = 0
    try:
        conn = GetConnection()
        cur = conn.cursor()

        ret = cur.executemany(sql, args)
        conn.commit()
    except MySQLdb.Error, e:
        return False
    finally:
        cur.close()
    return ret


