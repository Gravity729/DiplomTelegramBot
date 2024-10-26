import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


bot = telebot.TeleBot('7367162278:AAFoec1gXlLQipauMQKUp01tlO-EpILWjbA')

# Создаем команду "start"
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup(row_width=2)  # Указываем количество кнопок в ряду
    keyboard.add(
        InlineKeyboardButton("YouTube", url="https://youtube.com/@dashamolk?si=wa1sqAsso4ZmCfOl"),
        InlineKeyboardButton("VK", url="https://vk.com/club222319967"),
        InlineKeyboardButton("Telegram", url="https://t.me/sport_Molkova"),
        InlineKeyboardButton("Instagram", url="https://www.instagram.com/dashamolk?igsh=aXlyZGg4d3docDNq&utm_source=qr")
    )

    text = """
Всем привет! Меня зовут Дарья Молькова, и я ваш персональный тренер! 💪

Я помогу вам достичь ваших фитнес-целей и стать лучшей версией себя!  

В моих соц.сетях вы найдете полезные советы по тренировкам, мотивацию и вдохновение, а также много интересного контента. 

Подписывайтесь и следите за обновлениями!

Мои соц.сети:
    """

    # Отправляем фото с сообщением
    with open('photo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text, reply_markup=keyboard)

# Команда для запуска магазина в Web App
@bot.message_handler(commands=['shop'])
def shop(message):
    # Обновленный URL для Cloudflare Tunnel
    web_app_url = "https://packed-pb-teachers-friends.trycloudflare.com"  # Cloudflare URL без /index.html
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Открыть магазин", web_app=WebAppInfo(url=web_app_url))
    )
    bot.send_message(message.chat.id, "Откройте магазин, чтобы выбрать курс:", reply_markup=keyboard)


# Запуск бота
bot.polling()
