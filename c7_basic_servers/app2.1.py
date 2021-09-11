import asyncio
import aiohttp
import time


async def phonebook_getter(session):
    response = await session.request(method='GET', url='http://localhost:8080/')
    my_phonebook = await response.text()
    return my_phonebook


async def phonebook_getter2():
    async with aiohttp.ClientSession() as session:
        task = await asyncio.gather(phonebook_getter(session), phonebook_add(session, {'key2': 2}),
                                    phonebook_remove(session, 'key1'))
        print(task)


async def phonebook_add(session: aiohttp.ClientSession, entries: dict):
    respose = await session.post(url='http://localhost:8080/add', data='message')
    my_phonebook = await respose.text()
    time.sleep(2)
    return my_phonebook


async def phonebook_remove(session: aiohttp.ClientSession, name):
    response = await session.delete(url='http://localhost:8080/remove', data={'entries': [name]})
    my_phonebook = await response.text()
    return my_phonebook


asyncio.run(phonebook_getter2())
