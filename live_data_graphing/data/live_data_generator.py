import time
import pandas as pd


def main():
    frequency = 1000.0
    data = pd.read_csv('sample_data.csv')
    row = 0
    packet_size = 4  # number of rows written each time (4 to mimic 200Hz gathering transmitted over 50Hz BLE)
    header = pd.DataFrame(columns=data.columns)
    header.to_csv('generated.csv', header=True, index=False)
    start_time = time.time()
    while True:
        try:
            towrite = data.loc[list(range(row, row + packet_size))]
            row += packet_size
            towrite.to_csv('generated.csv', header=False, index=False, mode='a')
            time.sleep((1.0 / frequency) - ((time.time() - start_time) % (1.0 / frequency)))
        except:
            break


if __name__ == '__main__':
    main()
