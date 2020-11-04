import asyncio

async def mesure1():
    print("Begin1")
    await asyncio.sleep(2)
    print("End1")

async def mesure2():
    print("Begin2")
    await asyncio.sleep(1)
    print("End2")

async def main_sync():
    await mesure1()
    await mesure2()

async def main_async():
    task1 = asyncio.create_task(mesure1())
    task2 = asyncio.create_task(mesure2())
    await task1
    await task2

asyncio.run(main_async())

