import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball_number in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f'Силач {name} поднял {ball_number} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Mike", 3))
    task2 = asyncio.create_task(start_strongman('John', 4))
    task3 = asyncio.create_task(start_strongman('Alex', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

