# plot_live_data

plot_live_data is a project aimed to create a script which can create plots where the data is being drawn live.

## Usage

- The script is designed to read newly written data from a .csv file.

- The script has variables that change the resulting plots.

- Currently, the script is written to plot three line plots with three lines each.

- The data used is a sample data measured from an x-IMU that has 9DOF, 
and a script is written to mimic data being written into a .csv file in real time.

- To see the example effects:
1. run data/live_data_generator.py with line 37 commented out (generate_data(data))
```
...

def main():
    data = pd.read_csv('sample_data.csv')
    reset_data(data)
    # generate_data(data)

...
```

2. run the plotting script first. (a browser window with empty plots should pop up)
```
cd [path_to_project]\plot_live_data\live_data_graphing
bokeh serve --show bokeh_plot.py
```

3. run data/live_data_generator.py with line 37 not commented out.
```
...

def main():
    data = pd.read_csv('sample_data.csv')
    reset_data(data)
    generate_data(data)

...
```

