#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Enviar correo Gmail con Python
 
import smtplib
 
remitente = 'correo@gmail.com'
destinatario  = 'correo2@gmail.com'
msg = 'Correo enviado utilizano Python + smtplib'
 
 
# Datos
username = 'correo@gmail.com'
password = 'password'
 
# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(remitente, destinatario, msg)
server.quit()

#Otro ejemplo de envío de correo esta vez sólo con smtlib que esta incluida como librería standard y envío con gmail