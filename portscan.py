# -*- coding: utf-8 -*-
print '''\033[1;32m
   ___       _          _                  
  / __\__ _ | |_  __ _ | | ___   ___   ___ 
 / _\ / _` || __|/ _` || |/ __| / _ \ / __|
/ /  | (_| || |_| (_| || |\__ \|  __/| (__ 
\/    \__,_| \__|\__,_||_||___/ \___| \___|'''+'\033[0;0m'
print '\033[1;35m'+'                                     Portscan'+'\033[0;0m'
print ''
print 'digite site alvo exemplo: "site.com, vaisefoder.com, meupau.com"'
vaisefoder=raw_input ('\033[31m'+'Site alvo: '+'\033[0;0m') 
import socket
import time
import datetime

date_object = datetime.date.today()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print ''
print'ataque iniciado no horario', current_time, 'na data', date_object 

print ''
print 'Iremos ver qual portas estão abertas'
portas = [21, 23, 80 ,8080, 443, 22] #lista de portas
print ''
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex((vaisefoder, porta))
    if codigo == 0:  
        print porta, '\033[1;32m'+'ESTA ABERTA'+'\033[0;0m'

 
