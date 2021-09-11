
import aiohttp
import json

import time
import asyncio

from datetime import datetime


async def time_getter(session,location='Bucharest',nr=0):
    response=await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/{location}')
    my_time = await response.text()

    return json.loads(my_time)

async def time_zone_getter(session):
    response=await session.request(method='GET',url='http://worldtimeapi.org/api/timezone')
    my_time_zones=await response.text()
    my_time_zones=json.loads(my_time_zones)
    result=filter(lambda x:x,map(lambda zone: zone.rsplit('/',maxsplit=1)[-1] if 'Europe' in zone else None ,my_time_zones))

    #print(list(result))

    return list(result)



async def get_world_time():
   async with aiohttp.ClientSession() as session:
      start_time=time.time()
      task0= await asyncio.gather(time_zone_getter(session))
      zones=task0[0]
      task1=await asyncio.gather(*(time_getter(session,location)for location in zones))
      end_time=time.time()
      print(type(task1))
      print(f'total time:{end_time-start_time}')
      print('Time zones are:',zones)
      print('Times are:',*task1,sep='\n')

if __name__=='__main__':
    asyncio.run(get_world_time())

