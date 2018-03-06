#-*-coding:utf-8 -*-

def set_saltgroup_abbr_name(sender,instance,**kwargs):
    if not instance.abbr_name:
        instance.abbr_name = instance.generate_abbr_name()
        instance.save()