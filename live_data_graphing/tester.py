import data.live_data_generator

from pynput import keyboard
from live_data_graphing import bokeh_runner


def on_press(key):
    if key == keyboard.Key.esc:
        runner.kill_process()
        return False


if __name__ == '__main__':
    data.live_data_generator.main(reset=True)
    runner = bokeh_runner.Runner('bokeh_plot.py')
    data.live_data_generator.main()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
