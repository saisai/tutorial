import asyncio


async def nested():
    return 42


async def main():
    # schedule nestd() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # task can not be used cancel "nested()", or
    # can simple be awaited to wait unitl it is complete
    await task

asyncio.run(main())
