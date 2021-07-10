## Ce projet est réalise par Derridj Fares et Mansour Ka

## Réalisation d'une base de données à partir d'APIs:

### Nous avons choisi d'étudier l'ensemble des actualités sur le Cours des crypto-monnaies à partir de différentes sources d'informations sur le web.
#### Pour celà, nous allons avoir besoin de deux bases de données différentes.
#### Cependant, pour récupérer les informations nécessaires pour concevoir notre base de données, nous avons choisi deux APIs:
#### - Une Api pour récuperer les données des cryptomonnaies à un instant donné, pour celà nous avons décidé de choisir l'api de CoinGeko (via lien suivant) : https://www.coingecko.com/en/api#explore-api .

#### - Une Api pour récuperer l'actualité sur la cryptomonnaie (via lien suivant) : https://newsapi.org/ .


#### voici le schémas de notre base de données, conçue aprés la liaison des deux APIs:

![Schema_BDD](https://user-images.githubusercontent.com/57758790/124604766-8fc74400-de6b-11eb-9f22-9703d70bad3c.png)

#### - Explication de la conception de notre Base de Données:
##### Nous avons créer une table Assets (Voir le Schéma ci-dessus) qui va comporter un id comme primary key, nom de l'asset (ex bitcoin) et le symbole de l'asset.

##### On poursuit avec la création de la deuxème table qui est daily_asset_info cette table à pour objectif de sauvegarder l'historique de l'asset en daily  (prix,market_cap,rank) 

##### La relation entre la table Assets et daily_asset_info est une relation one-to-many et c'est grace a ça que l'on peut tracker la variation du prix market_cap rank en daily. 

##### Concernant les tables Articles et Publisher, la table Article va comporter à son tour un Id comme primary key car notre article est unique , une date de publication de l'article , une déscription et un titre et une foreign key de de la table publisher pour pouvoir savoir quel publisher est derière l'article.


##### La table Publisher quant à elle,elle fait office de référecnce pour les sources de nos articles.

#### - Et en fin on a développé les scripts en Python ( voir sur la branche master), pour récuper les données dont nous avons via les deux APIs, pour remplir notre de données.
