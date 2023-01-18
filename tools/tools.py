# -*- coding: utf-8 -*-

# Tools for different processing

import requests as r, os, time, random, shutil, zipfile,webbrowser
from progress.bar import ChargingBar
from tools import sender as send
from termcolor import colored
from datetime import datetime
from sys import platform
from tools import proxy

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # For Russia
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # For Belarus
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
			numb_4 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] + '-' + numb[9:11] + '-' + numb[11:13]
			numb_5 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] +numb[9:11] +numb[11:13]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]
			numb_4 = '+' + numb[:3] + ' (' + numb[3:5] + ") " + numb[5:8] + '-' + numb[8:10] + '-' + numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10

def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def anim_text(text, speed, color="magenta"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def banner_tools():
	print(colored("[1]", "red"), colored("Начать спам", "magenta"))
	print(colored("[2]", "red"), colored("FAQ Про прокси", "magenta"))
	print(colored("[3]", "red"), colored("Краткое руководство проблем", "magenta"))
	print(colored("[4]", "red"), colored("Отказ от ответственности", "magenta"))
	print(colored("[5]", "red"), colored("Поддержать донатом", "magenta"))
	print(colored("[6]", "red"), colored("Информация", "magenta"))
	print(colored("\n[0] Выход", "red"))

def quick_guide():
	clear()
	print("")
	print(colored("В нашем бомбере спам может постепенно ухудшаться из-за того что на один и тот же номер поступает очень много запросов на отправку смс.", "magenta"))
	print(colored("Не пытайтесь оставить спам на всю ночь на один и тот же номер, вы просто заставите сервисы заблокировать данный номер у себя в базе и никакие прокси тут уже не помогут.", "magenta"))
	print(colored("Достаточно 2-3 круга на один номер раз в сутки чтобы доставить не малое количество смс на один номер.", "magenta"))
	print(colored("Не будьте жадны и слишком мстительны, тогда вы сможете отправлять смс на один и тот же номер постоянно.", "magenta"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def disclaimer():
	clear()
	print("")
	print(colored("Разработчик инструмента не несет ответственность за доставленный моральный или физический ущерб вашей жертве.", "magenta"))
	print(colored("Пользуясь данной программой вы автоматически соглашаетесь на это и берете всю ответственность на себя", "magenta"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def donate():
	clear()
	print("")
	print(colored("Ваша поддержа еще больше мотивирует меня выпускать обновления!", "magenta"))
	print("")
	print(colored("ТИНЬКОФФ", "yellow"))
	print(colored("2200 7004 9284 5630", "cyan"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def faq_proxy():
	clear()
	print("")
	print(colored("Почему с прокси такой медленный спам и такая частая проверка?", "red"))
	print(colored("Наш парсер берет прокси с общедоступных сервисов, конечно не только мы так делаем и соотвественно не только мы пользуемся этими прокси.", "magenta"))
	print(colored("Также на данных сервисах очень мало довольно быстрых и анонимных прокси что позволяло бы улучшить спам с ними.", "magenta"))
	print(colored("Частая проверка возникает из-за не стабильности этих прокси, часто они просто перестают работать и программа берет следующий из списка.", "magenta"))
	print("")
	print(colored("Почему нельзя просто брать прокси любой страны а не только номера которого ввели?", "red"))
	print(colored("Не получиться использовать допустим канадские прокси с российскими сервисами с доменом .ru", "magenta"))
	print(colored("Если на сайте указан домен данной страны то и прокси должны быть этой же страны.", "magenta"))
	print(colored("Сервисы с доменом своей страны просто не пустят наш запрос с прокси иной страны.", "magenta"))
	print("")
	print(colored("Почему нельзя просто подключить больше сервисов для прокси?", "red"))
	print(colored("90% Сервисов с бесплатными прокси просто воруют их друг у друга и из-за этого просто не получиться получить больший список.", "magenta"))
	print(colored("Мы стараемся искать хорошие сервисы с бесплатными прокси которые не воруют друг у другу и удобны в парсинге либо имеют свой API.", "magenta"))
	print("")
	print("")
	print(colored("Советуем вам использовать ваши собственные покупные прокси если хотите сократить блокировку вашего IP у сервисов и иметь хорошую скорость спама", "magenta"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			clear()
			print(colored("Файлы", "magenta"), colored("logs.txt error_logs.txt", "cyan"), colored("были сохранены в папку Download на вашем устройстве", "magenta"))
			print(colored("Пожалуйста отправьте поочередно эти 2 файла мне в лс", "magenta"), colored("https://t.me/EkZoRtSiSt6", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
		elif platform == "win32":
			clear()
			print("")
			print(colored("Пожалуйста отправьте мне в лс", "magenta"), colored("https://t.me/EkZoRtSiSt6", "cyan"), colored("поочередно файлы", "magenta"), colored("logs.txt error_logs.txt", "cyan"), colored("из папки", "magenta"), colored("tools", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
	except:
		clear()
		print("")
		print(colored("Мы не смогли переместить файлы в нужную директорию", "red"))
		print(colored("Возможно у вас для Термукса в настройках разрешения приложению не доступны Файлы и медиаконтент", "red"))
		print(colored("Пожалуйста разрешите Термуксу в настройках все нужные разрешения и повторите попытку"))
		print(colored("За помощью по данному вопросу пишите мне в лс"), colored("https://t.me/EkZoRtSiSt6", "cyan"))
		print("")
		print("\nНажмите Enter чтобы вернуться назад")
		input()

def clear_logs():
	a = open("tools/logs.txt", "w")
	a.close()
	a = open("tools/error_logs.txt", "w")
	a.close()
	clear()
	print("")
	print(colored("Логи успешно были очищены", "magenta"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def banner_info():
	clear()
	print(colored("Телеграм Канал", "magenta")+":", colored("https://t.me/bomberEkZoRtSiSt", "cyan"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def number_ckeck(numb):
	if len(numb) == 9 or len(numb) == 10:
		sp_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in str(numb):
			try:
				int(i)
			except:
				return False
		return True
	else:
		return False

def start_input():
	country_code = {"1": "+375",
					"2": "+7"}
	country_code_2 = {"1": "by",
					  "2": "ru"}
	while True:
		clear()
		print("")
		print(colored("[99] Отмена", "red"))
		print("")
		print(colored("[1]", "red"), colored("Беларусь +375", "magenta"))
		print(colored("[2]", "red"), colored("Россия +7", "magenta"))
		print("")
		ct = input(colored("Выберите страну: ", "red"))
		if ct == "2":
			break
		elif ct == "1":
			break
		elif ct == "99":
			return 0, 0, 0
	while True:
		clear()
		print("")
		print(colored("[99] Отмена", "red"))
		print("")
		numb = input(colored("Введите номер без кода страны "+country_code[ct]+" ", "red"))
		if number_ckeck(numb):
			break
		elif numb == "99":
			return 0, 0, 0
	while True:
		clear()
		print("")
		print(colored("[99] Отмена", "red"))
		print("")
		print(colored("[1]", "red"), colored("Да", "magenta"))
		print(colored("[2]", "red"), colored("Нет", "magenta"))
		print("")
		pr = input(colored("Использовать прокси?: ", "red"))
		if pr in ["1", "2"]:
			if pr == "1":
				pr = country_code_2[ct]
			else:
				pr = None
			break
		elif pr == "99":
			return 0, 0, 0
	if pr != None:
		while True:
			clear()
			print("")
			print(colored("[99] Отмена", "red"))
			print("")
			print(colored("[1]", "red"), colored("Общедоступный прокси", "magenta"))
			print(colored("Общедоступный прокси используют все пользователи EkZbomb3r", "cyan"))
			print("")
			print(colored("[2]", "red"), colored("Свой прокси", "magenta"))
			print(colored("Ваш прокси обязательно должен иметь протокол HTTP или HTTPS с поддержкой ipv4 и страну вашего номера", "cyan"))
			print("")
			who_pr = input(colored("Вариант: ", "red"))
			if who_pr in ["1", "2"]:
				if who_pr == "2":
					clear()
					print("")
					print(colored("[99] Отмена", "red"))
					print("")
					print(colored("Введите Ip и Port и логин и пароль если прокси частный", "magenta"))
					print("└"+colored("Пример:\n123.45.678.910:8080\n123.45.678.910:8080:LOGIN:PASSWORD", "magenta"))
					print("")
					new_pr = input(colored("~# ", "red"))
					
					if new_pr == "99":
						return 0, 0, 0
					elif len(new_pr.split(":")) < 3:
						# Shared Proxy Check
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1])
						if result == False:
							print(colored("Ваш прокси не работает!", "red"))
						else:
							pr = {"ip": new_pr.split(":")[0],
								  "port": new_pr.split(":")[1],
								  "format": result}
							print(colored("Прокси работает!", "magenta"))
							time.sleep(2)
							break
					elif len(new_pr.split(":")) > 2:
						# Private Proxy Check
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1], login=new_pr.split(":")[2], password=new_pr.split(":")[3])
						if result == False:
							print(colored("Ваш прокси не работает!", "red"))
						else:
							pr = {"ip": new_pr.split(":")[0],
								  "port": new_pr.split(":")[1],
								  "login": new_pr.split(":")[2],
								  "password": new_pr.split(":")[3],
								  "format": result}
							print(colored("Прокси работает!", "magenta"))
							time.sleep(2)
							break

				else:
					break
			elif who_pr == "99":
				return 0, 0, 0

	return country_code[ct]+numb, country_code_2[ct], pr

def ICC():
	try:
		anim_text("Проверка интернет соединения...", speed=0.030, color="magenta")
		r.get("https://example.org", timeout=5)
		clear()
	except Exception as es:
		clear()
		print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету или интернет слишком слабый!", "magenta"))
		exit()

def CFU():
	in_d = False
	# Checking the Internet
	try:
		r.get("https://example.org", timeout=5)
		in_d = True
	except:
		clear()
		print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету или интернет слишком слабый!", "magenta"))
		exit()
	clear()
	if in_d:
		anim_text("Проверяем обновления...", speed=0.050, color="magenta")
		result = r.get("https://raw.githubusercontent.com/dzeff9827/EkZbomb3r/master/version.txt")
		last_ver = result.content.decode("utf-8")
		a = open("tools/version.txt", "r")
		current_ver = a.read()
		a.close()
		if last_ver != current_ver:
			clear()
			print(colored("[!]", "magenta"), colored("Найдено новое обновление", "magenta"), colored(last_ver, "cyan")+colored("!", "magenta"))
			print("")
			print(colored("Желаете ли вы обновиться до актуальной версии?", "red"))
			print("")
			print(colored("[1]", "red"), colored("Да", "magenta"))
			print(colored("[2]", "red"), colored("Нет", "magenta"))
			print("")
			while True:
				how = input(colored("EkZbomb3r>>", "red"))
				if how == "1":
					webbrowser.open("https://github.com/dzeff9827/EkZbomb3r")
				elif how == "2":
					clear()
					break
		else:
			clear()

class Logs:
	def __init__(self):
		pass

	def save_logs(self, service, status_code, error="There is not"):
		date = datetime.now()
		if status_code in [666, False]:
			status_code = "Unknown"
		file = open("tools/logs.txt", "a")
		file.write(f"DATE - {date}\nService - {service}\nStatus_code - {status_code}\nERROR:\n{error}\n\n\n")
		file.close()

	def error_logs(self, error):
		date = datetime.now()
		file_error = open("tools/error_logs.txt", "a")
		file_error.write(f"DATE - {date}\nERROR:\n{error}\n")
		file_error.close()

def check_files():
	anim_text("Проверка файлов...", speed=0.050, color="magenta")
	files = os.listdir()
	list_ = ["EkZbomber.py", "LICENSE", "tools","Install.py"]
	list_2 = ["proxy.py", "sender.py", "services.json", "tools.py", "version.txt", "logs.txt", "error_logs.txt"]

	for f in list_:
		if f not in files:
			clear()
			print(colored("Наша программа не нашла некоторые наши файлы", "red"))
			print(colored("Пожалуйста установите программу заново предварительно удалив папку с этой!\n", "magenta"))
			exit()
	last_dir = os.getcwd()
	os.chdir("tools")
	files = os.listdir()
	for f in list_2:
		if f not in files:
			clear()
			print(colored("Наша программа не нашла некоторые наши файлы", "red"))
			print(colored("Пожалуйста установите программу заново предварительно удалив папку с этой!\n", "magenta"))
			os.chdir(last_dir)
			exit()
	os.chdir(last_dir)

def FormattingResponse(status_code, service):
	date = datetime.now()
	# Hour
	if date.hour <= 9:
		hour = f"0{date.hour}"
	else:
		hour = date.hour
	# Minute
	if date.minute <= 9:
		minute = f"0{date.minute}"
	else:
		minute = date.minute
	# Second
	if date.second <= 9:
		second = f"0{date.second}"
	else:
		second = date.second
	date = colored(f"{hour}:{minute}:{second}", "magenta")

	status_codes = {200: colored("отправлено", "green"),
					201: colored("отправлено", "green"),
					429: colored("время-истекает", "yellow"),
					400: colored("время-истекает", "yellow"),
					404: colored("не найдено", "red"),
					500: colored("время-истекает", "yellow"),
					400: colored("время-истекает", "yellow")}
	service = colored(service, "yellow")
	if status_code not in status_codes:
		status_code = colored("UNKNOWN ANSWER", "red")
		info = f"{date} | {service} | {status_code}"
		print(info)
	else:
		info = f"{date} | {service} | {status_codes[status_code]}"
		print(info)

def start(number, country, proxy_=None):
	# Proxy preparation
	if proxy_ == None:
		proxy_ = None
	elif proxy_ in ["ru", "by"]:
		starting = True
		while starting:
			print(colored("\nПодготовка прокси... (Не дольше 1 минуты)", "magenta"))
			if proxy_ == "by":
				proxy_class = proxy.Proxy(country=["ru", "by"])
			else:
				proxy_class = proxy.Proxy(country=[country])
			proxy_class.get()
			print("")
			print(colored("Проверка найденного списка прокси... (Не дольше 2х минут)", "magenta"))
			proxy_class.verify()
			if proxy_class.mix() == False:
				print(colored("\n\nУПС!", "red"), colored("К сожалению наша программа не смогла найти ни одного рабочего прокси ;(", "magenta"))
				print("")
				print(colored("[1]", "red"), colored("Без прокси", "magenta"))
				print(colored("[2]", "red"), colored("Попробуем еще раз", "magenta"))
				print(colored("[3]", "red"), colored("Выход", "red"))
				print("")
				print(colored("Начать спам без прокси или попробуем еще раз?", "red"))
				while True:
					how = input(colored("~# ", "red"))
					if how in ["3", "0", "99"]:
						return
					elif how == "1":
						proxy_ = None
						starting = False
						break
					elif how == "2":
						break
			else:
				print(colored("\n\nПытаемся найти подходящий! (Не дольше 1 минуты)", "magenta"))
				all_list = proxy_class.mix()
				bar = ChargingBar('Ищем подходящий', max = len(all_list["all"]))
				# proxy_class.list[proxy_]
				for pr in all_list["all"]:
					ch = proxy.SPC(pr["ip"], pr["port"])
					bar.next()
					if ch != False:
						proxy_ = {"ip": pr["ip"],
								  "port": pr["port"],
								  "format": ch}
						starting = False
						break
					else:
						all_list["all"].remove(pr)
				if proxy_ in ["ru", "by"]:
					print(colored("\n\nК сожалению наша программа не нашла рабочий прокси ;(", "red"))
					print("")
					print(colored("[1]", "red"), colored("Да", "magenta"))
					print(colored("[2]", "red"), colored("Нет", "magenta"))
					print("")
					while True:
						how = input(colored("Начать спам без прокси? ", "red"))
						if how == "2":
							return
						elif how == "1":
							proxy_ = None
							starting = False
							break
				else:
					print("")
					print(colored("Прокси найден!", "magenta"))
					time.sleep(2)
					starting = False
	else:
		proxy_ = proxy_


	clear()
	print("")
	print(colored("Остановка спама", "red"))
	print(colored("Termux", "magenta")+":", colored("На встроенной клавиатуре от Termux выбрать CTRL затем C", "cyan"))
	print(colored("Windows", "magenta")+":", colored("Комбинация клавишь Ctrl+C или Ctrl+Z", "cyan"))
	print(colored("Linux", "magenta")+":", colored("Комбинация клавишь Ctrl+Z", "cyan"))
	an=["5", "4", "3", "2", "1"]
	for i in an:
		print(colored("Спам начнется через ", "red")+colored(i, "magenta")+" ",sep=' ',end='\r')
		time.sleep(1)
	clear()

	# Number formats
	number = FormattingNumber(number, country)

	# Bomber launch
	sender_class = send.Send(country)
	logs = Logs()
	if country == "ru":
		services_list = send.services_list
	else:
		services_list = send.services_list_by
	starting_spam = True
	circles = 0
	circles_2 = 1
	while starting_spam:
		try:
			if circles == len(services_list):
				circles -= len(services_list)
				circles_2 += 1
			time.sleep(1)
			for serv in services_list:
				if sender_class.checktimeout(serv) == True:
					if proxy_ != None:
						result = sender_class.spam(serv, number, proxy=proxy_["format"])
						if result[0] == False:
							logs.save_logs(serv, result[0], error=str(result[1]))
						else:
							logs.save_logs(serv, result[0])
						if result[0] == False:
							# Checking the proxy before the next spam attempt
							print(colored("Проверка прокси...", "magenta"))
							if "login" in proxy_:
								test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"], login=proxy_["login"], password=proxy_["password"])
								if test_proxy == False:
									print(colored("Ваш прокси больше не работает!", "red"))
									print("")
									print(colored("[1]", "red"), colored("Да", "magenta"))
									print(colored("[2]", "red"), colored("Нет", "magenta"))
									while True:
										print("")
										print(colored("Продолжить спам без прокси?", "red"))
										print("")
										how = input(colored("~# ", "red"))
										if how == "2":
											starting_spam = False
											return
										elif how == "1":
											proxy_ = None
											break
								else:
									proxy_ = {"ip": proxy_["ip"],
										     "port": proxy_["port"],
										     "login": proxy_["login"],
										     "password": proxy_["password"],
										     "format": test_proxy}
									print(colored("Прокси работает!", "magenta"))
									print(colored("Продолжаю спам!", "magenta"))

							else:
								try:
									a = all_list
									general = True
								except:
									general = False
								if general == False:
									test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"])
									if test_proxy == False:
										print(colored("Ваш прокси больше не работает!", "red"))
										print("")
										print(colored("[1]", "red"), colored("Да", "magenta"))
										print(colored("[2]", "red"), colored("Нет", "magenta"))
										while True:
											print("")
											print(colored("Продолжить спам без прокси?", "red"))
											print("")
											how = input(colored("~# ", "red"))
											if how == "2":
												starting_spam = False
												return
											elif how == "1":
												proxy_ = None
												break
									else:
										print(colored("Ваш прокси работает, продолжаю спам", "magenta"))
								else:
									test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"])
									if test_proxy == False:
										if len(all_list["all"]) < 1:
											print(colored("Увы но прокси закончились ;(", "red"))
											print("")
											print(colored("[1]", "red"), colored("Да", "magenta"))
											print(colored("[2]", "red"), colored("Нет", "magenta"))
											while True:
												print("")
												print(colored("Продолжить спам без прокси?", "red"))
												print("")
												how = input(colored("~# ", "red"))
												if how == "2":
													starting_spam = False
													return
												elif how == "1":
													proxy_ = None
													break
										else:
											print(colored("Берем следующий прокси...", "magenta"))
											last_pr = proxy_
											all_list["all"].remove(proxy_)
											for pr in all_list["all"]:
												ch = proxy.SPC(pr["ip"], pr["port"])
												if ch != False:
													proxy_ = {"ip": pr["ip"],
														      "port": pr["port"],
														      "format": ch}
													starting = False
													break
												else:
													all_list["all"].remove(pr)
											if proxy_ == last_pr:
												print(colored("Увы но прокси закончились ;(", "red"))
												print("")
												print(colored("[1]", "red"), colored("Да", "magenta"))
												print(colored("[2]", "red"), colored("Нет", "magenta"))
												while True:
													print("")
													print(colored("Продолжить спам без прокси?", "red"))
													print("")
													how = input(colored("~# ", "red"))
													if how == "2":
														starting_spam = False
														return
													elif how == "1":
														proxy_ = None
														break
									else:
										print(colored("Прокси работает, продолжаю спам!", "magenta"))
						else:
							circles += 1
							if result[0] != False:
								if serv == "magnit":
									if type(result[1]) == dict:
										if result[1]["status_code"] == 200:
											FormattingResponse(200, serv)
										elif result[1]["status_code"] == 422:
											FormattingResponse(429, serv)
									else:
										FormattingResponse(result[0], serv)
								else:
									FormattingResponse(result[0], serv)
							else:
								FormattingResponse(666, serv)
					else:
						result = sender_class.spam(serv, number)
						if result[0] == False:
							logs.save_logs(serv, result[0], error=str(result[1]))
						else:
							logs.save_logs(serv, result[0])
						circles += 1
						if result[0] != False:
							if serv == "magnit":
								if type(result[1]) == dict:
									if result[1]["status_code"] == 200:
										FormattingResponse(200, serv)
									elif result[1]["status_code"] == 422:
										FormattingResponse(429, serv)
								else:
									FormattingResponse(result[0], serv)
							else:
								FormattingResponse(result[0], serv)
						else:
							FormattingResponse(666, serv)
		except KeyboardInterrupt:
			starting_spam = False
			print("\n")
			print(colored("Спам был принудительно оставлен\n", "magenta"))
			print("Нажмите Enter чтобы вернуть назад")
			try:
				input()
			except KeyboardInterrupt:
				return
			return
		except Exception as e:
			starting_spam = False
			print("\n")
			print(colored("Из-за неизвестной ошибки наша программа выдала ошибку при спаме\n", "red"))
			logs.error_logs(str(e))
			print(colored("Данная ошибка была сохранена в логи", "magenta"))
			print(colored("Пожалуйста отправьте нам файл с логами по инструкции в главном меню чтобы мы могли улучшать наш проект с вашей помощью", "magenta"))
			print("\nНажмите Enter чтобы вернуть назад")
			try:
				input()
			except KeyboardInterrupt:
				return
			return
