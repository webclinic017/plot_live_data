import time
import pandas as pd
import sys


def reset_data(data):
    zero_dict = dict()
    for i in range(10):
        zero_dict[data.columns[i]] = 0
    header = pd.DataFrame(zero_dict, index=[0])
    header.to_csv('data/generated.csv', header=True, index=False)


def generate_data(data):
    frequency = 50.0
    period = 1.0/frequency
    row = 0
    packet_size = 4
    start = time.time()
    last = 0
    while True:
        try:
            this = time.time() - start
            towrite = data.loc[list(range(row, row + packet_size))]
            row += packet_size
            towrite.to_csv('data/generated.csv', header=False, index=False, mode='a')
            sleep_length = last + period - (time.time() - start)
            time.sleep(sleep_length if sleep_length >= 0 else 0)
            last = this
        except KeyError:
            print('All data written into generated.csv')
            break


def main(reset=False):
    data = pd.read_csv('data/sample_data.csv')
    reset_data(data)
    if not reset:
        generate_data(data)


if __name__ == '__main__':
    param = False
    if len(sys.argv) > 1:
        if sys.argv[1].__eq__('True'):
            param = True
    main(reset=param)
