import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # get a "work item" out of the queue.
        sleep_for = await queue.get()

        # sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # nofity the queu that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')

async def main():
    # create a queue that we will use to store our "workload".
    queue = asyncio.Queue()


    # generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # wait until the queue is full processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at


    # cancel our worker tasks.
    for task in tasks:
        task.cancel()

    # wait unitl all worker tasks are cancelled
    await asyncio.gather(*tasks, return_exceptions=True)


    print("====")
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

asyncio.run(main())
