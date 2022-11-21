from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
import sys
import time
import json
import os

def repondre(id, liste, connect, mr):
    print(f"On test la lecture de fichier et le passage d'infos\n{id}\n{liste}\n{connect}\n")

    if mr == 1:
        reponse = {'reponse' : {
                'type' : 0,
                'id_discussion' : 0,
                'nom_client' : "",
                'total' : 0
                } 
              }
    else :
        reponse = {'reponse' : {
                'type' : 0,
                'id_discussion' : 0,
                'nom_client' : "",
                'liste_entreprises' : []
                } 
              }

    cursor = connect.cursor()


    
    if mr == 1:
        cursor.execute("""SELECT SUM(prix) AS total FROM Factures inner join Entreprises on Entreprises.num = Factures.numEntreprise WHERE Entreprises.siren=(%s)""",(liste[6][2],))

        rep = cursor.fetchall()

        reponse['reponse']['type'] = 1
        reponse['reponse']['id_discussion'] = liste[6][0]
        reponse['reponse']['nom_client'] = liste[6][1]
        for i in rep:
            reponse['reponse']['total'] += float(i[0])

    else :
        cursor.execute("""SELECT siren AS liste FROM Entreprises inner join Factures on Factures.numEntreprise = Entreprises.num inner join Commandes on Commandes.num = Factures.numCommande inner join Produits on Produits.numCommande = Factures.numCommande WHERE Produits.produit=(%s)""",(liste[7][2],))

        rep = cursor.fetchall()

        reponse['reponse']['type'] = 1
        reponse['reponse']['id_discussion'] = liste[7][0]
        reponse['reponse']['nom_client'] = liste[7][1]

        for i in rep:
            reponse['reponse']['liste_entreprises'].append(i[0])


    jsReponse = json.dumps(reponse, indent=3)

    if (os.getcwd() == os.path.dirname(os.path.abspath(__file__))):
        path = os.path.dirname(os.path.abspath(__file__))+"/simulation_reseau/responses"

    else :
        path = os.getcwd()+"/simulation_reseau/responses"

    with open(path+"/requete"+str(id)+".json","w+") as outputFile:
        outputFile.write(jsReponse)







    

def lectureMessage(f, l, c):

    # Lists for stocking info of responses
    lt1 = []
    lt2 = []

    with open(f, 'r') as file:
        data = json.load(file)

        #Checking type of the message
        messageType = data['requete']['type']
        discussionID = data['requete']['id_discussion']

        # We received a request of total price from a company
        if (messageType == 1):

            if len(lt1) <= 3:
                lt1.append(messageType)
                lt1.append(data['requete']['nom_client'])
                lt1.append(data['requete']['num_siren'])

            else :
                lt1[0] = messageType    
                lt1[1] = data['requete']['nom_client']
                lt1[2] = data['requete']['num_siren']

            # First message
            if len(l) <= 6:
                if len(l) < 2:
                    for i in range(1,6):
                        l.append("placeholder")
                l.append(lt1)


            # Already parsed some messages
            else :
                l[6] = lt1



        # We received a request of list of company you have paid delivery
        elif (messageType == 2):

            if len(lt2) <= 3:
                lt2.append(messageType)
                lt2.append(data['requete']['nom_client'])
                lt2.append(data['requete']['produit'])
            else :
                lt2[0] = messageType
                lt2[1] = data['requete']['nom_client']
                lt2[2] = data['requete']['produit']

            # First message
            if len(l) <= 6:
                if len(l) < 2:
                    for i in range(1,7):
                        l.append("placeholder")
                l.append(lt2)


            # Already parsed some messages
            else :
                if len(l) == 6:
                    l.append(lt2)
                else:
                    l[7] = lt2



    repondre(discussionID, l, c, messageType)



class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self, liste, connection):
        event_handler = Handler(liste, connection)
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)

        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

    
class Handler(PatternMatchingEventHandler):
    def __init__(self, l, c):
        self.liste = l
        self.connection = c
        super(Handler, self).__init__(
            patterns=["*.json"],
            ignore_patterns=["*.tmp","*.*~","#*.*",".*.*"],
            ignore_directories=True,
            case_sensitive=False,
    )


    def on_any_event(self, event):
        if event.event_type == "created":
            lectureMessage(event.src_path, self.liste, self.connection)