import telebot
from telebot import types

bot = telebot.TeleBot('1150292740:AAHPI8gkH1oMMISMJjl1ETgJWxcUgIdgzxU')


@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://itproger.com"))
	bot.send_message(message.chat.id,
			"Отличный выбор, нажмите на кнопку ниже и начинайте изучения курсов прямо сейчас",
			parse_mode='html', reply_markup=markup)


# @bot.message_handler(commands=['insta'])
# def instagram(message):
# 	markup = types.InlineKeyboardMarkup()
# 	markup.add(types.InlineKeyboardButton("test"))
# 	bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас", parse_mode='html', reply_markup=markup)


# @bot.message_handler(commands=['vk'])
# def vk(message):
# 	markup = types.InlineKeyboardMarkup()
# 	markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com/prog_life"))
# 	bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир IT прямо сейчас", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Отправление смс')
	btn2 = types.KeyboardButton('Некорректная тарификация')
	btn3 = types.KeyboardButton('Детализация ЛК')
	btn4 = types.KeyboardButton('Проверка ussd запроси')
	btn5 = types.KeyboardButton('Базовые станции')
	btn6 = types.KeyboardButton('Трафик интернета')
	markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nВыберите пункт ниже ?"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "начать тест заново":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Отправление смс')
		btn2 = types.KeyboardButton('Некорректная тарификация')
		btn3 = types.KeyboardButton('Детализация ЛК')
		btn4 = types.KeyboardButton('Проверка ussd запроси')
		btn5 = types.KeyboardButton('Базовые станции')
		btn6 = types.KeyboardButton('Трафик интернета')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "Решил попробовать что-то ещё? \nВыберите пункт ниже:"
	elif get_message_bot == "Отправление смс":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Поступил платеж 50с')
		btn2 = types.KeyboardButton('Ваш баланс 50с')
		btn3 = types.KeyboardButton('Ой! У вас заканчивается мб')
		btn4 = types.KeyboardButton('тест тест')
		btn5 = types.KeyboardButton("Начать тест заново")
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Отлично, геймдев крутая тема, но под что хочется разрабатывать?"
	elif get_message_bot == "Отправление смс":
    		markup = types.InlineKeyboardMarkup()
		# markup.add(types.InlineKeyboardButton("Посмотреть курсы по Unity", url="https://itproger.com/tag/unity"))
		# final_message = "Для разработки игр под мобильные устройства зачастую используется игровой движок <a href='https://itproger.com/tag/unity'>Unity</a>\nДвижок прост в изучении и вы можете просмотреть курсы по нему по кнопке ниже"
	# Здесь различные дополнительные проверки и условия
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Отправление смс')
		btn2 = types.KeyboardButton('Некорректная тарификация')
		btn3 = types.KeyboardButton('Детализация ЛК')
		btn4 = types.KeyboardButton('Проверка ussd запроси')
		btn5 = types.KeyboardButton('Базовые станции')
		btn6 = types.KeyboardButton('Трафик интернета')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		final_message = "Так \nOOOPS No connect to DB, Соглосуйтес с СБ для коннекта, ХАХА"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)