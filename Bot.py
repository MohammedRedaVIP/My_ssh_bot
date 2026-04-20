import telebot

# استبدل الكلمة اللي تحت بالتوكن بتاعك من BotFather
TOKEN = '8712559445:AAHeON_omFsjnEaTt_S4HWkyO9L5w6rXmI0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك يا صديقي! أنا بوت إنشاء حسابات SSH مجانية.\n\nدوس على /create عشان أبعتلك روابط السيرفرات الجاهزة.")

@bot.message_handler(commands=['create'])
def create(message):
    text = (
        "اختار السيرفر اللي يعجبك واعمل حسابك في ثواني:\n\n"
        "1️⃣ سيرفر مصر: https://sshs8.com/create-ssh/egypt\n"
        "2️⃣ سيرفر سنغافورة: https://sshs8.com/create-ssh/singapore\n\n"
        "بعد ما تعمل الحساب، خد البيانات وحطها في HTTP Custom."
    )
    bot.send_message(message.chat.id, text)

bot.polling()
