import asyncio


async def nested():
    return 42

async def main():
    # nothing happens if we just call "nested()"..
    #  a couroutine object is created but not awaited,
    # so it #won't run at all*.
    nested()

    # let's do it differently now and await it:
    print(await nested()) # will print "42"


asyncio.run(main())
