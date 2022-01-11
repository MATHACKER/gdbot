api = "b525c151af1c44ad5bf9fed2d23bd4800ede31d70afe68f91ef89fd87c0a775601d5b6594099866bef15b"

from vkbottle.bot import Bot, Message
from vkbottle import  BaseStateGroup, PhotoMessageUploader, DocMessagesUploader, VoiceMessageUploader, CtxStorage, Keyboard, Callback, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, GroupEventType, VKAPIError
from vkbottle.modules import json
from vkbottle_types import GroupTypes
bot = Bot(token=api)
from PIL import Image, ImageDraw, ImageFont
from random import randint
import time
import textwrap
import re
import pickle
import json

print('Запущен')

def write(data, filename):
	data = json.dumps(data)
	data = json.loads(str(data))
	with open(filename, 'w', encoding = 'utf-8') as file:
		json.dump(data, file, indent = 4)









command = {}

def read(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		return json.load(file)




@bot.on.chat_message(action=["chat_invite_user", "chat_invait_user_by_link"])
async def invite(message:Message):
	if message.action.member_id == -208980739:
			await message.answer("👋 Привет! Это DBot!\n🔱 Для полноценной работы бота, выдайте мне права администратора!")






'''
@bot.on.message(text="привет")
async def handler(message:Message):
	keyboardy = (
		Keyboard()
		.add(Callback("HELLO", {"cmd":"hello"}))
		.add(Callback("HELLO 2", {"cmd":"hello2"}))
		)
	await message.answer("callback button", keyboard=keyboardy)

@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def message_event_handler(event:GroupTypes.MessageEvent):
	if event.object.payload["cmd"] == "hello":
		await bot.api.messages.send_message_event_answer(
			event_id=event.object.event_id,
			peer_id=event.object.peer_id,
			user_id=event.object.user_id,
			event_data=json.dumps({"type":"show_snackbar", "text":"test message"})
			)
	elif event.object.payload["cmd"] == "hello2":
		await bot.api.messages.send_message_event_answer(
			event_id=event.object.event_id,
			peer_id=event.object.peer_id,
			user_id=event.object.user_id,
			event_data=json.dumps({"type":"show_snackbar", "text":"new message"})
			)
'''








#https://yandex.ru/images/search?text=%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5&from=tabbar&p=1&pos=34&rpt=simage&img_url=https%3A%2F%2Fhddesktopwallpapers.in%2Fwp-content%2Fuploads%2F2015%2F09%2Fleopard-art.jpg
@bot.on.message()
async def message_handler(message:Message):
	if message.text.lower().startswith("/цитата") or message.text.lower().startswith("цитата"):
		user = await bot.api.users.get(message.from_id)
		await message.answer("Ожидайте...")
		citata = message.text.split()
		citata.pop(0)
		img = Image.open('фон_3_новый.QFSqF.jpg')
		idraw = ImageDraw.Draw(img)
		headline = ImageFont.truetype('arial.ttf', size=52)
		text_font = ImageFont.truetype('arial.ttf', size=35)
		name_font = ImageFont.truetype('arial.ttf', size=38)
		citata_new = ' '.join(citata) + '»'
		head = "Цитаты великих людей"
		citata_new_2 = '«' + citata_new[:37] + '\n' + citata_new[37:]
		first_name_users = "© " + user[0].first_name
		last_name_users = user[0].last_name
		idraw.text((130, 55), head, font=headline)
		idraw.text((130, 152), str(citata_new_2), font=text_font)
		idraw.text((130, 255), str(first_name_users) + " " + str(last_name_users), font=name_font)
		img.save('citata.png')
		vk_cita = PhotoMessageUploader(bot.api)
		photo_cita_vk = await vk_cita.upload("citata.png")
		await message.answer("💬 Ваша цитата готова!", attachment=photo_cita_vk)
	#рандом
	elif message.text.lower().startswith("/рандом") or message.text.lower().startswith("рандом"):
		try:
			ot = int(message.text.split()[1])
			do = int(message.text.split()[2])
			otdo = randint(ot, do)
			imgRandom = Image.open('random.jpg')
			idrawRandom = ImageDraw.Draw(imgRandom)
			idrawRandom = ImageDraw.Draw(imgRandom)
			headlineRandom = ImageFont.truetype('arial.ttf', size=150)
			text_fontRandom = ImageFont.truetype('arial.ttf', size=300)
			headRandom = "Рандомное число:"
			idrawRandom.text((50, 600), headRandom, font=headlineRandom)
			idrawRandom.text((1335, 470), str(otdo), font=text_fontRandom)
			imgRandom.save('random_1.jpg')
			vk_random = PhotoMessageUploader(bot.api)
			photo_random_vk = await vk_random.upload("random_1.jpg")
			await message.answer(attachment=photo_random_vk)
		except (ValueError, IndexError):
			await message.answer("Отправьте по заданному образцу: \nРандом (число от) (число до)")
	#спам
	elif message.text.lower().startswith("/спам"):
		id_vk = str(message.text.split()[1])
		kolvo_spam = int(message.text.split()[2])
		try:
			text_spam = re.findall(rf'{message.text.split()[2]} (.*?);',message.text)
			text_spam = ''.join(text_spam) 
		except:
			for spam in range(kolvo_spam):
				time.sleep(1)
				await message.answer(id_vk + " На вас заказали спам атаку! ")
		for spam in range(kolvo_spam):
			time.sleep(1)
			await message.answer(id_vk + " "+  text_spam)
	#конструктор
	elif message.text.startswith("Если сообщение равно") or message.text.startswith("/Если сообщение равно"):
		global keys
		global value
		global command
		keys= re.findall(r'равно (.*?) отправить',message.text)
		keys = ''.join(keys).lower()
		value = re.findall(r'текст (.*?);',message.text)
		value = ''.join(value)
		command[keys] = value
		global com_new
		com_new = read('command.json')
		comand_js_new = {**command, **com_new}
		write(comand_js_new, 'command.json')
		global command_new
		command_new = read('command.json')
		await message.answer("Комманда успешно создана: \nif message.text ==" + keys + ":\n    await message.answer(" + command[keys] + ")")
	elif message.text.lower() in command_new: 
		print(message.text.lower())
		await message.answer(command_new[message.text.lower()])
		
command_new = read('command.json')



'''
@bot.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def groupjoin_handler(event: GroupTypes.GroupJoin):
	try:
		await bot.api.messages.send(
			peer_id=event.object.user_id,
			message="Спасибо, что подписался!",
			random_id=0
			)
	except VKAPIError(901):
		pass

@bot.on.raw_event(GroupEventType.GROUP_LEAVE, dataclass=GroupTypes.GroupLeave)
async def groupleave_handler(event: GroupTypes.GroupLeave):
	try:
		await bot.api.messages.send(
			peer_id=event.object.user_id,
			message="Плак...",
			random_id=0
			)
	except VKAPIError(901):
		pass
'''
bot.run_forever()