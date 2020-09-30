import asyncio
import aiomysql

async def main():
    loop = asyncio.get_running_loop()
    conn = await aiomysql.connect(host='127.0.0.1',
                                  port=3306,
                                  user='root',
                                  password='root',
                                  db="sms",
                                  autocommit=False,
                                  loop=loop)

    async with conn.cursor() as cursor:
        stmt_drop = "DROP TABLE IF EXISTS names"
        await cursor.execute(stmt_drop)
        await cursor.execute("""
            CREATE TABLE names (
                id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
                name VARCHAR(30) DEFAULT '' NOT NULL,
                cnt TINYINT UNSIGNED DEFAULT 0,
                PRIMARY KEY (id))""")
        await conn.commit()


        # Insert 3 records
        names = (('Geert',), ('Jan',), ('Michel',))
        stmt_insert = "INSERT INTO names (name) VALUES (%s)"
        await cursor.executemany(stmt_insert, names)

        # ROLL back
        await conn.rollback()


        # there should be no data
        stmt_select = "SELECT id, name FROM names ORDER BY id"
        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        # Check there is not data
        assert not resp

        # dot the insert again.
        await cursor.executemany(stmt_insert, names)


        # data should be already there
        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        print(resp)
        # do a commit
        await conn.commit()


        await cursor.execute(stmt_select)
        print(resp)

        # cleaning up, dropping the table again
        await cursor.execute(stmt_drop)
        await cursor.close()

        conn.close()

asyncio.run(main())
