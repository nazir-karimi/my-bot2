from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

TOKEN = "8796614951:AAHMmmrATx5TcMl-ZSeVMUcnR0CeybrW1Uc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 ربات روشن شد!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("پیام شما: " + update.message.text)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))

    print("Bot started...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
