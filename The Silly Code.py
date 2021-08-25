#!/usr/bin/env python
# coding: utf-8

# < CORPO DO PROGRAMA >
# 

# In[5]:


import pyautogui as pat
import pyperclip as pcl
import time

pat.PAUSE = 1

#Passo 01 = Abrir calculadora
time.sleep (1)
pat.press ("win")
time.sleep (2)
pat.write ("calculadora")
pat.press ("enter")
time.sleep (5)

#Passo 02 = Digitar números
pat.press ("2")
pat.press ("+")
pat.press ("2")
pat.press ("enter")
time.sleep (3)

#Passo 03 = Fechar a calculadora
pat.click (x=931, y=322)
time.sleep (0.5)

#Passo 04 = Criar o "Erro"
print ("O resultado é")
time.sleep (1)
print (".")
time.sleep (1)
print (".")
time.sleep (1)
print (".")
time.sleep (1)
print (".")
time.sleep (1)
print (".")
time.sleep (1)
print (".")
time.sleep (1)
print (".")
time.sleep (1)
print (".")
time.sleep (1)
print (".")

time.sleep (1)
print ("Erro#0101012dj10")
print ("Impossível calcular resultado")


#Passo 05 = Finalizar código
time.sleep (2)
print ("Final do programa")




# 
# <POSIÇÃO DO MOUSE>
# 

# In[21]:


import pyautogui
import time


time.sleep (5)
pyautogui.position ()

