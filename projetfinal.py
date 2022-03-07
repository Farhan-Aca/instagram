""" Les Packages Python """

import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

""" liste des messages """

list_message = ["Nous avons vu que vous êtes très intéressé(e) par l'achat de chaussures. Venez visitez notre page Instagram et découvrir nos derniers arrivages.",
                "Nous sommes spécialisé dans la conception de sneakers et nous savons que cela vous intéresse. Venez découvrir notre gamme de sneakers faites pour vous.",
                "Des sneakers sur mesure ça vous intéresse ? Venez découvrir notre pages dédiées aux sneakers sans plus attendre. Nous vous attendons avec impatience.",
                "Des sneakers pas cher à volonté!!"]
#Ils seront tirés au sort grace au select random,ligne 5.
first_passage_in_msg = True

""" Les fonctions """


def login():
    driver.get("https://www.instagram.com/")

    try:
        accepte_cookies = driver.find_element(By.XPATH,
                                              "//button[text()='Autoriser les cookies essentiels et optionnels']")
        accepte_cookies.click()  # Apparition du premier cookie & on clique sur accepter.

        print("Cookies acceptés")
        time.sleep(3)
    except:
        print("Cookies non acceptés")

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.click()
    username.send_keys("shoesmakeyourlife")  # On rentre notre identifiant
    time.sleep(2)

    password.click()
    password.send_keys("Acalasow24")  # On rentre notre mot de passe
    time.sleep(2)

    try:
        connexion = driver.find_element(By.XPATH, "//div[text()='Connexion']")
        connexion.click()  # On clique sur le bouton connexion
        print("Connexion réussi")
    except:
        print("Connexion échoué")

# On arrive sur la page d'accueil
def profil():
    try:
        time.sleep(5)
        onglet_profil = driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img')
        onglet_profil.click()
        print("On a bien cliqué sur l'onglet ")
        time.sleep(3)

        profil_instagram = driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div')
        profil_instagram.click()
        print('Ouverture du profil')  # On a cliqué sur la rubrique profil
    except:
        print("Echec de l'ouverture du profil")

#On va faire la liste des abonnements

def following():
    time.sleep(5)

    a = driver.find_element(By.XPATH, "//a[contains(@href,'/following')]")
    print(a.text)
    if '\n' in a.text:     #Ici on extrait le nombre d'abonnements via deux méthodes,en fonction de si la page est ouvert en grand ou petit.
        nb = int(a.text.split('\n')[0])
    else:
        nb = int(a.text.split(' ')[0])
    a.click()  # On clique sur le bouton abonnements.
    print("Ouverture de l'abonnements")
    time.sleep(2)
    links = [] #Liste des liens en Url
    print(nb)
    for i in range(1, nb + 1):
        follower = driver.find_element(By.XPATH,
                                       '/html/body/div[6]/div/div/div/div[3]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a'.format(
                                           i))
        link = follower.get_attribute("href")
        links.append(link)
    # Ici pour chaque abonnements,la seule chose qui differe dans leurs elements se situe au niveau du li{}.
    # On a donc fait une boucle qui prend chaque elements de la liste des abonnées et puis nous la renvoie dans la liste links.
    return links


def selectRandom(Lien):      #fonction qu'on utilisera pas
    return random.choice(Lien)


def checkcomment():
    time.sleep(7)
    photo = driver.find_element(By.XPATH, "(//div[@class='eLAPa'])[1]") #Il cherche la derniere publication
    photo.click()
    comment = [] #Liste des personnes qui ont commentées(sous forme Url)
    time.sleep(3)
    #Boucle qui nous permet de cliquer sur le bouton +,afin d'afficher tous les commentaires de la publication
    while True:
        try:
            commentplus = driver.find_element(By.XPATH,
                                              '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/li/div/button')
            commentplus.click()
            time.sleep(3)
        except:
            break

    time.sleep(2)
    #La boucle commence à partir du premier commentaires et s'arrête au 500 ème
    for i in range(1, 500):
        try:
            commentateur = driver.find_element(By.XPATH,
                                               f'/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul[{i}]/div/li/div/div/div[2]/h3/div/span/a')
            com = commentateur.get_attribute("href")
            comment.append(com)
        except:
            break   # Sort de la boucle lorsque sa n'affiche de commentaire sur instragram.

    # Condition qui nous permet de passer à la deuxième publication,s'il n'y a de commentaire à la premiere publication
    if len(comment) > 0:
        pass
    else:
        print("Il n'y a pas de commentaire sur la 1ère publication.")
        time.sleep(2)
        fermer_photo = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/button")
        fermer_photo.click()
        time.sleep(2)
        photo2 = driver.find_element(By.XPATH, "(//div[@class='eLAPa'])[2]")
        photo2.click()
        time.sleep(2)
    while True:
        try:
            commentplus = driver.find_element(By.XPATH,
                                              '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/li/div/button')
            commentplus.click()
            time.sleep(3)
        except:
            break

    time.sleep(2)
    for i in range(1, 500):
        try:
            commentateur = driver.find_element(By.XPATH,
                                               f'/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul[{i}]/div/li/div/div/div[2]/h3/div/span/a')
            com = commentateur.get_attribute("href")
            comment.append(com)
        except:
            break

    return comment


# first_passage_in_msg check s'il s'agit du premier passage dans la page "message"
def message(first_passage_in_msg):
    driver.get("https://www.instagram.com/direct/inbox/")

    time.sleep(4)
    if first_passage_in_msg:
        notif_message = driver.find_element(By.XPATH, '//button[contains(@class,"aOOlW   HoLwm ")]')
        notif_message.click()

    time.sleep(1)
    bouton_message = driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
    bouton_message.click()

    time.sleep(1)
    boite_recherche = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input")
    boite_recherche.click()

    time.sleep(3)
    # Boucle qui rentre tout les noms des personnes qui ont commenté
    for i in list_client:
        driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]").click()
        if driver.find_element(By.XPATH, '//input[@placeholder="Recherchez..."]'):
            nom_client = driver.find_element(By.XPATH, '//input[@placeholder="Recherchez..."]')
            nom_client.send_keys(i)
            time.sleep(2)
            driver.find_element(By.XPATH, "(//button[@class='wpO6b  '])[1]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[@class='sqdOP yWX7d    y3zKF   cB_4K  ']").click()
            time.sleep(4)
            # On envoie des messages personnalisé,c'est à dire le nom de la personne + un message de notre liste tiré au sort
            if driver.find_element(By.XPATH,
                                   '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'):
                message_envoyez = driver.find_element(By.XPATH,
                                                      '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                message_envoyez.send_keys(f"Bonjour, {i} \n" + selectRandom(list_message))
                print(selectRandom(list_message))
                time.sleep(3)

                driver.find_element(By.XPATH,
                                    '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                print(i)

                time.sleep(2)

                open_messageonglet = driver.find_element(By.XPATH, "//a[contains(@href,'/inbox/')]")
                open_messageonglet.click()
                time.sleep(2)

                bouton2_message = driver.find_element(By.XPATH,
                                                      '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
                bouton2_message.click()

                time.sleep(2)
        else:
            pass
    return False


""" Le programme principal """

PATH = "C:\SeleniumDrivers\chromedriver.exe"
driver: WebDriver = webdriver.Chrome(PATH) # Ouverture de Google Chrome



login()  # Validation des cookies et connexion à instagram

profil()  # Accès au profil de l'utilisateur
lien = following()  # Création d'une liste de nos abonnements (following)
print(lien) # Affichage de la liste

for elt in lien:

    print(f"Le compte instagram selectionné est: {elt}")
    driver.get(f"{elt}")  # Ouverture du profil de notre abonnement
    time.sleep(8)
    list_client = checkcomment()  # Création d'une liste des personnes qui ont commenté et liké la publication
    if following in list_client:
        list_client.remove(elt)
    else:
        pass
    print(list_client)
    list_client = [e[26:][:-1] for e in list_client] # On transforme l'url en nom instagram
    list_client = list(set(list_client))  # On enlève les doublons de la liste,pour eviter d'envoie le message plusieur à la même personne
    print(list_client)
    print(f"La liste contient {len(list_client)} client(s).\n")
    time.sleep(5)
    print("Message envoyé à :")

    if len(list_client) != 0:
        first_passage_in_msg = message(first_passage_in_msg)  # Envoie du message aux personnes préalablement triées




