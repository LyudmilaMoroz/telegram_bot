from secret import TGTOKEN
from telegram.ext import Updater, CommandHandler
from photo_museum import get_current_exhibition
from weather import get_weather
from events import get_events
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
updater = Updater(TGTOKEN)
dispatcher = updater.dispatcher


# Create and send message for a new user
def start(update, context):
    logging.info(f"I'm inside start handler from {update.effective_user}, {update.effective_chat}")
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Hello, I'm a bot with information about events in Helsinki. Please, ask me something. "
             "You can find more with the /help command."
    )


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Create a list with tutorial
def help(update, context):
    logging.info(f"I'm inside help handler from {update.effective_user}, {update.effective_chat}")
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="""
        Hey, I'm here to help you!
        
        I can do:
        /start : this is our first meeting. I'll always remember us this way.
        
        /help : this command shows a tutorial and a whole list with commands.
        
        /photo_ex : this command shows all current exhibitions in The Finnish museum of Photography.
        
        /weather : this command shows current weather in a chosen city. 
Please, write the city's name in English with a first capital letter.

        /event : this command shows different events in Helsinki. 
All list with events - music, parties, art, concerts, festivals, sports, business, dance, health-wellness, comedy, performances. 
Please, write command in this way: "/event sports"
"""
    )


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


# Send info about photo exhibitions
def photo_ex(update, context):
    logging.info(f"I'm inside photo_exhibition handler from {update.effective_user}, {update.effective_chat}")
    chat_id = update.effective_chat.id
    url = 'https://www.valokuvataiteenmuseo.fi/en/exhibitions/current-exhibitions'
    context.bot.send_message(
        chat_id=chat_id,
        text=get_current_exhibition(url)
    )


photo_ex_handler = CommandHandler('photo_ex', photo_ex)
dispatcher.add_handler(photo_ex_handler)


# Send info about events
def event(update, context):
    logging.info(f"I'm inside event handler from {update.effective_user}, {update.effective_chat}")
    chat_id = update.effective_chat.id
    args = context.args
    choice = ' '.join(args)
    context.bot.send_message(
        chat_id=chat_id,
        text=get_events(choice)
    )


event_handler = CommandHandler('event', event)
dispatcher.add_handler(event_handler)


# Send weather forecast
def weather(update, context):
    logging.info(f"I'm inside weather handler from {update.effective_user}, {update.effective_chat}")
    chat_id = update.effective_chat.id
    args = context.args
    city = ' '.join(args)
    context.bot.send_message(
        chat_id=chat_id,
        text=get_weather(city)
    )


weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

updater.start_polling()
updater.idle()
