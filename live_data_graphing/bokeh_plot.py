import pandas as pd
import json

from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
from bokeh.layouts import column
from bokeh.themes import built_in_themes


##############################################
with open('/live_data_graphing/default_settings.json') as f:
    settings = json.load(f)
    
frame_update_frequency_limit = settings['frame_update_frequency_limit']
frame_period_ms = 1000//frame_update_frequency_limit
num_data_set_limit = settings['num_data_set_limit']

plot_width = settings['plot_width']
plot_height = settings['plot_height']
index_header = settings['index_header']  # also x label
col_headers = settings['col_headers']
plot_titles = settings['plot_titles']
plot_y_labels = settings['plot_y_labels']
line_labels = settings['line_labels']
line_colors = settings['line_colors']
plot_y_lims = settings['plot_y_lims']

data_file_path = settings['data_file_path']
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
                            y_axis_label=plot_y_labels[i],
                            y_range=plot_y_lims[i]))
        for j in range(3):
            plots[i].line(index_header,
                          col_headers[i][j],
                          line_color=line_colors[j],
                          legend_label=line_labels[j],
                          source=source)

    doc = curdoc()
    # doc.theme = Theme('theme.json')  # custom theme
    doc.theme = built_in_themes['dark_minimal']  # built in themes
    # 'caliber', 'dark_minimal', 'light_minimal', 'night_sky', 'contrast'
    doc.add_root(column(plots, sizing_mode='stretch_both'))
    doc.add_periodic_callback(update, frame_period_ms)


main()
