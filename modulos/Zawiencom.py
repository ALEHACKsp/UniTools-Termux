# -*- coding: utf-8 -*-
#Modulo do UniTools-Termux
import os
import sys
import time
vermelho = '\033[31m'
branco = '\033[37m'
verde = '\033[32m'

#Banner 
def banner():
	print ("                    #     # ####### #     # " )
	print ("                    #     #    #     #   #  " )
	print ("                    #     #    #      # #   " )
	print ("                    #     #    #       #    " )
	print ("                    #     #    #      # #   " )
	print ("                    #     #    #     #   #  " )
	print ("                     #####     #    #     #   v1.1" )

# Reiniciar Programa
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

# Utilidades para facilitar
def erro():
	os.system("clear")
	print ("OPS! Parece que você inseriu uma opção incorreta :(")
	time.sleep(3)
	os.system("clear")
	restart_program()

def erro_en():
	os.system("clear")
	print ("OPS! It seems that you inserted an incorrect option :(")
	time.sleep(3)
	os.system("clear")
	restart_program()

def erro_es():
	os.system("clear")
	print ("OPS! Parece que has insertado una opción incorrecta :(")
	time.sleep(3)
	os.system("clear")
	restart_program()


def cc():
	os.system("clear")
	print ("Concluido!")
	time.sleep(3)
def update():
	os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade -y")

def root():
	print ("Root é necessario")
	print ("Deseja continuar?" + verde + "(S)im" + vermelho +"(N)ão" + branco)
	pedido_root = input("Selecione uma opção: ")



# Path
def path_pip():
	pip_path = "/data/data/com.termux/files/usr/tmp/pip"
	if os.path.isdir(os.path.join(pip_path)) != True:
		os.system("pkg install python")
	else:
		pass

def python3_path():
	python3_path = "/data/data/com.termux/files/usr/tmp/python3"
	if os.path.isdir(os.path.join(python3_path)) != True:
		os.system("pkg install python")

	else:
		pass
def path_pip2():
	pip2_path = "/data/data/com.termux/files/usr/tmp/pip2"
	if os.path.isdir(os.path.join(pip2_path)) != True:
		os.system("pkg install python2")
	else:
		pass
		
def python2_path():
	python2_path = "/data/data/com.termux/files/usr/tmp/python2"
	if os.path.isdir(os.path.join(python2_path)) != True:
		os.system("pkg install python2")

	else:
		pass

# Fim das Utilidades


# inicio do pacote
def menu_pacote_1():
	os.system("clear")

# Inicio da opção de atualização
def att():
	os.system("git pull")



# Fim da opção de atualização
