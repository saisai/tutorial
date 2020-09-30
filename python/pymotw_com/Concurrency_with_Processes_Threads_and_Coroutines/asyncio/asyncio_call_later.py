import asyncio

def callback(n):
    print('callback {} invoked'.format(n))


async def main():
    print('registering callbacks')
    loop = asyncio.get_running_loop()

    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)


asyncio.run(main())
