import random
import pandas as pd
from bokeh.driving import count
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

fps = 100
ro = 100
data = pd.read_csv('data/generated.csv')

source = ColumnDataSource(data)


@count()
def update(x):
    y = random.random()
    source.stream({'x': [x], 'y': [y]}, rollover=ro)


plot = figure()
plot.line('x', 'y', source=source)
plot.xaxis.axis_label = 'x'
plot.yaxis.axis_label = 'y'

doc = curdoc()
doc.add_root(plot)
doc.add_periodic_callback(update, fps)
