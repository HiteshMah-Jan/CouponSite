#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/12/18

__author__ = 'MiracleYoung'


from scrapy import cmdline

name = 'douban'
cmd = f'scrapy crawl {name}'
cmdline.execute(cmd.split())