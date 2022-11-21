from tkinter import *
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json

REQUEST_PATH = "./simulation_reseau/requests/requete.json"

def generateJson2(clienNameInput,productNameInput):
      global REQUEST_PATH
      f=open(REQUEST_PATH,"w")
      tmp = []
      d = {
       "requete" : {
        "type" : 1,
        "id_discussion" : 1,
        "nom_client" : "Tiplouf",
        "nom_produit" : "masterball"
       }}
      d["requete"]["type"] = 2
      d["requete"]["nom_client"] = clienNameInput
      d["requete"]["nom_produit"] = productNameInput
      
      tmp.append(d)
      json.dump(d,f, indent=3)
      f.close();
      with open(REQUEST_PATH, 'r') as j:
       contents = json.loads(j.read())
       print(contents)
      f.close();
      
def generateJson(clienName, sirenNum):
      global REQUEST_PATH
      f=open(REQUEST_PATH,"w")
     
      d ={
       "requete" : {
        "type" : 1,
        "id_discussion" : 1,
        "nom_client" : "Tiplouf",
        "num_siren" : "123456789"
       }}
      
      d["requete"]["nom_client"] = clienName
     
      d["requete"]["num_siren"] = sirenNum
      
      json.dump(d,f, indent=3)
      f.close();
      with open(REQUEST_PATH, 'r') as j:
       contents = json.loads(j.read())
       print(contents)
   
      f.close();
