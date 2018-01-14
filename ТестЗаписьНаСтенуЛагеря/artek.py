#!/usr/bin/python
# coding: utf-8

from libraryartek import FirstTest

brs = FirstTest()
if(brs):
    print "Статус:"
    print "Test success"
else:
    print "Статус:"
    print "Test error"

