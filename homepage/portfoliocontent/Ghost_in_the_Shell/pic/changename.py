#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re


for root, dirs, files in os.walk("."):
    for name in files:
        print(os.path.join(root, name))
        if  re.search("猎豹截图", name)
            print "get"
    for name in dirs:
        print(os.path.join(root, name))