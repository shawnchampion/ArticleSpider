# -*- coding: utf-8 -*-

from zheye import zheye
z = zheye()
positions = z.Recognize('realcap/a.gif')
print(positions)