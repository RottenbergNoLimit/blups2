import telebot
from telebot import types

# Zast¹p 'TOKEN' tokenem swojego bota
TOKEN = '6753585920:AAFI7Jfls5k41TKfDefUXA56xxlXC4OwjeE'
# Zast¹p 'YOUR_GROUP_CHAT_ID' id twojej grupy
GROUP_CHAT_ID = -1001995287586  # Znak minus przed numerem oznacza, ¿e to ID grupy

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    try:
        # Wysyłanie opisu bota
        description = "Yoo Bro... Do you know where is $DEV?."
        bot.send_message(chat_id, description)

        # Wysyłanie obrazka (tutaj mo¿na podaæ œcie¿kê do obrazka na serwerze)
        photo_url = 'https://i.postimg.cc/hGHbrZF3/msg-546443947-36271.jpg'
        bot.send_photo(chat_id, photo=photo_url, caption="Where are you $DEV?.")
    except Exception as e:
        print(f"Error in start handler: {e}")

@bot.message_handler(func=lambda message: message.chat.id == GROUP_CHAT_ID, content_types=['text'])
def check_message(message):
    text = message.text.lower()

    try:
        # Sprawdzanie, czy wiadomoœæ zawiera s³owo 'Dev'
        if 'dev' not in text:
            warning_message = "If the word 'dev' isn't in your message, it is not allowed here. You can get banned from the dev_bot.You Like or Not this Dev...give him SIMPLE follow"

            # Dodawanie przycisku "Follow Twitter"
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Follow Twitter", url="https://twitter.com/TWITTER_USERNAME")  # Zastąp 'TWITTER_USERNAME' swoim użytkownikiem na Twitterze
            keyboard.add(url_button)

            # Wysyłanie wiadomoœci z przyciskiem i dodatkowym tekstem
            bot.send_message(GROUP_CHAT_ID, f"{warning_message}\n\nLike or Not this Dev...give him follow!", reply_markup=keyboard)
    except Exception as e:
        print(f"Error in check_message handler: {e}")

if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error in polling: {e}")
