# Projet bot Instagram
Objectif : Bot qui envoie automatiquement un message à des utilisateurs d'Instagram
Auteurs: STELLA Maxence, ACALASOW Farhan, CANTIN Paul

Pourquoi ce choix?
Les réseaux occupent une place de plus en plus importante dans la vie de chacun au quotidien. Ils deviennent une arme redoutable en termes de marketing, de pub provenant de marques, de personnes connues ou encore d'influenceurs. Il existe de nombreux bots sur les réseaux capables d'automatiser une multitude de tâches. Notre but est de créer un bot similaire plus efficace en termes de marketing en ciblant davantage les clients susceptibles d'être intéressés par un produit. 
Au préalable, notre compte est abonné à plusieurs marques et influenceurs dans une gamme de produits précis. En l'occurrence, le marché des sneakers (chaussures/baskets) qui est en pleine expansion. C'est pourquoi on a décidé de créer un bot qui envoie automatiquement un message à des utilisateurs d'Instagram intéressés par les sneakers.

Comment fonctionne le bot?
Le bot se connecte à notre compte instagram et envoie un message à chaque personnes qui commentent les deux dernières publications parmi les comptes auxquels on est abonné. Il va de soi que 100% de nos abonnements soient des marques de sneakers ou des comptes dédiés aux sneakers. 

Explication technique du bot:
Au préalable, on a installé des packages python, en l'occurrence selenium qui est le plus important pour automatiser la tâche à effectuer sur une page web (ici Instagram), random et time. Il faut aussi installer un webdriver qui nous permet d'ouvrir google Chrome.
Notre programme est composé de 6 fonctions.
1) La fonction "login" permet d'accepter les cookies et ensuite de se connecter à Instagram via le compte <<shoesmakeyourlife>>.
2) La fonction "profil" permet d'aller sur la page de profil de notre compte <<shoesmakeyourlife>>.
3) La fonction "following" permet de faire une listes des comptes auxquels on s'est abonné.
4) La fonction "selectRandom" nous permet de choisir au hasard un compte de la liste de la fonction "following".
5) La fonction "checkcomment" nous permet d'aller sur une publication du compte choisi au hasard grâce à la fonction précédente et de faire une liste des personnes qui l'ont commentés. 
6) La fonction "message" qui envoie un message à caractère publicitaire à toutes les personnes de la liste de la fonction "checkcomment".
