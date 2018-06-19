#coding=utf-8
import json

from django.http.response import JsonResponse
from .models import Items
from json.decoder import JSONDecodeError

from utils.ip_getter import get_request_ip
from utils.operation_recroder import OperationRecroder

def items_data(request):
    '''道具信息'''
    method_name = request.method
    request_ip = get_request_ip(request)
    operation_recroder = OperationRecroder(operation_type=method_name, info={'ip':request_ip})
    # 获取道具信息，模糊查询
    if method_name == 'GET':
        item_name = request.GET.get('item_name', '').strip()
        items_result = Items.objects.using('default').filter(name__contains = item_name)
        result_list = [{'item_name': item.name, 'item_descript': item.descript} for item in items_result]
        operation_recroder.info['item_name'] = item_name
        return_response = JsonResponse({'status': 'success', 'code': 0, 'results':result_list})
    # 新增道具信息，道具名必填    
    elif method_name == 'POST':
        prams_dict = request.POST.dict()
        operation_recroder.info['item_name'] = item_name = prams_dict.get('item_name', None).strip()
        operation_recroder.info['item_descript'] = item_descript = prams_dict.get('item_descript', None)
        operation_recroder.info['item_type'] = item_type = prams_dict.get('item_type', None)
        operation_recroder.info['item_info'] = item_info = prams_dict.get('item_info', None)
        if not item_name:
            return JsonResponse({'status': 'failed', 'code': -3, 'desc': 'itme name %s is invalid' % item_name})
        # 如果已有此道具，改为更新道具信息
        items_result = Items.objects.using('default').filter(name = item_name)
        if len(items_result) != 0:
            item_obj = items_result[0]
            item_obj.descript = item_descript
            item_obj.type = item_type
            item_obj.info = item_info
        else:
            item_obj = Items.create_item(item_name, descript=item_descript, type=item_type, info=item_info)
        item_obj.save()
        return_response = JsonResponse({'status': 'success', 'code': 0, 'results': 'item info has been saved'})
    # 删除道具信息，道具名必填，未测试    
    elif method_name == 'DELETE':
        try:
            params_dict = json.loads(request.body)
        except JSONDecodeError:
            return JsonResponse({'status': 'failed', 'code': -4, 'desc': 'request body %s is not Json format' % request.body})
        item_name = params_dict.get('item_name', None).strip()
        if not item_name:
            return JsonResponse({'status': 'failed', 'code': -5, 'desc': 'itme name %s is invalid' % item_name})
        items_result = Items.objects.using('default').filter(name = item_name)
        items_result[0].delete()
        operation_recroder.info['item_name'] = item_name
        return_response = JsonResponse({'status': 'success', 'code': 0, 'results': 'item %s has been deleted' % item_name})
    # 记录操作记录并返回    
    operation_recroder.recrod()
    return return_response