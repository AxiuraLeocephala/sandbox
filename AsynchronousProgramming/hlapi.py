import asyncio
import contextvars
import time
from functools import partial
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
несколько функций run в одном потоке 
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
    '''.
    Благодаря множеству следующий код имеет более надежные гарантии 
    безопасности, чем gather, при планировании вложенных задач: если 
    задача (или подзадача, запланированная задачей) вызывает исключение, 
    TaskGroup отменяет оставшиеся запланированные задачи, в то время как 
    gather этого не делает 
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
    «костыль»: задача, которая поднимает исключение
    '''
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(say_after(randrange(2, 5), "0"))
            tg.create_task(say_after(randrange(2, 5), "1"))

            await asyncio.sleep(1)

            tg.create_task(force_terminate_task_group())
    except* TerminateTaskGroup:
        print('task group has been terminated')

async def factorial(name: str, number: int) -> int:
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main_for_factorial():
    '''
    Также как и TaskGroup выполняет задачи паралельно, но если одна из 
    задач вызовет исключение, это не приведет к отмене других задач.
    Возвращает список с результатами выполнения задач, в том числе с 
    ошибками
    '''
    
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

    print(L)

async def my_coroutine() -> None:
    print("Executing my_coroutine")

def on_done_task(task: asyncio.Task, context: contextvars.Context) -> None:
    print(f"task {task.get_name()} is finished")
    
    key_backgroud_task: contextvars.ContextVar = None
    for k in context.keys():
        if k.name == "background_tasks":
            key_backgroud_task = k
            break
    backgroung_tasks = context.get(key_backgroud_task)

    backgroung_tasks.discard(task)

    print(f"tasks in process {[task.get_name() for task in backgroung_tasks]}")

async def main_for_eager_task_factory():
    '''
    (function) eager_task_factory - используется для синхронного 
    выполнения корутин. Если корутина блокирует поток - она 
    запускается в цикле событий.  
    '''

    backgroud_tasks: Set = set()
    backgroud_tasks_var: contextvars.ContextVar = contextvars.ContextVar('background_tasks')
    backgroud_tasks_var.set(backgroud_tasks)

    loop = asyncio.get_event_loop()
    loop.set_task_factory(asyncio.eager_task_factory)

    for i in range(3):
        task = loop.create_task(my_coroutine(), name=f"{i}")
        backgroud_tasks.add(task)
        task.add_done_callback(partial(on_done_task, context=contextvars.copy_context()))

async def long_running_task() -> None:
    print('task started')
    await asyncio.sleep(11)
    print('task finished')

async def main_fo_long_running_task() -> None:
    '''
    (context maneger) async with asyncio.timeout(delay) - запускает задачу,
    с заданным ограничением во времени. Если достигнуто время ожидания 
    выполнения задачи - она отменяется и вызывается исключение TimeoutError 
    Все таймауты:
        timeout (when) - отменяет задачи, если превышено время ожидания, 
        согласно часам обработки событий
        
        timeout_at (when) - отменяет задачи, если превышено абсолютное время 
        ожидания

        wait_for(timeout) - отменяет задачу, если достугнут timeout, и 
        возвращает исключение TimeoutError
    '''
    try:
        async with asyncio.timeout(10):
            await long_running_task()
    except TimeoutError:
        print("the waiting time for the task has been exceeded")

async def main_for_wait() -> None:
    '''
    (function) wait - запускает задачи параллельно и возвращает их 
    результат, когда:
    1. истекает таймаут. Задачи, которые были выполнены в срок, будут
    находиться в переменной done, задачи, которые не были выполнены 
    в срок, - в переменной pending. Исключение TimeoutError не вызывается
    2. Выполнены или отменены все задачи (return_when="ALL_COMPLETED"). Задачи будут находиться в done
    3. Выполнена или отменена любая задача (return_when="FIRST_COMPLETED")
    4. Создано исключение какой-либо задачей (return_when="FIRST_EXCEPTION")

    Все ожидающие примитивы:
        wait - запускает задачи параллельно и возвращает реультаты, когда ...

        as_complete - удобен в использовании в асинхронном итераторе. 
        Запускает задачи параллельно и возвращает результат по мере их 
        завершения (см. документацию с примером использования)
    '''

    task1 = asyncio.create_task(say_after(1, "0"))
    task2 = asyncio.create_task(say_after(5, "1"))

    done, pending = await asyncio.wait([task1, task2], timeout=4, return_when="ALL_COMPLETED")
    
    print(done, pending)

def blocking_io(*args, **kwargs) -> None: # io - input-output
    print(f"start blocking at {time.strftime('%X')}")
    time.sleep(1)
    print(args, kwargs)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main_for_thread():
    '''
    (function) to_thread - запускает функцию асинхронно в отдельном потоке,
    возвращает корутину, которую можно дождаться, чтобы получить 
    окончательный результат
    '''

    print(f"started main at {time.strftime('%X')}")
    await asyncio.gather(
        asyncio.to_thread(blocking_io, 1, 2, name="name"),
        asyncio.sleep(1)
    )
    print(f"finished main at {time.strftime('%X')}")

asyncio.run(main_for_thread())