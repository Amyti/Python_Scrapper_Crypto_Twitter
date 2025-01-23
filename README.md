
---

# Twitter Crypto Monitor - Projet de surveillance des tweets

**Auteur** : Amir Kabbouri

Ce projet permet de surveiller les derniers tweets de certains utilisateurs spécifiques sur Twitter, rechercher des mots-clés associés à la crypto-monnaie dans leurs tweets, puis envoyer une alerte via Telegram lorsqu'un tweet correspondant est détecté.

Le projet se compose de deux étapes principales :

1. **Connexion et sauvegarde des cookies** via `login.py`.
2. **Surveillance des tweets** via `main.py`.

## Prérequis

Avant de commencer, assure-toi que les prérequis suivants sont installés :

- Python 3.12.8 ou superieur
- `pip` pour installer les dépendances Python
- Un **token Telegram** pour recevoir les notifications des tweets détectés.

## Installation

### 1. Clone le projet

Clone ce repository sur ton ordinateur.

```bash
git clone https://github.com/Amyti/Python_Scrapper_Crypto_Twitter.git
cd Python_Scrapper_Crypto_Twitter
```


### 2. Installe les dépendances

Installe toutes les dépendances nécessaires avec `pip`.

```bash
pip install -r requirements.txt
```

### 3. Configure les variables d'environnement

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

Le script continuera à tourner en boucle, vérifiant les nouveaux tweets toutes les 10 à 30 secondes.

## Auteurs

- **Amir Kabbouri** - [My Git](https://github.com/Amyti)

---
