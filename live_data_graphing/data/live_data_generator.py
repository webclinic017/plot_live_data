import time
import pandas as pd


def reset_data(data):
    header = pd.DataFrame(columns=data.columns)
    header.to_csv('generated.csv', header=True, index=False)


def generate_data(data):
    frequency = 1000.0
    row = 0
    packet_size = 4
    start_time = time.time()
    while True:
        try:
            towrite = data.loc[list(range(row, row + packet_size))]
            row += packet_size
            towrite.to_csv('generated.csv', header=False, index=False, mode='a')
            time.sleep((1.0 / frequency) - ((time.time() - start_time) % (1.0 / frequency)))
        except:
            break


def main():
    data = pd.read_csv('sample_data.csv')
    reset_data(data)
    # generate_data(data)


if __name__ == '__main__':
    main()
