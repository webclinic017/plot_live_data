import subprocess


class Runner:

    def kill_process(self):
        self.bokeh_serve.terminate()
        kill_current_bokeh = subprocess.Popen('taskkill /F /IM bokeh.exe')
        kill_current_bokeh.terminate()
        print('Bokeh plot server closed.')

    def __init__(self, bokeh_plot_path):
        # 'C:\\Users\\Jimmy Li\\PycharmProjects\\plot_live_data\\live_data_graphing\\bokeh_plot.py'
        command = f'bokeh serve --show \"{bokeh_plot_path}\"'
        self.bokeh_serve = subprocess.Popen(command, shell=False)

#
# sample code
# import time
#
# from live_data_graphing import bokeh_runner
#
#
# runner = \
#   bokeh_runner.Runner('C:\\Users\\Jimmy Li\\PycharmProjects\\plot_live_data\\live_data_graphing\\bokeh_plot.py')
# time.sleep(5)
# runner.kill_process()
