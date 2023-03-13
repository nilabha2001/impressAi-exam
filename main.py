
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton
bot=Bot(token="6093366391:AAGfDvAcI7iTVpVsoFexDIOCn4h20kQ1V-A")
dp=Dispatcher(bot)

button1=KeyboardButton('stupid')
button2=KeyboardButton('fat')
button3=KeyboardButton('dumb')
keyboard1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3)

@dp.message_handler()
async def kb_answer(message: types.Message):
    jokes = {
         'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                    """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
         'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                    """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
         }  
    if message.text == 'stupid':
        await message.random.choice(jokes['stupid'])
    elif message.text == 'fat':
        await message.random.choice(jokes['fat'])
    elif message.text == 'dumb':
        await message.random.choice(jokes['dumb'])
    



executor.start_polling(dp)
    
    
