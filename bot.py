import telebot

bot = telebot.TeleBot('your key')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, "Enter your mathematical expression. For exampele 2 + 44  \n or 5 / 5 * 888 + 2 - 50 \n", parse_mode='html')
 
          
@bot.message_handler()
def get_user_text(message):
 try:
   
  i = -1
  limit = len(message.text)
  s = message.text
  num = ""
  while i < limit - 1:
    i+=1
    if s[i] == '=':
        continue
    else:
        num += s[i]

  bot.send_message(message.chat.id, eval(num), parse_mode='html')
 
 except:
    bot.send_message(message.chat.id, "error", parse_mode='html')


bot.polling(none_stop=True)