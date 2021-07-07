import pandas as pd
import time

from numpy import linspace
from matplotlib import pyplot as plt


class GraphFigs:

    @staticmethod
    def my_extend(array, to_extend):
        array.extend(to_extend)
        if len(array) > 1000:
            return array[-1000:]
        else:
            return array

    def animate(self, last_frame, this_frame):
        # read csv file, skipping drawn rows
        data_raw = pd.read_csv(self.data_file, skiprows=range(1, self.drawn_rows))
        # check num_row of new data
        num_new_row = len(data_raw)
        # if there is any new rows, plot it
        if num_new_row > 0:
            # create time array for new data rows
            to_extend = linspace(last_frame, this_frame, num_new_row, endpoint=False)
            self.my_extend(self.t, to_extend)
            # add data to data arrays and update drawing
            for i in range(len(self.axes)):
                for j in range(3):
                    self.my_extend(self.data[i][j], data_raw[self.data_name[i][j]])
                    self.axes[i].lines[j].set_data(self.t, self.data[i][j])
                if not self.use_constant_y_lim:
                    all_data = pd.DataFrame(self.data[i])
                    self.axes[i].set_ylim(all_data.min().min() - 1, all_data.max().max() + 1)
        self.axes[0].set_xlim(last_frame - 4, last_frame + 1)

    def __init__(self, num_axes=3,
                 data_file='data/generated.csv',
                 data_name=None,
                 frequency=50,
                 data_sets_per_frame=4,
                 title=None,
                 x_label='x_label missing',
                 y_label=None,
                 use_constant_y_lim=True,
                 legend_loc='upper right',
                 style='fivethirtyeight'):
        plt.style.use(style)
        self.fig, (self.axes) = plt.subplots(nrows=num_axes, sharex='all', figsize=(15, 10))
        self.data_file = data_file
        self.data_name = data_name if data_name is not None else \
            [['Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)'],
             ['Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)'],
             ['Magnetometer X (G)', 'Magnetometer Y (G)', 'Magnetometer Z (G)']]
        self.frequency = frequency
        self.data_sets_per_frame = data_sets_per_frame
        # Number of data points needed to be plotted.
        self.num_data_sets_needed = 4 * frequency * data_sets_per_frame
        self.title = title if not None else ['Angular acceleration', 'Acceleration', 'Magnetic field']
        self.ylabel = y_label if not None else ['Gyroscope (deg/s)', 'Accelerometer (g)', 'Magnetometer (G)']
        # Initial x limits are from -4 to 1 second(s)
        # 	- Figure will be animated so that old data move left.
        # 	- 4/5 of the screen will be old data up to current time
        # 	- 1/5 of the screen will be empty.
        self.axes[0].set_xlim(-4, 1)
        # Plot three empty lines to start.
        self.t = [0]
        self.data = []
        for i in range(num_axes):
            self.data.append([[0], [0], [0]])
            self.axes[i].plot(self.t, self.data[i][0], label='X', c='r')
            self.axes[i].plot(self.t, self.data[i][1], label='Y', c='g')
            self.axes[i].plot(self.t, self.data[i][2], label='Z', c='b')
            # Figure labels
            self.axes[i].set_title(title[i])
            self.axes[i].set_xlabel(x_label)
            self.axes[i].set_ylabel(y_label[i])
            self.axes[i].legend(loc=legend_loc)
            self.axes[i].set_ylim(-10, 10)
        self.use_constant_y_lim = use_constant_y_lim
        self.start_time = time.time()
        self.last_frame = 0
        self.this_frame = 0
        # lines of data that is already drawn.
        self.drawn_rows = 1
        # Animation command.
        # 	- The animation needs to be stored so it is not deleted by garbage collection.
        # self.ani = FuncAnimation(self.fig, self.animate, interval=0)
        plt.tight_layout()

    # def pause_ani(self):
    #     self.ani.pause()
    #
    # def resume_ani(self):
    #     self.ani.resume()


def main():
    graph = GraphFigs(3, 'data/generated.csv',
                      [['Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)'],
                       ['Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)'],
                       ['Magnetometer X (G)', 'Magnetometer Y (G)', 'Magnetometer Z (G)']],
                      data_sets_per_frame=4,
                      title=['Angular acceleration', 'Acceleration', 'Magnetic field'],
                      x_label='Time (s)',
                      y_label=['Gyroscope (deg/s)', 'Accelerometer (g)', 'Magnetometer (G)'],
                      use_constant_y_lim=False
                      )
    start_time = time.time()
    last_frame = 0
    while True:
        this_frame = time.time() - start_time
        graph.animate(last_frame, this_frame)
        plt.pause(0.001)
        last_frame = this_frame
        if len(plt.get_fignums()) == 0:
            break
    plt.show()


if __name__ == '__main__':
    main()

"""
graph_class arguments:

num_axes = number of plots that is going to be plotted in this figure.
data_file = path_to_file of file that contains data to be plotted
data_name = column name of data columns (should be in 2D list of num_axes*3 elements)
frequency = frame rate per second, or update frequency (Hz) (default = 50)
data_sets_per_frame = number of sets of data that is updated each frame (default = 4)
title = graph title (default = 'title missing')
xlabel =x label ('xlabel missing')
ylabel = y label (default = 'ylabel missing')
use_constant_ylim = whether y limit is fixed (default = True)
legend_loc = legend location on each plot (default = 'upper right')
style = matplotlib.pyplot.style that is used (default = 'fivethirtyeight')

"""
