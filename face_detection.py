#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# face detection use face++ SDK

API_KEY = '9089b21713f33492bc84584449d0f8a4'
API_SECRET = 'vBEvvSdshCbdt3IiMKIem6NwxQ1NCHTv'

from facepp import API, File

api = API(API_KEY, API_SECRET)

result = api.detection.detect(img = File('ugly.png'))

# print("type(result) = %s" % type(result))

print("result = %s" % repr(result))
