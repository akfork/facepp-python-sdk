#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: detection_detect_demo1.py

# This demo show you how to use Face++ API:/detection/detect.
# 本示例展示如何使用/detection/detect接口

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
            return dict([(encode(k), encode(v)) for (k,v) in obj.iteritems()])
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

# Here is the url to the person's face image
# 人脸部图片url

IMAGE_URL = 'http://www.faceplusplus.com.cn//static/resources/python_demo/1.jpg'

# Detect face in the picture and find out his position and attributes
# 检测出输入图片中的Face, 找出图片中Face的位置及属性

# face = api.detection.detect(url=IMAGE_URL)
face = api.detection.detect(img=facepp.File('1.jpg'),
                            attribute="gender,age,race,smiling,glass,pose",
                            tag='This is 1.jpg',
                            async='true')

print_result("sample person's face information:", face)
# res = api.info.get_session(session_id='f72f5f9cf66543449471880a6ce82696')
# print_result("sample person's face information:", res)
