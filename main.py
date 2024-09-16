import telegram
from datetime import datetime, timedelta
import requests

# Замените эту строку вашим токеном API
TOKEN = '7333081603:AAHraRdYrXn8IhgEnOwXmISh8K5uZfaBgGA'


def get_weather(city='Москва'):
    """Возвращает текущую погоду в городе."""
    api_url = f'https://api.openweathermap.org/data/2.5/onecall?lat=55.75&lon=37.62&exclude=current,minutely,hourly&units=metric&appid={YOUR_OPENWEATHERMAP_APPID}'

    response = requests.get(api_url)
    data = response.json()

    return data['daily'][0]


def send_message(bot, chat_id, message):
    bot.send_message(chat_id, message)


def main():
    # Создаем объект для общения с ботом
    bot = telegram.Bot(token=TOKEN)

    # Получаем список чатов, к которым привязан бот
    bot_chats = bot.get_chat_list()

    for chat in bot_chats:
        if not chat.type == 'private':
            continue

        chat_id = chat.id
        first_name = chat.first_name

        print('Начало отправки сообщений для пользователя', first_name)

        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        day_after_tomorrow = today + timedelta(days=2)

        weather_today = get_weather()
        weather_tomorrow = get_weather(city=weather_today['city']['name'])
        weather_day_after_tomorrow = get_weather(city=weather_tomorrow['city']['name'])

        message_today = f'Сегодня в {weather_today["city"]["name"]} ожидается {weather_today["temp"]["day"]}°C'
        message_tomorrow = f'Завтра в {weather_tomorrow["city"]["name"]} ожидается {weather_tomorrow["temp"]["day"]}°C'
        message_day_after_tomorrow = f'Послезавтра в {weather_day_after_tomorrow["city"]["name"]} ожидается {weather_day_after_tomorrow["temp"]["day"]}°C'

        send_message(bot, chat_id, message_today)
        send_message(bot, chat_id, message_tomorrow)
        send_message(bot, chat_id, message_day_after_tomorrow)


if __name__ == '__main__':
    main()
