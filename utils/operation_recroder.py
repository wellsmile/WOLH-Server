#coding=utf-8
'''
Created on 2018年6月19日

@author: caoxiaocheng
'''
import json

from items_manage.models import Operation

class OperationRecroder(object):
    def __init__(self, **kwargs):
        self.operation_type = kwargs.get('operation_type', None)
        self.user_name = kwargs.get('user_name', None)
        self.info = kwargs.get('info', {})
    
    def recrod(self):
        operation_obj = Operation()
        operation_obj.operation = self.operation_type
        operation_obj.user = self.user_name
        operation_obj.info = json.dumps(self.info, ensure_ascii=False)
        operation_obj.save()