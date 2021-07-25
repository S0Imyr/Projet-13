## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement 

## Pipeline CI/CD

Le pipeline est géré avec Circle CI.
Lorsqu'il y a une modification sur le dépôt GitHub, deux cas de figures :
 - la modification concerne une branche différente de la branche master :
 seul les tests sont exécutés
 - la modification concerne la branche master : 
 les tests sont exécutés, ensuite la conteneurisation s'exécute sur Docker et enfin  le site est déployé sur Heroku. Pour qu'une étape s'exécute, il faut que la précédente ait été couronnée de succès.

## CircleCI

Il est d'abord nécessaire de se créer un compte sur [CircleCI](https://circleci.com/signup/). La création avec Github permet de relier les dépôts Github et le compte CircleCI.
Pour la suite, il faut avoir configuré différents comptes. On définira ensuite des variables d'environnement correspondant à ces comptes.

## DockerHub

Le premier de ces comptes [DockerHub](https://hub.docker.com/signup).
Une fois le compte créé et connecté, cliquer sur 'Create Repository' pour créer un nouveau dépôt.

Pour le fonctionnement de Circle, il faudra pouvoir s'authentifier sur Docker à l'aide d'un token.
Pour obtenir le token :
 - cliquer sur le menu déroulant sur votre identifiant,
 - cliquer sur 'Account settings',
 - cliquer sur le menu 'Security',
 - cliquer sur 'New Access Token',
 - définir un nom et obtenir le token.

On retiendra trois variables d'environnement pour CircleCI :
 - DOCKER_LOGIN : l'identifiant donné,
 - DOCKER_PASSWORD : le token obtenu,
 - PROJECT_NAME : le nom du dépôt créé.

## Heroku

Ensuite, il faut créé un compte sur [Heroku](https://signup.heroku.com/).
Pour créer une nouvelle application, aller dans le menu 'New' et sélectionner 'Create new app'. On préfera inclure oc-lettings dans le nom de l'application.

On pourra installer le client Heroku : [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

Il est également nécessaire d'obtenir un token.
Pour obtenir un token tapper dans un terminal `$heroku auth:token`

On retiendra deux variables d'environnement pour CircleCI :
 - HEROKU_APP_NAME : le nom de l'application créée,
 - HEROKU_TOKEN : le token obtenu dans le terminal.

## Sentry

Enfin pour permettre le suivi des erreurs, on créé un compte sur [Sentry](https://sentry.io/signup).
Il est également nécessaire d'obtenir un token. Pour l'obtenir :
 - cliquer sur 'Settings' dans le menu de droite,
 - aller dans 'Projects',
 - dans 'General Settings' trouver le champs 'Security Token' où se trouve le token.

On retiendra ce token pour la variable d'environnement SENTRY_DSN.

Une erreur volontaire est définie à l'url de l'application complétée par /sentry-debug/
Elle sera visible dans les Issues, une fois connecté sur le compte [Sentry](https://sentry.io/).

## Fin de la configuration sur CircleCI :

Il s'agit désormais de définir les variables d'environnements dans CircleCI.
Une fois connecté sur votre compte CircleCI:
 - sélectionner 'Projects',
 - cliquer sur le repo de notre application,
 - cliquer sur 'Projects settings' à droite,
 - cliquer sur 'Environment Variables'
 - Cliquer sur 'Add Environment Variable' pour ajouter les variables suivantes :
  - DOCKER_LOGIN
  - DOCKER_PASSWORD
  - PROJECT_NAME
  - HEROKU_APP_NAME
  - HEROKU_TOKEN
  - SENTRY_DSN
  - DJANGO_SECRET_KEY : la clé Django

Pour cette dernière, on peut la générer dans un terminal dans l'environnement virtuel de l'application :
`$ from django.core.management.utils import get_random_secret_key`  
`$ print(get_random_secret_key())`

## Déploiement d'une image Docker en local

Pour déployer une image Docker en local, on va devoir aller sur DockerHub pour copier le nom de l'image souhaitée.
Ensuite en renseignant ce nom on tape la commande suivante :

`$ docker run --pull always -p 8000:8000 --name <nom_local> <nom_image_docker>`
