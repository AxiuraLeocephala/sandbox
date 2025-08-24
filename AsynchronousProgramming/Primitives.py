import asyncio
import time

'''
Synchronization primitives (синхроизирующие примитивы) - используются
для синхронизации задач. НЕ ЯВЛЯЮТСЯ ПОТОКО БЕЗОПАСНЫМИ, использовать
модуль threading
'''

async def func_1(prim):
    async with prim: 
        print(f"Start executing func_1 at {time.strftime("%X")}")
        await asyncio.sleep(4)
        await prim.wait()
        print(f"Finish executing func_1 at {time.strftime("%X")}")

async def func_2(prim):
        print(f"Start executing func_2 at {time.strftime("%X")}")
        await asyncio.sleep(5)
        await prim.wait()
        print(f"Finish executing func_2 at {time.strftime("%X")}")

async def func_3(prim):
        print(f"Start executing func_3 at {time.strftime("%X")}")
        await asyncio.sleep(6)
        print(f"Finish executing func_3 at {time.strftime("%X")}")

async def main():
    print(f"Start executing main at {time.strftime("%X")}")

    # Приостанавливает выполнение задач, предоставляя экслюзивный доступ
    # к ресурсам одной задаче. Имеет два способа применения:
    # 1. async with lock: ... - предпочтительных способ
    # 2. await lock.acquire()
    #    try:
    #        ...
    #    finally:
    #        lock.release()  
    lock = asyncio.Lock()

    # Приостанавливает выполнение задач до тех пор, пока флаг, event,
    # не изменит свое значение на true, изначально имеет значение false.
    # (method) set() - изменяет значение флага на true;
    # (method) clear() - изменяет значение флага на false;
    # (method) await event.wait() - отслеживает изменение флага с false 
    # на true
    event = asyncio.Event()

    # Сочетает особенности работы Lock и Event. Приостаналивает выполнение
    # задач до тех пор, пока флаг, не изменит свое значение на true, чтобы
    # одна задача получила экслюзивный доступ к ресурсам.
    # Способы использования такие же, как и у Lock
    condition = asyncio.Condition()

    async with asyncio.TaskGroup() as group:
        task_1 = group.create_task(func_1(condition))
        task_2 = group.create_task(func_2(condition))
        task_3 = group.create_task(func_3(condition))

    print(f"Finish executing main at {time.strftime("%X")}")

asyncio.run(main())