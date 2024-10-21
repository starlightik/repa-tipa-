import telebot


API_TOKEN = '7772555117:AAE6B3MuGyyrdlaQtNUd6QB39X6SmEixlzc'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    
    bot.reply_to(message, message.text)

print("Бот запущен...")
bot.polling(none_stop=True)