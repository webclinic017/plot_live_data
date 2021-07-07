import pandas as pd

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

class Graph_figs:

	def update_axes(self, graph_ax, t, x, y, z):
		graph_ax.update_axes(t, x, y, z)

	def fetch_data(self, i):
		try:
			return pd.read_csv(self.data_file, skiprows=list(range(1,i-self.num_data_sets_needed)), nrows=self.num_data_sets_needed)
		except:
			return pd.read_csv(self.data_file)
	
	def animate(self, frame):
		i = frame
		t = range(i-self.num_data_sets_needed, i*self.data_sets_per_frame)
		if i < self.num_data_sets_needed:
			data = pd.read_csv(self.data_file, nrows=i*self.data_sets_per_frame)
			t = range(0, i*self.data_sets_per_frame)
		else:
			data = self.fetch_data(i)
		t = [float(x/(self.frequency*self.data_sets_per_frame)) for x in t]
		
		for i, data_col in enumerate(self.data_name):
			x = data[data_col[0]]
			y = data[data_col[1]]
			z = data[data_col[2]]
			self.update_axes(self.axes[i], t, x, y, z)

		# Increase x limits by the amount of time that passed since the last frame
		#	- Time passed is calculated by 1 second / frequency
		xlim_low, xlim_high = self.axes[0].get_xlim()
		self.axes[0].set_xlim(xlim_low + (1/self.frequency), xlim_high + (1/self.frequency))

	def __init__(self, num_axes, data_file, data_name, 
		frequency=50,
		data_sets_per_frame=4,
		title='Title Missing',
		xlabel='xlabel missing',
		ylabel='ylabel missing',
		use_constant_ylim=True,
		legend_loc='upper right',
		style='fivethirtyeight'):
		plt.style.use(style)
		self.fig, (self.axes) = plt.subplots(nrows=num_axes, sharex=True, figsize=(10, 10))
		self.data_file = data_file
		self.data_name = data_name
		self.frequency = frequency
		self.data_sets_per_frame = data_sets_per_frame
		# Number of data points needed to be plotted.
		self.num_data_sets_needed = 4*frequency*data_sets_per_frame
		# Initial x limits are from -4 to 1 second(s)
		#	- Figure will be animated so that old data move left.
		#	- 4/5 of the screen will be old data up to current time
		#	- 1/5 of the screen will be empty.
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
		self.use_constant_ylim = use_constant_ylim
		# Animation command.
		#	- The animation needs to be stored so it is not deleted by garbage collection.
		self.ani = FuncAnimation(self.fig, self.animate, interval=0)
		# Show figure.
		#	- set block=True in order to prevent the script from continuing.
		plt.tight_layout()
		plt.show(block=False)

	@staticmethod
	def show(block=True):
		plt.show(block=block)

	def update_axes(self, ax, t, x, y, z):
		# Update data that draws the lines
		x_line, y_line, z_line = ax.lines
		x_line.set_data(t, x)
		y_line.set_data(t, y)
		z_line.set_data(t, z)
		if self.use_constant_ylim:
			# Fixed y limits 
			#	- data won't be streached during updates
			#	- data may exceed limit or leave too much white space
			ax.set_ylim(-5, 5)
		else:
			# Variable y limits
			#	- data will stay within figure
			#	- data streaching may cause confusion
			# y_max_list = []
			# y_max_list.append(x.max())
			# y_max_list.append(y.max())
			# y_max_list.append(z.max())
			# y_max = pd.Series(y_max_list).max()
			all_data = pd.DataFrame([x,y,z])
			y_max = all_data.max().max()
			y_min = all_data.min().min()

			# y_min_list = []
			# y_min_list.append(x.min())
			# y_min_list.append(y.min())
			# y_min_list.append(z.min())
			# y_min = pd.Series(y_min_list).min()
			
			try:
				ax.set_ylim(y_min-1, y_max+1)
			except:
				ax.set_ylim(-1,1)

"""
	def add_graph_axes(self, data_name, 
		title='Title Missing',
		xlabel='xlabel missing',
		ylabel='ylabel missing',
		use_constant_ylim=True,
		legend_loc='upper right'):
		self.data_name.append(data_name)
		self.fig.add_axes(sharex=True, label=title)
		ax = plt.gca()
		self.axes.append(ax)
		self.use_constant_ylim = use_constant_ylim
		# Plot three empty lines to start.
		ax.plot([0], [0], label='X', c='r')
		ax.plot([0], [0], label='Y', c='g')
		ax.plot([0], [0], label='Z', c='b')
		# Figure labels
		ax.set_title(title)
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel)
		temp.legend(loc=legend_loc)
"""