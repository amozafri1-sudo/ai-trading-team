import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# =========================
# AI TRADING TEAM
# Core Telegram Bot
# =========================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

BOT_NAME = "AI Trading Team"


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    message = (
        "🚀 Welcome to AI Trading Team!\n\n"
        "Your intelligent market analysis platform.\n\n"
        "🌐 Supported Markets:\n"
        "• Cryptocurrency\n"
        "• Forex\n"
        "• Gold\n\n"
        "🧠 AI Analysis Engine: Initializing\n"
        "📊 Technical Analysis: Coming Soon\n"
        "🛡 Risk Management: Coming Soon\n\n"
        "Use /help to see available commands."
    )

    await update.message.reply_text(message)


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    message = (
        "📌 AI Trading Team Commands\n\n"
        "/start - Start the bot\n"
        "/help - Show commands\n"
        "/status - System status\n"
        "/markets - Supported markets\n"
        "/about - About the project\n"
    )

    await update.message.reply_text(message)


async def status(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "🟢 Telegram Bot: Online\n"
        "🧠 AI Engine: Not Connected\n"
        "📊 Market Data: Not Connected\n"
        "🛡 Risk Engine: Under Development"
    )


async def markets(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "🌍 Supported Markets\n\n"
        "₿ Cryptocurrency\n"
        "💱 Forex\n"
        "🥇 Gold\n\n"
        "Market integrations are under development."
    )


async def about(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "AI Trading Team\n\n"
        "A modular multi-AI market analysis platform "
        "for cryptocurrency and forex markets.\n\n"
        "⚠️ No guaranteed trading profits."
    )


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):
    logger.error(
        "An error occurred:",
        exc_info=context.error
    )


def main():

    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is not configured."
        )

    application = (
        Application.builder()
        .token(token)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        CommandHandler("status", status)
    )

    application.add_handler(
        CommandHandler("markets", markets)
    )

    application.add_handler(
        CommandHandler("about", about)
    )

    application.add_error_handler(error_handler)

    logger.info("%s is starting...", BOT_NAME)

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
