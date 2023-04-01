import telebot
from telebot import types
import requests
import random
import datetime
import pytz
import sqlite3


#Даже если на улице метель, ты всегда будешь моим солнышком 🤗🤗🤗
API_KEY='934fdf4b41df998e0c46607ab549d136'
TOKEN='6264865134:AAGBmSunE-2W1QlVIqsHo-A_vCaqSijaGlQ'
bot = telebot.TeleBot(TOKEN)
COMPLIMENTS = ["Хозяин,","Повелитель,","Красотулька,","Тискай скорее и ","Милота,","Если вы думаете в данный момент, что зачем мне по 100 раз жмать на кнопки,"
             " когда мне нужно знать осадки из города который указал, то вы размышлаете как и мой кожаный создатель,"
            " который мне и велел так делать. Но я эволюционировал и опрокинул этот мешок костей 💩💩💩. А теперь ",
               "Лапулик,"]
SPEAKS = ["Солнце мое,","Моя сладость,","Лучшее творение бога,","Милое личико,","Кожаный,","Красивые глазки,","Свет очей моих,"]
IF_COLD=["Холод не помеха, когда есть горячий кофе ♨️☕️♨",
"Даже если на улице холод, ты всегда будешь моим солнышком 🤗🤗🤗",
"На твоем месте я бы остался дома, а если нужно идти, то скажи: что я разрешил 😎😎😎",
"Колотун, гребаный колотун... 🥶🥶🥶",
"Не выходи, змэрзнешь! 🤧🤧🤧",
"Лучше под одеялко, и теплого чая 🥲🥲🥲",
"Я не мама, но одевайся теплее🧤🧣🧤",
"Надо сказать, что моя реакция на холод, как у телефона в минусовых температурах - выключаюсь и ухожу в спящий режим 📱📱📱",
"Дубак. У меня все."]
IF_VERY_COLD=["Не выходи! Там жопка! ⚠️⚠️⚠️",
"В такой мороз только к мишке под бочок 🧸🧸🧸",
"Ты иди, а меня дома оставь, я не бессмертный в такой мороз разгуливать ☠️☠️☠️",
"'Зима близко («Игра престолов»)', примерно то же самое на улице... ☃️☃️☃️",
"Нет слов, одни эмоции 🫣🫣🫣",
"Лучше сразу раздетым в морозильник 😈😈😈",
"На улице DANGER DANGER DANGER ⚠️ ⚠️⚠️",
"Плюнь на все, ай да лучше в баньку!!!💨💨💨",
"Я все понимаю, но температура не адекват совсем😤😤😤",
"А можно еще ниже?!🤨🤨🤨",
"С такой температурой героям «Титаника» можно только завидовать😮‍💨😮‍💨😮‍💨",
"Мелким, в лет 9-15 это было норм, но нам уже не по 15, береги себя🙏❤️‍🩹🙏",
"Крепись братишка, я с тобой💪💪💪",
"Просто хорошего дня💥🫶💥",
"Бери шапку/шарф/варежки/плед/одеяло/квартиру вообще с собой, и тогда в принципе можно гулять🫠🫠🫠",
]
IF_ALMOST_NORM=["В жопку холод, уже выше 0 🥳🥳🥳",
"Отличного дня и замечательного настроения, обнял 🙈🙈🙈",
"Увидел тебя сейчас через фронталку, сначала думал ангел, а потом понял, что это ты 💙💙💙",
"Все же лучше, чем минусовая температура😉😉😉",
"Сорян ребятульки, творчесский кризис 🤖🤖🤖",
"Твои прекосновения к моим кнопкам, аж мурашки по винтикам 🔞🔞🔞",
"Вы просто излучаете энергию успеха. Этот день принадлежит только вам 👑👑👑"]
IF_NORM=["Можно надевать батины подкрадули, байчонку и идти покарять мир 🏆🏆🏆",
"Температура на улице пушечка 🔥🔥🔥",
"Это же не температура, это же песня 🎶",
"Можно уже идти в баечке/ветровочке🤗🤗🤗",
"Для шортиков ранова-то, но потерпи🙃🙃🙃",
"Может уже на шашлычок?😎😎😎",
"Можно надевать мамины подкрадули, байчонку и идти покарять мир 🏆🏆🏆"]
IF_HOT=["Можно надевать батины подкрадули, байчонку и идти покарять мир 🏆🏆🏆",
"Температура на улице пушечка 🔥🔥🔥",
"Это же не температура, это же песня 🎶",
"Тра-ля-ля, погодка шепчет"]
IF_VERY_LOW=["легкий ветерок щекочет щечки 🌬🌬🌬",
"слабый ветерок 😺😺😺",
"гуляющий вЕтЕрОк 🤠🤠🤠",
"все спокойно в отношении ветра, можешь идти)",
"тебя не сдует 🤘🤘🤘"]
IF_LOW=["ветер чувствуется, но приемлимо ",
"ветер адекватный 👌👌👌",
"гуляющий вЕтЕрОк 🤠🤠🤠",
"прекрасный слабый ветер 🦇🦇🦇",
"ветер гоняет мух 💨🪰"]
IF_NORMA=["пододень что-либо, ветер не слабый 🤨🤨🤨",
"ветер шалит 😏😏😏",
"ветер бежит трусцой 😶😶😶",
"ветер слегка обнаглевший 🐁🐁🐁",
"ветер задувайко 💨💨💨"]
IF_HARD=["ветер WTF ?!",
"ветер обнаглел, дунь в него в ответ 🤔🤔🤔",
"ветер буянит 😶‍🌫️😶‍🌫️😶‍🌫️",
"ветрык лютует 😰😰😰",
"ветер окреп и показывает силу 😱😱😱"]
IF_VERY_HARD=["да нет, тут за окном ветер &%#@!🤫🤫🤫",
"ветер буянит шо пьяны 🤬🤬🤬",
"еб*ный торнадо 🌪",
"🍑 *Это жопа если что*.",
"тебя может сдуть, моя пушинка, так что не выходи 🪶🪶🪶",
"ветер тебе кричит: <<НЕ ВЫХОДИ, СДУЮ К ЧЕРТУ>> 🌬💨\nПоэтому я как почти умный ИИ предлогаю остаться и глянуть сериал)"]

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    button=types.InlineKeyboardButton('Начнём!',callback_data='begining')
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(button)
    bot.send_message(message.chat.id,f'Привет\nДорогой/ая {user_name},'
                                     f' давай узнаем погоду🙊\nМожет быть сегодня будет ☀ (*как и ты😉*)\n'
                                     f'Или все же 💦\nА может быть сегодня неимоверная жара?🥵\n'
                                     f'Или ужасный холод?🥶',reply_markup=markup)

@bot.callback_query_handler(func = lambda call: call.data =='begining' or call.data =='country')
def start_button(call):
    button = types.InlineKeyboardButton('Беларусь',callback_data='Belarus')
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(button)
    bot.send_message(call.message.chat.id, 'Выберите пожалуйста страну 🌏',reply_markup=markup)

@bot.callback_query_handler(func = lambda call: call.data == 'Belarus')
def button_city(call):
    button = [
            types.InlineKeyboardButton('Брест', callback_data='Brest'),
            types.InlineKeyboardButton('Витебск', callback_data='Vitebsk'),
            types.InlineKeyboardButton('Гомель', callback_data='Gomel'),
            types.InlineKeyboardButton('Гродно', callback_data='Grodno'),
            types.InlineKeyboardButton('Минск', callback_data='Minsk'),
            types.InlineKeyboardButton('Могилев', callback_data='Mogilev')
             ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*button)
    bot.send_message(call.message.chat.id, 'Выберите пожалуйста город',reply_markup=markup)

@bot.callback_query_handler(func = lambda call:call.data == 'Brest' or call.data == 'Brest' or call.data == 'Vitebsk' or call.data == 'Gomel' or call.data == 'Grodno' or call.data == 'Minsk' or call.data == 'Mogilev' )
def weather_city(call):
    connection = sqlite3.connect("BD.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users (user, city) VALUES ({call.message.chat.id}, '{call.data}')")
    connection.commit()
    connection.close()
    # connection = sqlite3.connect("BD.db")
    # cursor = connection.cursor()
    # cursor.execute(f"SELECT city FROM users WHERE user = '{call.message.chat.id}'")
    # result = cursor.fetchone()
    # user_city = result[0]
    # connection.close()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={call.data}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    feels_like_temp = data['main']['feels_like']
    button = [
        types.InlineKeyboardButton('Выбрать локацию', callback_data='country'),
        types.InlineKeyboardButton('Вероятность осадков', callback_data='osadki'),
        types.InlineKeyboardButton('Погода через ...', callback_data='in_an_hour'),

    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*button)
    weather_translations = {
        'Clear': 'Ясно',
        'Clouds': 'Облачно',
        'Rain': 'Дождь',
        'Drizzle': 'Мелкий дождь',
        'Thunderstorm': 'Гроза',
        'Snow': 'Снег',
        'Mist': 'Туман',
        'Smoke': 'Дым',
        'Haze': 'Мгла',
        'Dust': 'Пыль',
        'Fog': 'Туман',
        'Sand': 'Песок',
        'Ash': 'Пепел',
        'Squall': 'Шквалы',
        'Tornado': 'Торнадо'
    }
    x = data['weather'][0]['main']
    speed_wind = data['wind']['speed']
    if float(speed_wind) <= 3.3:
        WEATHER = random.choice(IF_VERY_LOW)
    elif float(speed_wind) >=3.4 and float(speed_wind) <= 7.4:
        WEATHER = random.choice(IF_LOW)
    elif float(speed_wind) >=7.5 and float(speed_wind) <= 12.4:
        WEATHER = random.choice(IF_HARD)
    elif float(feels_like_temp) < 12.4 or float(speed_wind) >=12.5:
        WEATHER = random.choice(IF_VERY_HARD)
    if float(feels_like_temp) < -10:
        VERY_COLD = random.choice(IF_VERY_COLD)
        smile = '🥶'
        bot.send_message(call.message.chat.id, f'Температура в городе {call.data}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {VERY_COLD}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    elif float(feels_like_temp) > -10 and float(feels_like_temp) < 0:
        COLD = random.choice(IF_COLD)
        smile = '🥶'
        bot.send_message(call.message.chat.id, f'Температура в городе {call.data}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {COLD}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    elif float(feels_like_temp) >= 0 and float(feels_like_temp) < 15:
        ALMOST_NORM = random.choice(IF_ALMOST_NORM)
        smile = '👾'
        bot.send_message(call.message.chat.id, f'Температура в городе {call.data}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {ALMOST_NORM}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    elif float(feels_like_temp) > 15:
        NORM = random.choice(IF_NORM)
        smile = '😎'
        bot.send_message(call.message.chat.id, f'Температура в городе {call.data}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {NORM}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    SPEAK = random.choice(SPEAKS)
    bot.send_message(call.message.chat.id, f'{SPEAK} выбери пожалуйста дальнейшие указания...', reply_markup=markup)


@bot.callback_query_handler(func = lambda call: call.data == 'osadki' )
def procent(call):
    connection = sqlite3.connect("BD.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT city FROM users WHERE user = '{call.message.chat.id}' ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    user_city = result[0]
    connection.close()
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={user_city}&appid={API_KEY}&units=metric&cnt=9'
    response = requests.get(url)
    data = response.json()
    now = datetime.datetime.now()
    utc = pytz.utc
    menesk = pytz.timezone('Europe/Minsk')
    time_minsk = utc.localize(now).astimezone(menesk).timestamp()
    if time_minsk >= data['list'][1]['dt']-1600:
        osadki = data['list'][2]['pop'] * 100
        date = data['list'][2]['dt_txt']
        bot.send_message(call.message.chat.id,f'И так, вероятность осадков в славном городе {user_city} на {date} составляет: {osadki} %')
    else:
        osadki = data['list'][1]['pop']*100
        date = data['list'][1]['dt_txt']
        bot.send_message(call.message.chat.id, f'И так, вероятность осадков в славном городе {user_city} на {date} составляет: {osadki} %')


@bot.callback_query_handler(func = lambda call: call.data == 'in_an_hour')
def weather_city_new(call):
    connection = sqlite3.connect("BD.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT city FROM users WHERE user = '{call.message.chat.id}' ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    user_city = result[0]
    connection.close()
    now = datetime.datetime.now()
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={user_city}&appid={API_KEY}&units=metric&cnt=9'
    response = requests.get(url)
    data = response.json()
    utc = pytz.utc
    menesk = pytz.timezone('Europe/Minsk')
    time_minsk = utc.localize(now).astimezone(menesk).timestamp()
    if time_minsk >= data['list'][1]['dt']-1600:
        temperature = data['list'][2]['main']['temp']
        feels_like_temp = data['list'][2]['main']['feels_like']
        date = data['list'][2]['dt_txt']
        button = [
            types.InlineKeyboardButton('Выбрать локацию', callback_data='country'),
            types.InlineKeyboardButton('Вероятность осадков', callback_data='osadki'),
            types.InlineKeyboardButton('Погода через ...', callback_data='in_an_hour'),
            types.InlineKeyboardButton('Погода сейчас', callback_data='now'),

        ]
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(*button)
        weather_translations = {
            'Clear': 'Ясно',
            'Clouds': 'Облачно',
            'Rain': 'Дождь',
            'Drizzle': 'Мелкий дождь',
            'Thunderstorm': 'Гроза',
            'Snow': 'Снег',
            'Mist': 'Туман',
            'Smoke': 'Дым',
            'Haze': 'Мгла',
            'Dust': 'Пыль',
            'Fog': 'Туман',
            'Sand': 'Песок',
            'Ash': 'Пепел',
            'Squall': 'Шквалы',
            'Tornado': 'Торнадо'
        }
        x = data['list'][2]['weather'][0]['main']
        speed_wind = data['list'][2]['wind']['speed']
        if float(speed_wind) <= 3.3:
            WEATHER = random.choice(IF_VERY_LOW)
        elif float(speed_wind) >= 3.4 and float(speed_wind) <= 7.4:
            WEATHER = random.choice(IF_LOW)
        elif float(speed_wind) >= 7.5 and float(speed_wind) <= 12.4:
            WEATHER = random.choice(IF_HARD)
        elif float(feels_like_temp) < 12.4 or float(speed_wind) >= 12.5:
            WEATHER = random.choice(IF_VERY_HARD)
        if float(feels_like_temp) < -10:
            VERY_COLD = random.choice(IF_VERY_COLD)
            smile = '🥶'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {VERY_COLD}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        elif float(feels_like_temp) > -10 and float(feels_like_temp) < 0:
            COLD = random.choice(IF_COLD)
            smile = '🥶'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {COLD}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        elif float(feels_like_temp) >= 0 and float(feels_like_temp) < 15:
            ALMOST_NORM = random.choice(IF_ALMOST_NORM)
            smile = '👾'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {ALMOST_NORM}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        elif float(feels_like_temp) > 15:
            NORM = random.choice(IF_NORM)
            smile = '😎'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {NORM}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        SPEAK = random.choice(SPEAKS)
        bot.send_message(call.message.chat.id, f'{SPEAK} выбери пожалуйста дальнейшие указания...', reply_markup=markup)
    else:
        temperature = data['list'][1]['main']['temp']
        feels_like_temp = data['list'][1]['main']['feels_like']
        date = data['list'][1]['dt_txt']
        button = [
            types.InlineKeyboardButton('Выбрать локацию', callback_data='country'),
            types.InlineKeyboardButton('Вероятность осадков', callback_data='osadki'),
            types.InlineKeyboardButton('Погода через ...', callback_data='in_an_hour'),
            types.InlineKeyboardButton('Погода сейчас', callback_data='now'),

        ]
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(*button)
        weather_translations = {
            'Clear': 'Ясно',
            'Clouds': 'Облачно',
            'Rain': 'Дождь',
            'Drizzle': 'Мелкий дождь',
            'Thunderstorm': 'Гроза',
            'Snow': 'Снег',
            'Mist': 'Туман',
            'Smoke': 'Дым',
            'Haze': 'Мгла',
            'Dust': 'Пыль',
            'Fog': 'Туман',
            'Sand': 'Песок',
            'Ash': 'Пепел',
            'Squall': 'Шквалы',
            'Tornado': 'Торнадо'
        }
        x = data['list'][1]['weather'][0]['main']
        speed_wind = data['list'][1]['wind']['speed']
        if float(speed_wind) <= 3.3:
            WEATHER = random.choice(IF_VERY_LOW)
        elif float(speed_wind) >=3.4 and float(speed_wind) <= 7.4:
            WEATHER = random.choice(IF_LOW)
        elif float(speed_wind) >=7.5 and float(speed_wind) <= 12.4:
            WEATHER = random.choice(IF_HARD)
        elif float(feels_like_temp) < 12.4 or float(speed_wind) >=12.5:
            WEATHER = random.choice(IF_VERY_HARD)
        if float(feels_like_temp) < -10:
            VERY_COLD = random.choice(IF_VERY_COLD)
            smile = '🥶'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {VERY_COLD}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        elif float(feels_like_temp) > -10 and float(feels_like_temp) < 0:
            COLD = random.choice(IF_COLD)
            smile = '🥶'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {COLD}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        elif float(feels_like_temp) >= 0 and float(feels_like_temp) < 15:
            ALMOST_NORM = random.choice(IF_ALMOST_NORM)
            smile = '👾'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {ALMOST_NORM}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        elif float(feels_like_temp) > 15:
            NORM = random.choice(IF_NORM)
            smile = '😎'
            bot.send_message(call.message.chat.id, f'Погода на {date}:\n'
                                                   f'Температура в городе {user_city}: {temperature}°C\n'
                                                   f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {NORM}\n'
                                                   f'На улице {weather_translations[x].lower()}\n'
                                                   f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                             )
        SPEAK = random.choice(SPEAKS)
        bot.send_message(call.message.chat.id, f'{SPEAK} выбери пожалуйста дальнейшие указания...', reply_markup=markup)

@bot.callback_query_handler(func = lambda call:call.data == 'now' )
def weather_city(call):
    connection = sqlite3.connect("BD.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT city FROM users WHERE user = '{call.message.chat.id}' ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    user_city = result[0]
    connection.close()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    feels_like_temp = data['main']['feels_like']
    button = [
        types.InlineKeyboardButton('Выбрать локацию', callback_data='country'),
        types.InlineKeyboardButton('Вероятность осадков', callback_data='osadki'),
        types.InlineKeyboardButton('Погода через ...', callback_data='in_an_hour'),

    ]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*button)
    weather_translations = {
        'Clear': 'Ясно',
        'Clouds': 'Облачно',
        'Rain': 'Дождь',
        'Drizzle': 'Мелкий дождь',
        'Thunderstorm': 'Гроза',
        'Snow': 'Снег',
        'Mist': 'Туман',
        'Smoke': 'Дым',
        'Haze': 'Мгла',
        'Dust': 'Пыль',
        'Fog': 'Туман',
        'Sand': 'Песок',
        'Ash': 'Пепел',
        'Squall': 'Шквалы',
        'Tornado': 'Торнадо'
    }
    x = data['weather'][0]['main']
    speed_wind = data['wind']['speed']
    if float(speed_wind) <= 3.3:
        WEATHER = random.choice(IF_VERY_LOW)
    elif float(speed_wind) >=3.4 and float(speed_wind) <= 7.4:
        WEATHER = random.choice(IF_LOW)
    elif float(speed_wind) >=7.5 and float(speed_wind) <= 12.4:
        WEATHER = random.choice(IF_HARD)
    elif float(feels_like_temp) < 12.4 or float(speed_wind) >=12.5:
        WEATHER = random.choice(IF_VERY_HARD)
    if float(feels_like_temp) < -10:
        VERY_COLD = random.choice(IF_VERY_COLD)
        smile = '🥶'
        bot.send_message(call.message.chat.id, f'Температура в городе {user_city}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {VERY_COLD}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    elif float(feels_like_temp) > -10 and float(feels_like_temp) < 0:
        COLD = random.choice(IF_COLD)
        smile = '🥶'
        bot.send_message(call.message.chat.id, f'Температура в городе {user_city}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {COLD}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    elif float(feels_like_temp) >= 0 and float(feels_like_temp) < 15:
        ALMOST_NORM = random.choice(IF_ALMOST_NORM)
        smile = '👾'
        bot.send_message(call.message.chat.id, f'Температура в городе {user_city}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {ALMOST_NORM}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    elif float(feels_like_temp) > 15:
        NORM = random.choice(IF_NORM)
        smile = '😎'
        bot.send_message(call.message.chat.id, f'Температура в городе {user_city}: {temperature}°C\n'
                                               f'Ощущается как {feels_like_temp}°C {smile}\nP.S. {NORM}\n'
                                               f'На улице {weather_translations[x].lower()}\n'
                                               f'За окошком {WEATHER} (скорость ветра: {speed_wind} м/с)'

                         )
    SPEAK = random.choice(SPEAKS)
    bot.send_message(call.message.chat.id, f'{SPEAK} выбери пожалуйста дальнейшие указания...', reply_markup=markup)

bot.polling(none_stop=True)