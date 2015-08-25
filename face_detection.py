#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# face detection use face++ SDK

API_KEY = '9089b21713f33492bc84584449d0f8a4'
API_SECRET = 'vBEvvSdshCbdt3IiMKIem6NwxQ1NCHTv'

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

from facepp import API, File

api = API(API_KEY, API_SECRET)

face = api.detection.detect(img = File('ugly.png'))

# print("type(result) = %s" % type(result))

# print("face = %s" % repr(face))

print_result("sample person's face information:", face)




