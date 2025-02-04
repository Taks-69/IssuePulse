import nest_asyncio
nest_asyncio.apply()

import asyncio
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configure le logging pour afficher les informations dans la console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Remplace par ton token Telegram
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Remplace par les informations de ton dépôt GitHub
GITHUB_OWNER = "YOUR_GITHUB_USERNAME"
GITHUB_REPO = "YOUR_GITHUB_REPOSITORY"


TELEGRAM_CHAT_ID =  123456789 # Replace with your Telegram chat ID

# Variables pour stocker les derniers numéros d'issue et de pull request connus
last_issue_number = 0
last_pr_number = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user

    # Envoie un message à l'utilisateur avec l'ID du chat
    await update.message.reply_text(f"Ton Chat ID est : {chat_id}")

    # Consigne dans la console l'utilisateur et l'ID du chat
    logging.info(f"L'utilisateur {user.username} ({user.id}) a exécuté la commande /start dans le chat {chat_id}")

    # Vérifie si l'ID du chat est déjà configuré pour les notifications
    if chat_id == TELEGRAM_CHAT_ID:
        await update.message.reply_text("Les notifications GitHub sont déjà configurées pour cet ID de chat.")
    else:
        await update.message.reply_text(
            "Veuillez mettre à jour la variable TELEGRAM_CHAT_ID dans le script avec cet ID pour recevoir les notifications GitHub."
        )

async def check_updates(context: ContextTypes.DEFAULT_TYPE):
    global last_issue_number, last_pr_number
    chat_id = TELEGRAM_CHAT_ID

    # Vérifie les issues sur GitHub
    issues_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/issues"
    try:
        response = requests.get(issues_url, timeout=10)
        response.raise_for_status()
        issues = response.json()

        for issue in issues:
            # Si ce n'est pas un pull request
            if "pull_request" not in issue:
                if issue["number"] > last_issue_number:
                    message = (
                        f"Nouvelle issue #{issue['number']}: {issue['title']}\n"
                        f"{issue['html_url']}"
                    )
                    await context.bot.send_message(chat_id=chat_id, text=message)
                    last_issue_number = issue["number"]
            else:
                # C'est un pull request
                if issue["number"] > last_pr_number:
                    message = (
                        f"Nouveau pull request #{issue['number']}: {issue['title']}\n"
                        f"{issue['html_url']}"
                    )
                    await context.bot.send_message(chat_id=chat_id, text=message)
                    last_pr_number = issue["number"]

    except requests.exceptions.RequestException as e:
        logging.error(f"Erreur lors de la récupération des données GitHub : {e}")

async def main():
    # Crée l'application avec ton token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Ajoute le handler pour la commande /start
    application.add_handler(CommandHandler("start", start))

    # Programme un job répétitif pour vérifier les mises à jour toutes les 60 secondes
    job_queue = application.job_queue
    job_queue.run_repeating(check_updates, interval=60, first=10)

    # Lance le bot en mode polling
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
