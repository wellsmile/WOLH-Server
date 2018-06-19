#coding=utf-8
'''
Created on 2017年11月29日

@author: caoxiaocheng
'''
def get_request_ip(request):
    '''获取用户请求的IP地址'''
    remote_ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if remote_ip:
        remote_ip = remote_ip.split(',')[0]
    else:
        remote_ip = request.META.get('REMOTE_ADDR', '')
    return remote_ip