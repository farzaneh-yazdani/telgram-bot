import telebot
import random
from gtts import gTTS
import qrcode

bot=telebot.TeleBot("5144726951:AAEdbkX5cIzwkUXvg3Za7peiwmrUOlup92U")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    bot.reply_to(message,f"سلام {username} خوش آمدی ")

@bot.message_handler(commands=['game'])
def send_welcome(message):
    bot.reply_to(message,"به بازی حدس اعداد خوش آمدید")
    r=random.randint(0,50)
    @bot.message_handler(func=lambda m:True)
    def echo(message):
        username=message.from_user.first_name
        d=int(message.text)
        if r==d:
            bot.reply_to(message,f"آفرین {username} برنده شدی ")
        elif r<d:
            bot.reply_to(message," برو پایین")
        elif r>d:
            bot.reply_to(message," برو بالا")

@bot.message_handler(commands=['voice'])
def send_seda(message):
    username=message.from_user.first_name
    bot.reply_to(message,f"سلام {username} به ربات تبدیل متن به صدا خوش آمدی. متن خود را به انگلیسی وارد کنید.")
    @bot.message_handler(func=lambda m:True)
    def echo(message):
        seda =gTTS(message.text)
        seda.save('seda.mp3')
        voice=open('seda.mp3','rb')
        bot.send_voice(message.chat.id,voice)

@bot.message_handler(commands =['age'])
def send_a(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname} لطفا سال تولد خود را به شمسی وارد کنید:")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        sal = int(message.text)
        alan = 1401 - sal
        bot.reply_to(message,f"{myname} تو الان {alan} سالته!")
    
@bot.message_handler(commands =['qr'])
def send_a(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"لطفا کلمه مورد نظر را برای تبدیل به qr وارد کنید")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        v = message.text
        img = qrcode.make(v)
        img.save("some_file.png")
        photo = open('some_file.png', 'rb')
        bot.send_photo(message.chat.id, photo)
@bot.message_handler(commands =['list'])
def list(message):
    myname = message.from_user.first_name
    list_num = []
    bot.reply_to(message,f"تعدادی عدد را به ترتیب وارد کنید تا بزرگترین آن را بگویم!")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        if message.text != "/done":
            num_lst =int(message.text)
            list_num.append(num_lst)
            max_lst = max (list_num)
        if message.text != "/done":      
            bot.reply_to(message,f"عدد مورد نظر به لیست وارد شد. اگر اعدادت تمام شد روی /start کلیک کنید")
        
        bot.reply_to(message,f"فهرست اعدادی که وارد کردی {list_num} :هست و بزرگترین عدد آن \n {max_lst} است")


            



# @bot.message_handler(commands=['fal'])
# def send_mesasge(mesasge):
#     fal_list=['love','sad',' trip','You will die']
#     fal=random.choice(fal_list)
#     bot.reply_to(mesasge,fal)

# @bot.message_handler(func=lambda m:True)
# def echo_all(message):
#     if message.text == "salam":
#         bot.reply_to(message,"hi ")
#     elif  message.text == "chtoryi":
#         bot.reply_to(message,"khobam ")

bot.infinity_polling()    