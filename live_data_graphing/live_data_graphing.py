import graph_class


def main():
    graph = graph_class.GraphFigs(3, 'data/sample_data.csv',
                                  [['Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)'],
                                    ['Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)'],
                                    ['Magnetometer X (G)', 'Magnetometer Y (G)', 'Magnetometer Z (G)']],
                                  data_sets_per_frame=4,
                                  title=['Angular acceleration', 'Acceleration', 'Magnetic field'],
                                  xlabel='Time (s)',
                                  ylabel=['Gyroscope (deg/s)', 'Accelerometer (g)', 'Magnetometer (G)'],
                                  use_constant_y_lim=False
                                  )
    graph.show()


if __name__ == '__main__':
    main()

"""
When creating a graph_class object, an graph is created automatically with pyplot.subplots()
When more graphs on the same figure is needed, use graph_class.add_graph_axes()

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
