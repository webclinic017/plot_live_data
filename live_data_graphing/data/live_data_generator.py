import time
import pandas as pd


def reset_data(data):
    header = pd.DataFrame(columns=data.columns)
    header.to_csv('generated.csv', header=True, index=False)


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
            towrite.to_csv('generated.csv', header=False, index=False, mode='a')
            sleep_length = last + period - (time.time() - start)
            time.sleep(sleep_length if sleep_length >= 0 else 0)
            last = this
        except KeyError:
            print('All data written into generated.csv')
            break


def main():
    data = pd.read_csv('sample_data.csv')
    reset_data(data)
    generate_data(data)


if __name__ == '__main__':
    main()
