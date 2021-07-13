import pandas as pd
import json
import sys
import os

from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
from bokeh.layouts import column
from bokeh.themes import Theme

##############################################
try:
    if not os.path.isfile(sys.argv[1]):
        raise (FileNotFoundError('{} file not found'.format(sys.argv[1])))
    data_file_path = sys.argv[2]
    with open(sys.argv[1]) as f:
        settings = json.load(f)
except FileNotFoundError as e:
    print(e)
    raise
except IndexError as e:
    print('Missing argument for path to settings.json')
    raise
except Exception as e:
    print("Unexpected error:", e)
    raise

try:
    frame_update_frequency_limit = settings['frame_update_frequency_limit']
    frame_period_ms = 1000 // frame_update_frequency_limit
    num_data_set_limit = settings['num_data_set_limit']

    plot_width = settings['plot_width']
    plot_height = settings['plot_height']
    index_header = settings['index_header']  # also x label
    col_headers = settings['col_headers']
    plot_titles = settings['plot_titles']
    plot_y_labels = settings['plot_y_labels']
    line_labels = settings['line_labels']
    line_colors = settings['line_colors']
    plot_y_lims_temp = settings['plot_y_lims']
    plot_y_lims = []
    for lims in plot_y_lims_temp:
        plot_y_lims.append((lims[0], lims[1]))

    plotted = 1
    source = ColumnDataSource(pd.read_csv(data_file_path, index_col=index_header))
except KeyError as e:
    print('Missing settings from settings.json')
    raise
except FileNotFoundError as e:
    print(f'{data_file_path} does not exist.')
    raise
except Exception as e:
    print('Unexpected error', e)
    raise

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
        plots[i].grid.visible = False
        for j in range(3):
            plots[i].line(index_header,
                          col_headers[i][j],
                          line_color=line_colors[j],
                          legend_label=line_labels[j],
                          source=source)
    doc = curdoc()
    # doc.theme = Theme('theme.json')  # custom theme
    doc.theme = 'dark_minimal'  # built in themes
    # 'caliber', 'dark_minimal', 'light_minimal', 'night_sky', 'contrast'
    doc.add_root(column(plots, sizing_mode='stretch_both'))
    doc.add_periodic_callback(update, frame_period_ms)


main()
