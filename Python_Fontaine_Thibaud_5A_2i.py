import requests
import os

while(True):

	#Menu pour l'utilisateur
	affichage = raw_input ("1-->Afficher tous | 2-->Afficher un produit | 3-->Ajouter :  | 4-->Ajouter un produit : | q --> Quitter ")

	#Afficher tous les produits
	if affichage =='1':

		response = requests.get("http://localhost:8989/tous")
		print(response.text)
	
	#Afficher le produit correspondant au code
	if affichage =='2':
		code = str(input("Veuillez entrer un code : "))
		response = requests.get("http://localhost:8989/produit/"+code)
        	print(response.json())

	#Ajoute un produit predefinis
	if affichage =='3':
		
		data = {"code":"10", "designation":"PC","prix":"600"}
		r = requests.post("http://localhost:8989/ajouterunproduit", data = data)
		print("Produit ajoute")

	#Ajoute un produit que l'utilisateur souhaite
	if affichage =='4':
		code = str(input("Entrer un code : "))
		designation = raw_input ("Entrer le nom du produit : ")
		prix = raw_input ("Entrer le prix du produit : ")

		print ("Le produit suivant a ete ajoute : "+code+"/"+designation+"/"+prix)
		requests.post('http://localhost:8989/ajouter', {'code':code, 'designation':designation, 'prix':prix})

	#Quitte l'application
	if affichage == 'q':
		break
