import re
from dotenv import load_dotenv
import requests
import json
import random
import os
import time
from playwright.sync_api import sync_playwright



load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
tweets_history_file = "json/tweets_history.json"

CRYPTO_KEYWORDS = (
    r'crypto|cryptocurrency|blockchain|bitcoin|btc|ethereum|eth|altcoin|'
    r'decentralized|defi|dapp|smart contract|ledger|coin|new coin|my coin|'
    r'official coin|get your|\$[A-Z0-9]+|join now|buy now|special token|launch|'
    r'you can buy|airdrop|exclusive|limited|offer|pre-sale|presale|mint|minting|'
    r'token|reward|earn|wallet|public sale|private sale|'
    r'0x[a-fA-F0-9]{40}|[A-Za-z0-9\-]+\.eth|[A-Za-z0-9\-]+\.crypto|'
    r'[1-9A-HJ-NP-Za-km-z]{43,44}|' 
    r'https?://[A-Za-z0-9\-._~:/?#[\]@!$&\'()*+,;=]+'
)


def load_tweets_history():
    try:
        with open(tweets_history_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_tweet_history(tweets_history):
    with open(tweets_history_file, "w") as f:
        json.dump(tweets_history, f, indent=4)

def scrape_latest_tweet(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        )

        try:
            load_cookies(context)
            print("Cookies chargés avec succès.")
        except FileNotFoundError:
            print("Fichier cookies.json introuvable. Connecte-toi d'abord.")
            browser.close()
            return None

        page = context.new_page()
        print(f"Chargement de l'URL : {url}")
        page.goto(url)

        try:
            tweet_selector = "[data-testid='tweet']"
            print("En attente que les tweets soient visibles...")
            page.wait_for_selector(tweet_selector, timeout=15000)

            tweet_elements = page.query_selector_all(tweet_selector)
            tweet = tweet_elements[0] 
            pinned_tweet = "[data-testid='socialContext']"

            if tweet_elements[0].query_selector(pinned_tweet):
                pinned_text = tweet_elements[0].query_selector(pinned_tweet).inner_text()
                if pinned_text == "Épinglé":
                    tweet = tweet_elements[1] 
                else:
                    tweet = tweet_elements[0] 
            else:
                tweet = tweet_elements[0]  

            tweet_text_div = tweet.query_selector("[data-testid='tweetText']")
            if tweet_text_div:
                tweet_text = tweet_text_div.inner_text()
                print(f"Dernier tweet détecté : {tweet_text}")
                return tweet_text
            else:
                return None
            
        except Exception as e:
            print(f"Erreur lors du scraping : {e}")
        finally:
            browser.close()

def load_cookies(context):
    with open("json/cookies.json", "r") as f:
        cookies = json.load(f)
    context.add_cookies(cookies)

def send_telegram_message(message):
    formatted_message = f"🚨🚨 **ALERTE NOUVEAU TWEET CRYPTO** 🚨🚨\n\n" \
                        f"🔥 **Nouveau tweet détecté !** 🔥\n\n" \
                        f"📢 **Utilisateur**: {message['user_handle']}\n" \
                        f"💬 **Contenu du tweet**: \n\n{message['tweet_text']}\n\n" 

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": formatted_message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Message envoyé avec succès sur Telegram.")
        else:
            print(f"Erreur Telegram : {response.text}")
    except Exception as e:
        print(f"Erreur lors de l'envoi Telegram : {e}")




def monitor_tweets():
    tweets_history = load_tweets_history()
    
    users_urls = [
        "Xavier75",
        "Amyti191",
        "elonmusk",  
        "MrBeast",
        "realDonaldTrump",
        "Cobratate",
        "ishowspeedsui",
        "Cristiano",
        "neymarjr",
    ]

    while True:
        try:
            for url in users_urls:
                latest_tweet = scrape_latest_tweet(f"https://x.com/{url}")
                
                if latest_tweet:
                    user_handle = url.split("/")[-1] 
                    if re.search(CRYPTO_KEYWORDS, latest_tweet, re.IGNORECASE):
                        if user_handle not in tweets_history or tweets_history[user_handle] != latest_tweet :
                            tweets_history[user_handle] = latest_tweet
                            save_tweet_history(tweets_history)
                            message = {
                                "user_handle": user_handle,
                                "tweet_text": latest_tweet
                            }
                            send_telegram_message(message)
                            time.sleep(random.uniform(10, 25))
                        else:
                            print(f"Aucun nouveau tweet détecté pour {user_handle}.")
                            time.sleep(random.uniform(10, 25))
                    else:
                        print(f"Le tweet de {user_handle} ne contient pas de termes liés à la crypto.")
                        time.sleep(random.uniform(10, 25))
                else:
                    print(f"Impossible de récupérer le dernier tweet pour {url}.")
            time.sleep(30)
        except Exception as e:
            print(f"Erreur lors de la surveillance : {e}")
            time.sleep(10)
