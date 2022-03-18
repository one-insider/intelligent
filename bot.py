import telebot
from telebot import types
import vk
import time

bot = telebot.TeleBot('5131645257:AAHyEawmAqAe-kDRi8l5GLZXk2ZAEiCTsFo')

stat = 'Не настроено'
forget = '..нет данных для вывода..'
mak = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, {user}!'.format(user = message.chat.username))
    global first
    first=message.message_id
    print(message.from_user)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'dokbaeb a ne info')

@bot.message_handler(commands=['text'])
def tem1(message):
    mesg = bot.send_message(message.chat.id,'Введите текст')
    bot.register_next_step_handler(mesg,tem2)
def tem2(message):
    bot.send_message(message.chat.id,'Текст принят')
    global forget
    forget=message.text
    print(message.text)

@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, 'Выберите что хотите узнать', reply_markup=main())

@bot.message_handler(commands=['clear'])
def clear(message):
    global first
    N=0
    print('______________')
    while message.message_id-N > first+1:
        try:
            bot.delete_message(message.chat.id, (message.message_id-N))
        except:
            print('Cyka')
        N = N + 1

@bot.message_handler(commands=['main'])
def main(message):
    bot.delete_message(message.chat.id, message.message_id)
    global mak
    mak=message.message_id+1
    bot.send_message(message.chat.id, 'Menu:', reply_markup=menu())
def menu():
    markup = types.ReplyKeyboardMarkup(True)
    key0 = types.KeyboardButton('Все данные')
    key1 = types.KeyboardButton('Мой текст')
    key2 = types.KeyboardButton('Инфа чата')
    key3 = types.KeyboardButton('Айди чата')
    key4 = types.KeyboardButton('От кого')
    key5 = types.KeyboardButton('5')
    markup.add(key0, key1)
    markup.add(key2, key3)
    markup.add(key4, key5)
    return markup


@bot.message_handler(content_types='text')
def otvet(message):
    global stat, mak
    if mak != 0:
        bot.delete_message(message.chat.id, mak)
        mak = 0
    if message.text == 'Вконтакте':
        bot.send_message(message.chat.id, message)
    elif message.text == 'М е н ю':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=main())
    elif message.text == 'Все данные':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Ваши данные:', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, message)
    elif message.text == 'Мой текст':
        bot.delete_message(message.chat.id, message.message_id)
        global forget
        bot.send_message(message.chat.id, 'Ваш текст: ' + forget, reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'Инфа чата':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Информация о чате:', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, message.chat)
    elif message.text == 'Айди чата':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Айди вашего чата: ' + str(message.chat.id), reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'От кого':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'От кого:', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, message.from_user)
    elif message.text == '5':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, message.chat, reply_markup=types.ReplyKeyboardRemove())

if __name__ == "__main__":
    print("Бот запущен")
    bot.polling(none_stop=True, interval=0)

#pyTelegramBotAPI 4.1.1
#vk_api 11.9.6
