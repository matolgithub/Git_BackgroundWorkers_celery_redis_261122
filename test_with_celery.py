import datetime
from tasks import hard_function
from celery.result import AsyncResult


def main():
    task_1 = hard_function.delay(1, 3)
    # print("-------------------------------------------")
    # print(task_1.status, task_1.id)
    # print("-------------------------------------------")
    # res_task_1 = AsyncResult(task_1, app=hard_function)
    # print("-------------------------------------------")
    # print(res_task_1.get(), res_task_1.status, res_task_1.state)
    # print("-------------------------------------------")
    task_2 = hard_function.delay(2, 3)
    task_3 = hard_function.delay(1, 4)
    task_4 = hard_function.delay(3, 3)
    task_5 = hard_function.delay(4, 6)
    print(task_1, task_2, task_3, task_4, task_5)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    print(datetime.datetime.now() - start_time)
