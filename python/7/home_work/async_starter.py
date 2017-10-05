import asyncio
import random
import time
flag = 0
# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.
async def countdown(number, n):  
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        await asyncio.sleep(random.random())
        n -= 1
    global flag
    flag += 1

async def pick_and_say():
    
    while True:
        if flag == 2:
            break
        print("--------say--------")
        await asyncio.sleep(2)
        

loop = asyncio.get_event_loop()  
tasks = [
    asyncio.ensure_future(pick_and_say()),  
    asyncio.ensure_future(countdown("A", 12)),
    asyncio.ensure_future(countdown("B", 12))]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()  