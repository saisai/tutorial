import asyncio
import aiomysql


async def test_example():

    loop = asyncio.get_running_loop()

    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='root', db='mysql',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("SELECT Host, User FROM user")
        print(cur.description)
        r = await cur.fetchall()
        print(r)
        for a in r:
            print(a)
    conn.close()

asyncio.run(test_example())
