#!/usr/bin/env python
# encoding: utf-8
# @Time    : 11/6/18

__author__ = 'MiracleYoung'


class BaseConfig:
    pass


class DevConfig(BaseConfig):
    pass


config = {
    'dev': DevConfig,
}
