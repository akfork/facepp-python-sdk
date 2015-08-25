#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: detection_landmark_demo.py

# This demo show you how to use Face++ API:/detection/landmark.
# 本示例展示如何使用/detection/landmark接口

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

# Here is the url to the person's face image
# 人脸部图片url

IMAGE_URL = 'http://cn.faceplusplus.com/static/resources/python_demo/1.jpg'

# Detect face in the picture and find out his position and attributes
# 检测出输入图片中的Face, 找出图片中Face的位置及属性

face = api.detection.detect(url=IMAGE_URL)

face_id = face['face'][0]['face_id']

land_mark = api.detection.landmark(api_key=API_KEY, api_secret=API_SECRET, face_id=face_id, type='25p')
print_result("sample person's face information:", land_mark)
