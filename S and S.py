vimport socket
import sqlite3


def connexionBD():
   BD = sqlite3.connect("banque.db")
   #create a file (banque) even if it doesn't exist and if it does exist it just connects
   curseur = BD.cursor() 
   #create a cursor to  allows us to execute some sql commands
   curseur.execute("""CREATE TABLE client (
     id INTEGER PRIMARY KEY NOT NULL, 
     num_carte_bancaire INTEGER PRIMARY KEY NOT NULL, 
     nom TEXT  NOT NULL,
     solde float , 
     prélèvement float,
     operation_a_venir TEXT,
     virement float)""")
   #""": a docstring to allow us to write a string that's multiple lines without any special breaks 
	 # Create a table
	 BD.commit()
   #This method commits the current transaction. If you don’t call this method, anything you did since the last call to commit() is not visible from other database connections. If you wonder why you don’t see the data you’ve written to the database, please check you didn’t forget to call this method

	 return BD, curseur #curseur: valise pour les données 
   


for row in curseur:
   def authenification(id,num_carte_bancaire) :
     while True:
       accès = False
       id1=input(print ("Donner le num de votre carte d'identité: \n"))
       if id1 == client[0]:
         num_carte_bancaire1=input("\ndonner le num de votre carte bancaire: ")
           if num_carte_bancaire1=client[1]:
             print ("\nBienvenue")
             accès = True
          else:
             print ("\nErreur de connexion !")
       else:
         print ("\nErreur de connexion !") 




serveur=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 # we have to create a socket object and reserve a port on our pc
 # AF_INET refers to the address-family ipv4
 # SOCK_STREAM means connection-oriented TCP protocol
host=input("host: ")
port=input("port: ")# reserve a port on your computer
serveur.bind("",port) # écoute sur le port
 #we bound our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well.
serveur.listen (5)
 #we put the server into listening mode.5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket tries to connect then the connection is refused
print ("socket is listening")

while accès:
   # a forever loop until we interrupt it or an error  occurs
  client, nom = socket.accept()    
  print ('Got connection from', client[2] )
   # Establish connection with client
  client.send('Thank you for connecting'.encode())
  actif = True
   # send a thank you message to the client. encoding to send byte type
  client.close()
   # Close the connection with the client
  actif = False
  break
  # Breaking once connection 
   
  #At last, we make a while loop and start to accept all incoming connections and close those connections after a thank you message to all connected sockets

 for row in cursor:
   while actif:
     client.send("Bienvenue !",client[3].encode())
     client.send("votre solde est: ",client[4].encode())
     client.send("votre prélèvement est: ",client[5].encode())
     client.send("vos opérations à venir sont: ",client[6].encode())
     client.send("votre virement est: ",client[7].encode())
     break

 BD.close()
