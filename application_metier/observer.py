import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from resultats import *


class Watcher:
    DIRECTORY_TO_WATCH = "../simulation_reseau/responses"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = EventHandler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()

        time.sleep(20)
        self.observer.stop()

        self.observer.join()


class EventHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            print("Creation of : ", event.src_path)
            readJson(event.src_path)


def awaitingResponse():
    w = Watcher()
    w.run()
