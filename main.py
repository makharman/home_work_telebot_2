import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton


token='6387514894:AAE70uUBP9Eo1ZdPkBFS53Op8gEG9LkVyO8'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['dog'])
def start_message(message):
    bot.send_photo(message.chat.id, 'https://images.app.goo.gl/xodfjNtA22QmwCc67')


@bot.message_handler(commands=['start'])
def inline(message):
    markup = types.InlineKeyboardMarkup()
    
    github_button = types.InlineKeyboardButton(text='github', url='https://github.com')
    markup.add(github_button)
    
    balance_button = types.InlineKeyboardButton(text='balance', callback_data='balance')
    markup.add(balance_button)

    bot.send_message(message.chat.id, "Select", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: isinstance(call.data, str) and call.data == "balance")
def callback_handler(call):
  balance_keyboard = types.InlineKeyboardMarkup()

  button_1 = types.InlineKeyboardButton(text="Вывод",callback_data="withdraw")
  balance_keyboard.add(button_1)

  button_2 = types.InlineKeyboardButton(text="Пополнить",callback_data="deposit")
  balance_keyboard.add(button_2)

  bot.send_message(call.message.chat.id, "Select", reply_markup=balance_keyboard)
    
    
bot.polling()

