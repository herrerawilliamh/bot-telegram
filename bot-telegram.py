#echo "# bot-telegram" >> README.md
#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/#herrerawilliamh/bot-telegram.git
#git push -u origin main

from telegram import Update
from telegram.ext import (Application, 
                          CommandHandler, 
                          MessageHandler,
                          filters,
                          ContextTypes)
from dotenv import load_dotenv
import os

load_dotenv()

async def start(update: Update, 
                context: ContextTypes):
    await update.message.reply_text('Hola!, soy un bot de Telegram y estoy aquí para ayudarte.')


async def links(update: Update, 
                 context: ContextTypes):
    await update.message.reply_text('Discord: https://discord.gg/herrerawilliamh\
                                    Twitter: https://twitter.com/herrerawilliamh\
                                    Instagram:  https://www.instagram.com/herrerawilliamh\
                                    Facebook: https://www.facebook.com/herrerawilliamh\
                                    YouTube: https://www.youtube.com/channel/@herrerawilliamh')

def answer(text: str):
    text = text.lower()
    if 'hola' in text:
        return 'Hola, cómo estás?'
    elif 'bien' in text:
        return 'Me alegra mucho que estés bien.'
    elif 'mal' in text:
        return 'Lo lamento mucho. Espero te sientas bien pronto.'
    elif 'gracias' in text:
        return 'De nada. Estoy aquí para ayudarte.'
    elif 'ayuda' in text:
        return '¿En qué puedo ayudarte?'
    elif 'adios' in text:
        return 'Hasta la proxima!'
    else:
        return 'No te entiendo. Por favor, repita.'
    
async def chat_messages(update: Update, 
                        context: ContextTypes.DEFAULT_TYPE)  -> None:
    type = update.message.chat.type
    if type == 'private':
        text = update.message.text
        response = answer(text)
        await update.message.reply_text(response)

if __name__ == '__main__':
    app = Application.builder().token(os.getenv('7018836952:AAFd-K9GCSkiKysQCB3OzXYMpba1gCP6AhY')).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('links', links))
    app.add_handler(MessageHandler(filters.TEXT, chat_messages))
    app.run_polling(poll_interval=1)