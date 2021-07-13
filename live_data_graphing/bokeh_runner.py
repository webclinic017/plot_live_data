import os
import subprocess

ports = [5006, 5007, 5008, 5009, 5010]


class Runner:

    def kill_process(self):
        for i in range(len(self.bokeh_serve)):
            self.bokeh_serve[i].terminate()
            # self.f[i].close()
        # subprocess.run('taskkill /F /IM bokeh.exe')
        kill_current_bokeh = subprocess.Popen('taskkill /F /IM bokeh.exe')
        kill_current_bokeh.terminate()
        print('Bokeh plot server(s) closed.')

    def __init__(self, num_plots):
        plot_dir_root = __file__.split(os.sep)[:-1]
        bokeh_plot_path = plot_dir_root + ['bokeh_plot.py']
        settings_dir_path = plot_dir_root + ['settings']
        data_dir_path = plot_dir_root + ['data']
        self.bokeh_serve = []
        for i in range(num_plots):
            command = ['bokeh', 'serve', '--show', f'\"{os.sep.join(bokeh_plot_path)}\"', '--port', str(ports[i]),
                       '--args']
            settings_file_path = settings_dir_path + [f'settings_{i}.json']
            command.append(f'\"{os.sep.join(settings_file_path)}\"')
            data_file_path = data_dir_path + [f'data_{i}.csv']
            command.append(f'\"{os.sep.join(data_file_path)}\"')
            self.bokeh_serve.append(subprocess.Popen(' '.join(command), shell=False, stdout=subprocess.DEVNULL))

# sample code:
#
# import time
#
# from live_data_graphing import bokeh_runner
#
#
# runner = \
#   bokeh_runner.Runner('C:\\Users\\Jimmy Li\\PycharmProjects\\plot_live_data\\live_data_graphing\\bokeh_plot.py')
# time.sleep(5)
# runner.kill_process()
