#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: train_search_demo.py

# This demo shows you how to use Face++ API:/train/identify.
# 本示例展示如何使用/train/identify接口

# You need to register your App first, and enter you API key/secret.
# 您需要先注册一个App, 并将得到的API key和API secret写在这里.

API_KEY = '9089b21713f33492bc84584449d0f8a4'
API_SECRET = 'vBEvvSdshCbdt3IiMKIem6NwxQ1NCHTv'

# Import system libraries and define helper functions
# 导入系统库并定义辅助函数

import time
from pprint import pformat


def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return dict([(encode(k), encode(v)) for (k, v) in obj.iteritems()])
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj

    print hint
    result = encode(result)
    print('\n'.join([' ' + i for i in pformat(result, width=75).split('\n')]))


# First import the API class from the SDK
# 首先, 导入SDK中的API类

import facepp

api = facepp.API(API_KEY, API_SECRET)

face1 = api.detection.detect(api_key=API_KEY, api_secret=API_SECRET, img=facepp.File('1.jpg'), tag='1.jpg')

face2 = api.detection.detect(api_key=API_KEY, api_secret=API_SECRET, img=facepp.File('2.jpg'), tag='2.jpg')

person1 = api.person.create(api_key=API_KEY, api_secret=API_SECRET, face_id=face1['face'][0]['face_id'])

person2 = api.person.create(api_key=API_KEY, api_secret=API_SECRET, face_id=face2['face'][0]['face_id'])

group = api.group.create(api_key=API_KEY, api_secret=API_SECRET,
                         person_id=person1['person_id'] + ',' + person2['person_id'])

print_result("Group info:", group)

res = api.train.identify(api_key=API_KEY, api_secret=API_SECRET, group_name=group['group_name'])

time.sleep(5)

res2 = api.info.get_session(api_key=API_KEY, api_secret=API_SECRET, session_id = res['session_id'])

print_result("Train res:", res2)