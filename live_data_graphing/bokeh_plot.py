import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
from bokeh.layouts import column
# from bokeh.themes import Theme, built_in_themes

##############################################
frame_update_frequency_limit = 1000
frame_period_ms = 1000//frame_update_frequency_limit
num_data_set_limit = 600

plot_width = 1500
plot_height = 210
index_header = 'Packet number'  # also x label
col_headers = [['Gyroscope X (deg/s)',
                'Gyroscope Y (deg/s)',
                'Gyroscope Z (deg/s)', ],
               ['Accelerometer X (g)',
                'Accelerometer Y (g)',
                'Accelerometer Z (g)', ],
               ['Magnetometer X (G)',
                'Magnetometer Y (G)',
                'Magnetometer Z (G)'], ]
plot_titles = ['Gyroscope', 'Accelerometer', 'Magnetometer']
plot_y_labels = ['Angle Acceleration', 'Acceleration', 'Magnetic Field']
line_labels = ['x', 'y', 'z']
line_colors = ['red', 'green', 'blue']

data_file_path = 'data/generated.csv'
plotted = 1
source = ColumnDataSource(pd.read_csv(data_file_path, index_col=index_header))
##############################################


def update():
    global plotted
    data = pd.read_csv(data_file_path, index_col=index_header, skiprows=range(1, plotted))
    source.stream(data, rollover=num_data_set_limit)
    plotted += len(data)


def main():
    plots = []
    for i in range(len(col_headers)):
        plots.append(figure(plot_width=plot_width,
                            plot_height=plot_height,
                            title=plot_titles[i],
                            x_axis_label=index_header,
                            y_axis_label=plot_y_labels[i]))
        for j in range(3):
            plots[i].line(index_header,
                          col_headers[i][j],
                          line_color=line_colors[j],
                          legend_label=line_labels[j],
                          source=source)

    doc = curdoc()
    # doc.theme = Theme('theme.json')
    # doc.theme = 'dark_minimal'
    # 'caliber', 'dark_minimal', 'light_minimal', 'night_sky', 'contrast'
    column_to_add = column(plots, sizing_mode='stretch_both')
    doc.add_root(column_to_add)
    doc.add_periodic_callback(update, frame_period_ms)

main()
