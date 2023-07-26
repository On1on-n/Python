# coding=utf-8

'''
Author:On1on
Email:On1on_n@outlook.com

date:2023/7/26 13:11
'''


import orm
import asyncio
from models import User, Blog, Comment

async def sql(loop):
    await orm.create_pool(loop=loop, user='root', password='root', db='moe')
    u = User(name='Test', email='test@gmail.com', passwd='1234567890', image='about:blank')
    await u.save()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sql(loop))
    loop.close()