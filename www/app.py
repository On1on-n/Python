# coding=utf-8

'''
Author:On1on
Email:On1on_n@outlook.com

date:2023/7/24 13:42
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio
import os
import jaon
import time

from datetime import datetime
from aiohttp import web

# def index():
#     return web.Response(body=b'<h1>Awesome<h1>')

# @asyncio.coroutine
# def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET','/',index)
#     srv = yield  from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()


# 路由装饰器写法

# 路由装饰器
routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    return web.Response(body=b'<h1>Awesome<h1>',content_type='text/html')

async def init():
    app = web.Application()
    app.add_routes(routes)
    return app

web.run_app(init(),host='127.0.0.1',port=9000)