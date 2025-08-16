from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I crazzy?")
    
async def main():
    app = ApplicationBuilder().token('7814679775:AAHUfXZ-4_gDGeW2Oi7KjlV1NKX6AD-knc4').build()
    
    app.add_handler(CommandHandler("start",start))
    
    await app.run_polling()
    
if'__name__'=="__Mi_bot__":
    import asyncio
    asyncio.run(Mi_bot())