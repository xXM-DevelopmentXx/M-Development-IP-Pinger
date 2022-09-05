#Importiert das Modul OS
import os

#### Cleart die Console ####
os.system("cls")

#### Printet text etc in die Console ####
print("#" *60)

#### Eingabe der IP Adresse die gepingt werden soll ####
IP_die_gepingt_werde_soll = input("Gebe hier Die IP-Adresse ein die Gepingt werden soll: ")

#### Printet Text etc in die Console ####
print("-" *60)
#### OS soll die IP-Adresse pingen ####
os.system("ping {}" .format(IP_die_gepingt_werde_soll))

#### Printet text etc in die Console ####
print("-" *60)

################################# INFORMATION #################################
print("#" *60)
print("Coded by mxrvin#5452 \nOwner von M-Development \nM-Development Discord: https://discord.gg/JUuxCYJA5W \nM-Development Github: https://github.com/xXM-DevelopmentXx")
print("#" *60)

#### Wartet auf eingabe einer taste um das Programm zu schließen ####
input("Drücke eine Taste um das Programm zu schließen!")
