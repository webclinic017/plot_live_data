# plot_live_data

plot_live_data is a project aimed to create a script which can create plots where the data is being drawn live.

## Usage

* The script is designed to read newly written data from a .csv file.

* The script has variables that change the resulting plots.

* Currently, the script is written to plot three line plots with three lines each.

* The data used is a sample data measured from an x-IMU that has 9DOF, 
and a script is written to mimic data being written into a .csv file in real time.

    * To see the example effects, one could use the command prompt:
        * run data/live_data_generator.py with 'True' as first argument to reset generated.csv
            ```
            cd [path_to_project]\plot_live_data\live_data_graphing\data
            python live_data_generator.py True
            ```
    
        * run the plotting script first. (a browser window with empty plots should pop up)
            ```
            cd [path_to_project]\plot_live_data\live_data_graphing
            bokeh serve --show bokeh_plot.py
            ```

        * run data/live_data_generator.py no arguments to start mock data generation
            ```
            cd [path_to_project]\plot_live_data\live_data_graphing\data
            python live_data_generator.py
            ```
    * Or simply run the scripts through an IDE or python interpreter.
        * A runner helper class has been created to run bokeh server with a python script.
            * Sample code is in bokeh_runner.py on the bottom and commented out.