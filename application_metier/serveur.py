import mysql.connector
import sys
import os
import time
import json
from facture import fact
from serveurInterface import show







if __name__ == "__main__" :

    # Creating tables if needed :
    tables={}

    tables['Clients'] = ("CREATE TABLE IF NOT EXISTS Clients ("
                        "    num int NOT NULL AUTO_INCREMENT,"
                        "    nom varchar(200),"
                        "    adresse varchar(100),"
                        "    PRIMARY KEY(num),"
                        "    UNIQUE(nom)"
                        ")"
    )

    tables['Entreprises'] = ("CREATE TABLE IF NOT EXISTS Entreprises ("
                             "   num int NOT NULL AUTO_INCREMENT,"
                             "   siren varchar(20),"
                             "   PRIMARY KEY(num),"
                             "   UNIQUE (siren)"
                             ")"
    )

    tables['Commandes'] = ("CREATE TABLE IF NOT EXISTS Commandes ("
                           "    num int NOT NULL AUTO_INCREMENT,"
                           "    total int NOT NULL,"
                           "    PRIMARY KEY(num)"
                           ")"

    )

    tables['Produits'] = ("CREATE TABLE IF NOT EXISTS Produits ("
                          "  numCommande int NOT NULL,"
                          "  produit varchar(200),"
                          "  FOREIGN KEY (numCommande) REFERENCES Commandes(num) ON DELETE CASCADE"
                          ")"
    )

    tables['Factures'] = ("CREATE TABLE IF NOT EXISTS Factures ("
                        "numClient int NOT NULL,"
                        "numEntreprise int NOT NULL,"
                        "numCommande int NOT NULL,"
                        "prix int NOT NULL,"
                        "FOREIGN KEY (numClient) REFERENCES Clients(num) ON DELETE CASCADE,"
                        "FOREIGN KEY (numEntreprise) REFERENCES Entreprises(num) ON DELETE CASCADE,"
                        "FOREIGN KEY (numCommande) REFERENCES Commandes(num) ON DELETE CASCADE"
                ")"


    )

    try:
        #Launching server
        connection = None


        connection = mysql.connector.connect(host="localhost", user="demo", password="Azerty@1234", database="faculte", auth_plugin="")

        cursor = connection.cursor()

        for nom_table in tables:
            description_table = tables[nom_table]
            cursor.execute(description_table)

        cursor.close()

        show(connection)

    except mysql.connector.Error as mce :
        print(f"Error {mce.args[0]} : {mce.args[1]}")
        sys.exit(-1)

    finally:
        if connection:
            connection.close()

