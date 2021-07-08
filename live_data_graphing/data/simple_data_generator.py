import random
import pandas as pd
import time

names = ['Packet number',
         'Gyroscope X (deg/s)',
         'Gyroscope Y (deg/s)',
         'Gyroscope Z (deg/s)',
         'Accelerometer X (g)',
         'Accelerometer Y (g)',
         'Accelerometer Z (g)',
         'Magnetometer X (G)',
         'Magnetometer Y (G)',
         'Magnetometer Z (G)']


def reset_data():
    df = pd.DataFrame(data=[], columns=names[1:])
    df.to_csv('generated_simple.csv', index_label=names[0])


def generate():
    frequency = 50.0  # number of times data is generated per second
    data_count = 4  # number of data sets (rows) generated each time
    period = 1.0 / frequency  # time in seconds between each data generation
    count = 10000  # number of times total data is generated each run. Total rows generated is count*data_count
    index = 0
    start = time.time()  # start time of this script
    last = 0  # time passed since start to last data generation
    for i in range(count):  # data generation loop
        this = time.time() - start  # time of start of current loop
        new_data = dict()
        new_data[names[0]] = list(range(index, index + data_count))
        index += data_count
        for j in range(len(names) - 1):
            new_data[names[j + 1]] = []
            for _ in range(data_count):
                new_data[names[j + 1]].append(random.random())
        pd.DataFrame.from_dict(new_data, 'columns') \
            .to_csv('generated_simple.csv', index=False, header=False, mode='a')
        sleep_time = last + period - (time.time() - start)
        time.sleep(sleep_time if sleep_time >= 0 else 0)
        last = this


def main():
    reset_data()
    generate()


if __name__ == '__main__':
    main()
