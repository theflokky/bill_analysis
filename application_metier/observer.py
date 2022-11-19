from tkinter import *
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json

currentFilePath = ""

class Watcher:
    DIRECTORY_TO_WATCH = "simulation_reseau/responses"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = EventHandler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()

        time.sleep(10)
        self.observer.stop()

        self.observer.join()


class EventHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        global currentFilePath
        if event.event_type == 'created':
            print("Creation of : ", event.src_path)
            currentFilePath = event.src_path


def awaitingResponse():
    w = Watcher()
    w.run()

def readJson():
    global currentFilePath
    with open(currentFilePath, 'r') as file:
        data = json.load(file)
        total = []
        # We try the type of the message
        messageType = data['reponse']['type']
        discussionID = data['reponse']['id_discussion']
        clientName = data['reponse']['nom_client']
        if (messageType == 1):
            enterpriseList = data['reponse']['liste_entreprises']
            file.close()
            os.remove(currentFilePath)
            return enterpriseList
            print(enterpriseList)
        elif (messageType == 2):
            total.append(data['reponse']['total'])
            file.close()
            os.remove(currentFilePath)
            return total
            print(total)
        else:
            print("Error")
            exit(0)