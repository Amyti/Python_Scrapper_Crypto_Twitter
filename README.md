
---

# Twitter Crypto Monitor - Projet de surveillance des tweets

**Auteur** : Amir Kabbouri

Ce projet permet de surveiller les derniers tweets de certains utilisateurs spécifiques sur Twitter, rechercher des mots-clés associés à la crypto-monnaie dans leurs tweets, puis envoyer une alerte via Telegram lorsqu'un tweet correspondant est détecté.

Le projet se compose de deux étapes principales :

1. **Connexion et sauvegarde des cookies** via `login.py`.
2. **Surveillance des tweets** via `main.py`.

## Prérequis

Avant de commencer, assure-toi que les prérequis suivants sont installés :

- Python 3.x
- `pip` pour installer les dépendances Python
- Un **token Telegram** pour recevoir les notifications des tweets détectés.

## Installation

### 1. Clone le projet

Clone ce repository sur ton ordinateur.

```bash
git clone https://github.com/amir-kabbouri/twitter-crypto-monitor.git
cd twitter-crypto-monitor
```

### 2. Crée un environnement virtuel

Il est recommandé de créer un environnement virtuel pour gérer les dépendances.

```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/macOS
venv\Scripts\activate     # Sur Windows
```

### 3. Installe les dépendances

Installe toutes les dépendances nécessaires avec `pip`.

```bash
pip install -r requirements.txt
```

### 4. Configure les variables d'environnement

Crée un fichier `.env` à la racine du projet et ajoute tes informations Telegram (Token et Chat ID) comme suit :

```env
TELEGRAM_TOKEN=ton_telegram_token
TELEGRAM_CHAT_ID=ton_chat_id
```

- **TELEGRAM_TOKEN** : Obtenu lors de la création de ton bot sur Telegram via le BotFather.
- **TELEGRAM_CHAT_ID** : L'ID de la conversation où tu souhaites recevoir les messages. Tu peux obtenir cet ID en envoyant un message à ton bot, puis en utilisant l'API de Telegram pour récupérer l'ID.

## Étapes pour utiliser le projet

### 1. **Effectuer la connexion et sauvegarder les cookies**

Avant de pouvoir surveiller les tweets, tu dois d'abord te connecter à Twitter et sauvegarder les cookies pour une session persistante. Pour ce faire, suis ces étapes :

1. Exécute le script `login.py` pour lancer un navigateur qui te permettra de te connecter manuellement.

```bash
python login.py
```

2. Le navigateur Playwright va s'ouvrir et te demander de te connecter à ton compte Twitter. Une fois que tu es connecté, le script attendra un moment et sauvegardera les cookies de ta session dans le fichier `json/cookies.json`.

3. **Une fois les cookies sauvegardés**, tu peux fermer le navigateur.

Ces cookies seront utilisés pour maintenir la session active sans avoir besoin de te reconnecter à chaque fois.

### 2. **Lancer le script de surveillance des tweets**

Après avoir sauvegardé les cookies, tu peux lancer le script principal `main.py` pour surveiller les tweets des utilisateurs spécifiés.

```bash
python main.py
```

- Ce script surveille les derniers tweets des utilisateurs définis dans la liste `users_urls`.
- Il recherche des mots-clés associés à la crypto-monnaie dans chaque tweet.
- Si un tweet correspondant est trouvé, une alerte est envoyée à ton compte Telegram avec le contenu du tweet et des informations supplémentaires.

Le script continuera à tourner en boucle, vérifiant les nouveaux tweets toutes les 30 secondes.

### 3. **Garder le bot en ligne (facultatif)**

Si tu veux garder ton bot en ligne en permanence, même si tu l'exécutes sur un serveur, tu peux utiliser un serveur Flask pour faire tourner l'application. Le script `main.py` inclut la fonction `keep_alive()` qui fait tourner un serveur Flask en arrière-plan.

Cela permet de maintenir le bot actif sur des plateformes comme Replit ou des serveurs cloud qui nécessitent une activité web pour ne pas se mettre en veille.

Tu peux démarrer le serveur avec cette commande :

```bash
python main.py
```

Le serveur sera disponible sur `http://127.0.0.1:8080` ou `http://<ton_ip>:8080`.

### 4. **Interagir avec l'application web (facultatif)**

Une fois que le serveur Flask est lancé, tu peux accéder à l'interface web pour vérifier que ton bot est bien en ligne. Ouvre simplement ton navigateur et va à l'URL suivante :

```
http://127.0.0.1:8080
```

Cela affichera un message confirmant que le bot est en ligne.

## Structure du projet

Voici un aperçu de la structure du projet :

```
twitter-crypto-monitor/
│
├── json/
│   ├── cookies.json          # Fichier contenant les cookies de session Twitter
│   └── tweets_history.json   # Historique des tweets surveillés
│
├── main.py                   # Script principal de surveillance des tweets
├── login.py                  # Script de connexion pour sauvegarder les cookies
├── requirements.txt          # Liste des dépendances du projet
├── .env                      # Variables d'environnement (Telegram Token et Chat ID)
└── README.md                 # Ce fichier
```

## Dépannage

- **Problème de cookies** : Si tu rencontres des erreurs liées aux cookies, assure-toi que le fichier `cookies.json` est correctement généré. Tu peux essayer de refaire la connexion en exécutant `login.py` à nouveau.
- **Erreur Telegram** : Si les messages Telegram ne sont pas envoyés, vérifie que ton `TELEGRAM_TOKEN` et `TELEGRAM_CHAT_ID` sont correctement configurés dans le fichier `.env`.

## Auteurs

- **Amir Kabbouri** - [Ton GitHub](https://github.com/amir-kabbouri)

---

Si tu as des questions ou des améliorations à suggérer, n'hésite pas à ouvrir une *issue* ou à envoyer une *pull request*.

