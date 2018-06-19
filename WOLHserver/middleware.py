#coding=utf-8
'''
Created on 2018年6月19日

@author: caoxiaocheng
'''
from django.conf import settings
from django.http import JsonResponse

class ValidateMiddleware(object):
    '''请求有效性验证'''
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if '/admin/' in request.path:
            return self.get_response(request)
        if request.path not in settings.API_DEFINATIONS:
            response = JsonResponse({'status': 'failed', 'code': -1, 'desc': 'unsupported endpoint %s' % request.path})
        else:
            api_defination = settings.API_DEFINATIONS[request.path]
            allowed_method = api_defination['allowed_method']
            method_name = request.method
            if method_name in allowed_method:
                response = self.get_response(request)
            else:
                response = JsonResponse({'status': 'failed', 'code': -2, 'desc': 'unsupported method %s' % method_name})
        return response