import asyncio
import time
from typing import Set, Coroutine
from random import randrange, randint

async def func_1() -> int:
    '''
    Корутина/сопрограмма/асинхронная функция - функция, объявленная с помощью 
    async/await синтаксиса. Является ожидаемым объектом
    '''
    
    time_start = time.strftime('%X')
    print(f"start execute func_1 in {time_start}")
    await asyncio.sleep(1)
    time_finish = time.strftime('%X')
    print(f"finish execute func_1 in {time_finish}")
    return 1

async def func_2() -> int:
    time_start = time.strftime('%X')
    print(f"start execute func_2 in {time_start}")
    await asyncio.sleep(1)
    time_finish = time.strftime('%X')
    print(f"finish execute func_2 in {time_finish}")
    return 1


'''
(funcion) run - запускает корутину, ожидает ее завершение и возвращает 
результат или исключение. Блокирует поток, поэтому нельзя вызвать 
несколько функций 
'''
# result = asyncio.run(main())
# print(result)

'''
(runner context maneger) with asyncio.Runner() - запускает корутину/
несколького корутин в одном контексте. Каждая корутина выполняется 
последовательно 
'''
# with asyncio.Runner() as runner:
#     result_func_1 = runner.run(func_1())
#     result_func_2 = runner.run(func_2())
#     print(result_func_1, result_func_2)

async def say_after(delay: float, what: str) -> int:
    print(f"started say '{what}' at {time.strftime('%X')}")
    await asyncio.sleep(delay)
    print(what)
    print(f"finished say '{what}' af {time.strftime('%X')}")
    return 1

async def main_for_func_say_after_tasks() -> None:
    '''
    (function) create_task - создает задачу, запуская корутину. Если
    создать несколько задач и ожидать их завершения, как в примере ниже,
    они будут выполняться паралельно. Задачи являются ожидаемыми объектами
    '''
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    result1 = await task1
    result2 = await task2
    print(result1, result2)

async def main_for_func_say_after_task_group() -> None:    
    '''
    (Class) TaskGroup - аналог тому, что написано в функции выше, но 
    более лаконичный, компактный и современный вариант запуска корутин
    паралельно друг другу
    '''
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(1, 'hello'))
        task2 = tg.create_task(say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    print(f"finished at {time.strftime('%X')}")
    print(task1.result, task2.result)


'''
Future - "представляет возможный результат ассинхронной операции" - хз,
что это. Является ожидаемым объектом
'''

async def main_creation_tasks():
    '''
    Создается надежная ссылка на задачу, чтобы сборщик мусора не удалил
    ее до того, как она завершится. Также, каждая задача имеет колбек - 
    так обеспечивается удаление задачи из множества, когда она 
    завершается - «вызвал и забыл»
    '''
    background_tasks: Set[Coroutine] = set()

    async with asyncio.TaskGroup() as tg:
        for i in range(10):
            task = tg.create_task(say_after(randrange(1, 5), f"{i}"))

            background_tasks.add(task)

            task.add_done_callback(background_tasks.discard)

async def main_cancel_tasks():
    '''
    Создается надежная ссылка на задачу, чтобы сборщик мусора не удалил
    ее до того, как она завершится. Также, каждая задача имеет колбек - 
    так обеспечивается удаление задачи из множества, когда она 
    завершается - «вызвал и забыл»
    '''
    background_tasks: Set[Coroutine] = set()

    async with asyncio.TaskGroup() as tg:
        for i in range(10):
            task = tg.create_task(say_after(randrange(1, 5), f"{i}"))

            background_tasks.add(task)

            task.add_done_callback(background_tasks.discard)

            result = randint(0, 1)
            print(result)
            if result == 1:
                was_cancelled = task.cancel()
                print(f"canceled: {was_cancelled}")

class TerminateTaskGroup(BaseException):
    '''Исключение для того, чтобы завершить группу задач'''

async def force_terminate_task_group():
    raise TerminateTaskGroup

async def main_cancel_task_group():
    '''
    asyncio не поддерживает завершение группы задач, поэтому используется 
    «костыль»
    '''
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(say_after(randrange(2, 5), "0"))
            tg.create_task(say_after(randrange(2, 5), "1"))

            await asyncio.sleep(1)

            tg.create_task(force_terminate_task_group())
    except* TerminateTaskGroup:
        print('task group has been terminated')

asyncio.run(main_cancel_task_group())