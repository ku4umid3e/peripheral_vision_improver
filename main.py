import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from handlers import greet_user, send_shulte, talk_to_me, send_pyramid, send_alphabet, menu_shulte


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

load_dotenv()

PROXY = {
    'proxy_url': os.getenv('PROXY_URL'),
    'urllib3_proxy_kwargs': {
        'username': os.getenv('PROXY_USERNAME'),
        'password': os.getenv('PROXY_PASSWORD')
    }
}


def main():
    shulte_bot = Updater(os.getenv('KEY'),
                         request_kwargs=PROXY, use_context=True)

    dp = shulte_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex("^(Шульте)$"), menu_shulte))
    dp.add_handler(MessageHandler(Filters.regex("^(Алфавит)$"), send_alphabet))
    dp.add_handler(MessageHandler(Filters.regex("^(Пирамида)$"), send_pyramid))
    dp.add_handler(CallbackQueryHandler(send_shulte))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    shulte_bot.start_polling()
    shulte_bot.idle()


if __name__ == "__main__":
    main()
