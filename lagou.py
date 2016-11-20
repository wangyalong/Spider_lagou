#usr/bin/env python
#coding=UTF-8
import  time
from lagouParser import lagou_task_parser
from insert_db import Insert_lagou
class lagouParser():
    def __init__(self):
        pass

    def parse(self, task):
        
        result = lagou_task_parser(task)
        Insert_lagou(result)
    '''
    可以在这里加扩展

    '''


if __name__ == "__main__":



    '''
    
    可提供任意关键字的搜索

    没有 加 try异常处理

    这个Parser 已经满足需求了

    '''
    
    Parser = lagouParser()
    task = '爬虫'
    result = Parser.parse(task)
    
