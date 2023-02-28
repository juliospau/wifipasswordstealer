import subprocess
from colorama import init, Fore

init()
RED=Fore.RED
GREEN=Fore.GREEN
RESET=Fore.RESET

command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
command = command.decode('utf-8', errors ="backslashreplace")
command = command.split("\n")

wifiData = []
wifiProf = {}

for i in command:
	if "Perfil de todos los usuarios" in i:
		i = i.split(":")
		i = i[1]
		i = i[1:-1]
		wifiData.append(i)

for i in wifiData:
	
	command = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, "key=clear"])
	command = command.decode('utf-8', errors ="backslashreplace")
	command = command.split("\n")

	wifiN = [j.split(":")[1][1:-1] for j in command if "Nombre de SSID" in j]
	passW = [j.split(":")[1][1:-1] for j in command if "Contenido de la clave" in j]

	namE = ""
	pasW = ""

	for k in wifiN:
		for l in passW:
			namE += k
			pasW += l
			wifiProf.update({namE:pasW})
			namE = ""
			pasW = ""

for i,j in wifiProf.items():
	print ( f'{RED}', i, f"{RESET}|{GREEN}", j, f'{RESET}')
