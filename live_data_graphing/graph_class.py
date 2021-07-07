import pandas as pd

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class GraphFigs:

    def fetch_data(self, i):
        try:
            return pd.read_csv(self.data_file, skiprows=list(range(1, i - self.num_data_sets_needed)),
                               nrows=self.num_data_sets_needed)
        except:
            return pd.read_csv(self.data_file)

    def update_axes(self, ax, t, x, y, z):
        # Update data that draws the lines
        x_line, y_line, z_line = ax.lines
        x_line.set_data(t, x)
        y_line.set_data(t, y)
        z_line.set_data(t, z)
        if self.use_constant_y_lim:
            # Fixed y limits
            # 	- data won't be stretched during updates
            # 	- data may exceed limit or leave too much white space
            ax.set_ylim(-5, 5)
        else:
            # Variable y limits
            # 	- data will stay within figure
            # 	- data stretching may cause confusion
            all_data = pd.DataFrame([x, y, z])
            y_max = all_data.max().max()
            y_min = all_data.min().min()
            ax.set_ylim(y_min - 1, y_max + 1)

    def animate(self, frame):
        i = frame
        t = range(i - self.num_data_sets_needed, i * self.data_sets_per_frame)
        if i < self.num_data_sets_needed:
            data = pd.read_csv(self.data_file, nrows=i * self.data_sets_per_frame)
            t = range(0, i * self.data_sets_per_frame)
        else:
            data = self.fetch_data(i)
        t = [float(x / (self.frequency * self.data_sets_per_frame)) for x in t]

        for i, data_col in enumerate(self.data_name):
            x = data[data_col[0]]
            y = data[data_col[1]]
            z = data[data_col[2]]
            self.update_axes(self.axes[i], t, x, y, z)
            self.axes[i].set_ylim(-1, 1)

        # Increase x limits by the amount of time that passed since the last frame
        # 	- Time passed is calculated by 1 second / frequency
        x_lim_low, x_lim_high = self.axes[0].get_xlim()
        self.axes[0].set_xlim(x_lim_low + (1 / self.frequency), x_lim_high + (1 / self.frequency))

    def __init__(self, num_axes, data_file, data_name,
                 frequency=50,
                 data_sets_per_frame=4,
                 title='Title Missing',
                 xlabel='xlabel missing',
                 ylabel='ylabel missing',
                 use_constant_y_lim=True,
                 legend_loc='upper right',
                 style='fivethirtyeight'):
        plt.style.use(style)
        self.fig, (self.axes) = plt.subplots(nrows=num_axes, sharex=True, figsize=(10, 10))
        self.data_file = data_file
        self.data_name = data_name
        self.frequency = frequency
        self.data_sets_per_frame = data_sets_per_frame
        # Number of data points needed to be plotted.
        self.num_data_sets_needed = 4 * frequency * data_sets_per_frame
        # Initial x limits are from -4 to 1 second(s)
        # 	- Figure will be animated so that old data move left.
        # 	- 4/5 of the screen will be old data up to current time
        # 	- 1/5 of the screen will be empty.
        self.axes[0].set_xlim(-4, 1)
        # Plot three empty lines to start.
        for i in range(num_axes):
            self.axes[i].plot([0], [0], label='X', c='r')
            self.axes[i].plot([0], [0], label='Y', c='g')
            self.axes[i].plot([0], [0], label='Z', c='b')
            # Figure labels
            self.axes[i].set_title(title[i])
            self.axes[i].set_xlabel(xlabel)
            self.axes[i].set_ylabel(ylabel[i])
            self.axes[i].legend(loc=legend_loc)
        self.use_constant_y_lim = use_constant_y_lim
        # Animation command.
        # 	- The animation needs to be stored so it is not deleted by garbage collection.
        self.ani = FuncAnimation(self.fig, self.animate, interval=0)
        # Show figure.
        # 	- set block=True in order to prevent the script from continuing.
        plt.tight_layout()
        plt.show(block=False)

    @staticmethod
    def show(block=True):
        plt.show(block=block)