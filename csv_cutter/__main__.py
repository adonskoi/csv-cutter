import configparser 
import csv
import logging

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

config = configparser.ConfigParser()
config.read("settings.ini") 
DELIMITER = config["in"]["delimiter"]
ENCODINGS=config["in"]["encodings"].split(", ")
ENCODING_OUT=config["out"]["encoding"]


def cut_csv(file_path):
    for encode in ENCODINGS:
        lines = 10
        if not isinstance(file_path, str):
            file_path = file_path.decode("utf-8")
        logging.info(f"start {file_path} with {encode}")
        new_path = ".".join((f"{file_path.split('.')[0]}_10_lines", "csv"))
        try:
            with open(file_path, "r", newline="",  encoding=encode) as f:
                with open(new_path, "w", encoding=ENCODING_OUT) as f_write:
                    writer = csv.writer(f_write, delimiter=DELIMITER)
                    reader = csv.reader(f, delimiter=DELIMITER)
                    header = next(reader)
                    n = 0
                    writer.writerow(header)
                    for row in reader:
                        writer.writerow(row)
                        n += 1
                        if n > lines:
                            logging.info(f"finish {file_path} with {encode}")
                            return
        except UnicodeDecodeError as e: 
            logging.error(f"failed {file_path} with {encode}, {e}")


class MainWidget(Widget):

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)


class CSVCutter(App):

    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return MainWidget()

    def _on_file_drop(self, window, file_path):
        cut_csv(file_path)
            

if __name__ == '__main__':
    CSVCutter().run()