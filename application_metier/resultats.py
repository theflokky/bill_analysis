import json


def readJson(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)

        # We try the type of the message
        messageType = data['reponse']['type']
        discussionID = data['reponse']['id_discussion']
        clientName = data['reponse']['nom_client']
        if (messageType == 1):
            enterpriseList = data['reponse']['liste_entreprises']
            print(enterpriseList)
        elif (messageType == 2):
            total = data['reponse']['total']
            print(total)
        else:
            print("Error")
            exit(0)
