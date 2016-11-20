#!/usr/bin/env python
#coding=utf-8

import db       

def Insert_lagou(args):
    sql = "INSERT INTO lg (city, positionName, district, companyName, salary, formatCreateTime ) VALUES (%s, %s, %s, %s, %s, %s)"
    return db.ExecuteSQLs(sql,args)

