import asyncio
import aiomysql

async def main():

    loop = asyncio.get_running_loop()

    conn = await aiomysql.connect(host='127.0.0.1',
                                  port=3306,
                                  user='root',
                                  password='root',
                                  db='sms',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("DROP PROCEDURE IF EXISTS myinc;")
        await cur.execute("""CREATE PROCEDURE myinc(p1 INT)
                            BEGIN
                                SELECT p1 + 1;
                            END""")
        await cur.callproc('myinc', [1])
        (ret, ) = await cur.fetchone()
        assert 2, ret
        print(ret)
    conn.close()


asyncio.run(main())
