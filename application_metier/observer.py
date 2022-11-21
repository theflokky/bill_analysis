from tkinter import *
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
import threading

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

        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class EventHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        global currentFilePath
        if event.event_type == 'created':
            if(event.src_path < currentFilePath and currentFilePath != ""):
                print("modif on repertory")
            else :
                print("Modification of : ", event.src_path)
                currentFilePath = event.src_path
        elif event.event_type == 'modified':
            if(event.src_path < currentFilePath and currentFilePath != ""):
                print("modif on repertory")
            else :
                print("Modification of : ", event.src_path)
                currentFilePath = event.src_path


def awaitingResponse():

    w = Watcher()
    #w.run()
    obs = threading.Thread(target=lambda : w.run(), daemon=True)
    obs.start()

def readJson():
    global currentFilePath
    with open(currentFilePath, 'r') as file:
        data = json.load(file)
        total = []
        # We try the type of the message
        messageType = data['reponse']['type']
        discussionID = data['reponse']['id_discussion']
        clientName = data['reponse']['nom_client']
        if (messageType == 2):
            enterpriseList = data['reponse']['liste_entreprises']
            file.close()
            os.remove(currentFilePath)
            return enterpriseList
            print(enterpriseList)
        elif (messageType == 1):
            total.append(data['reponse']['total'])
            file.close()
            os.remove(currentFilePath)
            return total
            print(total)
        else:
            print("Error")
            exit(0)