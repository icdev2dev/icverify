
import random
import asyncio
from flask import Flask

def getrandint():
    return str(random.randint(0,10))

async def getrandfloat():
    await asyncio.sleep(2)
    return str(random.random())


LIST_SVC_FUNCTIONS = [
    ("/getrandint", "getrandint", getrandint, ['GET', 'POST'] ),
    ("/getrandfloat", "getrandfloat", getrandfloat, ['GET', 'POST'] ),
    ]

def register_be_funcs(app:Flask):

    for (rule, endpoint, view_func, methods) in LIST_SVC_FUNCTIONS:
        app.add_url_rule (rule=rule, endpoint=endpoint, view_func=view_func, methods = methods )
    