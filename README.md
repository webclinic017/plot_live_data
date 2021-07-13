# plot_live_data

plot_live_data is a project aimed to create a script which can create plots where the data is being drawn live.

## Requirements

* Python 3.8
  * This project was developed with Python 3.8.10
  * Whether or not other versions of Python can run this project was not tested.
* All python packeges in requirements.txt
  * pip is automatically installed with Python (since Python 3.4)
  * run this command to install all packages ```pip install -r requirements.txt```
  

## Usage

* The script is designed to read newly written data from a .csv file.
* The script has variables that change the resulting plots.
* Currently, the script is written to plot three line plots with three lines each.
* The data used is a sample data measured from an x-IMU that has 9DOF, 
and a script is written to mimic data being written into a .csv file in real time.
    * To see the example effects, run ``` python tester.py ```