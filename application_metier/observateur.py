from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
import sys
import time
import json


def lectureMessage(f, l):
    with open(f, 'r') as file:
        data = json.load(file)

        #Checking type of the message
        messageType = data['reponse']['type']

        # We received a request
        if (messageType == 1):

            # First message
            if len(l) <= 6:
                print(l)


class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self, liste):
        event_handler = Handler(liste)
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)
                print(liste)

        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

    
class Handler(PatternMatchingEventHandler):
    def __init__(self, l):
        self.liste = l
        super(Handler, self).__init__(
            patterns=["*.json"],
            ignore_patterns=["*.tmp","*.*~","#*.*",".*.*"],
            ignore_directories=True,
            case_sensitive=False,
    )


    def on_any_event(self, event):
        if event.event_type == "created":
            lectureMessage(event.src_path, self.liste)