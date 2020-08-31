import asyncio
import sys


async def get_date():
    code = 'import datetime; print(datetime.datetime.now())'

    # create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE
    )
    # read one line of output

    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()


    # wait for the subprocess exit.
    await proc.wait()
    return line

date = asyncio.run(get_date())
print(f'current data: {date}')

