#coding=utf-8
from django.db import models

# Create your models here.
class Items(models.Model):
    '''所有道具'''
    ITEMSTYPE_CHOICES = (('arcane', '奥术'),
                         ('rune', '符文'),
                         ('curse', '诅咒'),
                         ('cloak', '斗篷'),
                         ('other', '其他'))
    
    id = models.AutoField(verbose_name="道具ID", primary_key=True)
    name = models.CharField(verbose_name='道具名', max_length=256, null=False, blank=False, db_index=True, unique=True, )
    descript = models.CharField(verbose_name='道具描述', max_length=256, null=True, blank=True, default='')
    type = models.CharField(verbose_name='道具类型', max_length=64, null=True, blank=True, db_index=True, choices=ITEMSTYPE_CHOICES)
    info = models.TextField(verbose_name='道具信息Json', null=True, blank=True, default='')
    
    class Meta:
        db_table = 'WOLH_items'
        verbose_name = "道具信息"
        verbose_name_plural = verbose_name
        
    def check_name(self, item_name):
        return True if item_name in self.name else False
    
    @classmethod
    def create_item(cls, item_name, **kwargs):
        item = Items()
        item.name = item_name
        item.descript = kwargs.get('descript', '')
        item.type = kwargs.get('type', 'other')
        item.info = kwargs.get('info', '')
        return item
    
class Operation(models.Model):
    '''操作记录'''
    
    id = models.AutoField(verbose_name="操作ID", primary_key=True)
    time = models.DateTimeField(verbose_name="操作时间", auto_now_add=True, db_index=True)
    user = models.CharField(verbose_name='操作用户', max_length=256, null=True, blank=True, default='')
    operation = models.CharField(verbose_name='操作类型', max_length=256, default='')
    info = models.TextField(verbose_name='操作信息Json', null=True, blank=True, default='')
    
    class Meta:
        db_table = 'WOLH_operations'
        verbose_name = "操作记录"
        verbose_name_plural = verbose_name