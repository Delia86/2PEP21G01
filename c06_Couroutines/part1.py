
import aiohttp
import json

import time
import asyncio

from datetime import datetime

async def time_getter(session,location='Bucharest'):
    response=await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/{location}')
    my_time = await response.text()

    return json.loads(my_time)


async def get_world_time():
   async with aiohttp.ClientSession() as session:
      start_time=time.time()
      task=await asyncio.gather(time_getter(session),time_getter(session,'Amsterdam'),)
      end_time=time.time()
      print(f'total time:{end_time-start_time}')
      print(task[0])

asyncio.run(get_world_time())

#
# async def get_time():
#     await asyncio.sleep(2)
#     print (f'finished time:{datetime.now()}')
#
# #print(type(get_time()))
#
# async def main():
#     start_time=time.time()
#     await asyncio.gather(get_time(),get_time(),get_time(),get_time())
#     end_time=time.time()
#     print(f'Execution time:{end_time-start_time}')
#
# if __name__ == '__main__':
#     asyncio.run(main())
#     # result=asyncio.gather(main(),main())
#     # print(type(result))
#     # await result
#
