import datetime
import time


def hard_function():
    time.sleep(1)


def main():
    number = 1
    start_time = datetime.datetime.now()
    for item in range(1, 6):
        number *= item
        print(f"Step: {item} - number is: ", number)
        hard_function()
    execution_time = str(datetime.datetime.now() - start_time)[5:10]
    print(f"Execution time of process is: {execution_time} seconds.")


if __name__ == "__main__":
    main()
