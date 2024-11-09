import multiprocessing
from time import time


def read_info(name):
    all_data = []
    with (open (name, 'r')) as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


"""
линейный вывод:
"""
# start_time = time()
# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# for i in filenames:
#     data = read_info(i)
# end_time = time()
# print(end_time - start_time)

"""
многопроцессорный вывод:
"""
if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_start = time()

    with multiprocessing.Pool() as pool:
        data = pool.map(read_info, filenames)
    time_end = time()
    total_time = time_end - time_start
    print(total_time)
