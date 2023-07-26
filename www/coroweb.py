# coding=utf-8

'''
Author:On1on
Email:On1on_n@outlook.com

date:2023/7/26 14:47
'''
__author__ = 'On1on'

import asyncio
import os
import inspect
import logging
import functools

from urllib import parse
from aiohttp import web

# apis是处理分页的模块，后面会编写，可以从github先下载到www下，以防止报错