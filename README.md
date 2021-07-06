## Ce projet est réalise par Derridj Fares et Mansour Ka

## Réalisation d'une base de données à partir d'APIs:

### Nous avons choisi d'étudier l'ensemble des actualités sur le Cours des crypto-monnaies à partir de différentes sources d'informations sur le web.
#### Pour celà, nous allons avoir besoin de deux bases de données différentes.
#### Cependant, pour récupérer les informations nécessaires pour concevoir notre base de données, nous avons choisi deux APIs:
#### - Une Api pour récuperer les données des cryptomonnaies à un instant donné, pour celà nous avons décidé de choisir l'api de CoinGeko.
##### Link : https://www.coingecko.com/en/api#explore-api

#### - Une Api pour récuperer l'actualité sur la cryptomonnaie.
#### Link : https://newsapi.org/


![Schema_BDD](https://user-images.githubusercontent.com/57758790/124604766-8fc74400-de6b-11eb-9f22-9703d70bad3c.png)

### Nous allons créer une table Assets (Voir le Schéma ci-dessus) qui va comporter un id comme primary key, nom de l'asset (ex bitcoin) et le symbole de l'asset.

### On poursuit avec la création de la deuxème table qui est daily_asset_info cette table à pour objectif de sauvegarder l'historique du prix.
