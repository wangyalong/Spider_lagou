#!usr/bin/env  python
#coding=UTF-8


import requests
import json
import sys
import urllib
from insert_db import Insert_lagou
import httplib


hd =  {
       "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }
def lagou_task_parser(Task):
    
    httplib.HTTPConnection.debuglevel=1
    
    result = []
    session = requests.Session()

    post_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    post_data = 'first=true&pn={0}&kd='+ urllib.quote(Task)
    
    page  = requests.post(post_url, data = post_data.format(1), headers = hd).content
    data = json.loads(page)
    totalCount = data['content']['positionResult']['totalCount']
    resultsize = data['content']['positionResult']['resultSize']
    print totalCount
    pageNum = totalCount / resultsize + (totalCount % resultsize != 0)

    for i in range(pageNum):
        
        page  = requests.post(post_url, data = post_data.format(i+1), headers = hd).content
        result += parse_lagou(page)
   
    print len(result)
    return result

def parse_lagou(page):
   
    result = []
    data = json.loads(page)
    companyNum = data['content']['positionResult']['result']
    print len(companyNum)

    for res in companyNum:
        
        city = res['city']
        positionName = res.get('positionName', 'NULL')
        district = res.get('district', 'NULL')
        companyName = res.get('companyFullName', 'NULL')
        salary = res.get('salary', 'NULL')
        formatCreateTime = res.get('createTime', 'NULL')
        res_tuple = ( city,positionName,district,companyName,salary,formatCreateTime)
        result.append(res_tuple)

    return result

if __name__ == '__main__':
    lg_task_parser('爬虫')
