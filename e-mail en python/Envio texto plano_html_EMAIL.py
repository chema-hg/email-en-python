#!/usr/bin/env python3

# Importamos los paquetes necesarios.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# creamos una instancia del objeto MIMEMultipart (alternative)
msg = MIMEMultipart('alternative')

# Creamos el cuerpo del mensaje. Va a ser texto plano y otro mensaje en html.
text = "Hi!\n¿Como estás?\nAqui esta el link que querias:\nhttps://novatilloenpython.blogspot.com/"
html = """\
<html>
  <head></head>
  <body>
    <p>¡Hola!<br>
       ¿Cómo estás?<br>
       Aqui tienes el link que querias <a href="https://novatilloenpython.blogspot.com/">link</a>.
    </p>
  </body>
</html>
"""

# Guardamos los tipos MIME de ambas partes, texto-plano y html:

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Agregamos ambas partes a nuestro contenedor de los mensajes.
# Según la especificación RFC 2046, la ultima parte de un mensaje multiparte, es este caso
# el mensaje html, será la mejor y será la que se utilice.
msg.attach(part1)
msg.attach(part2)


#Configuramos los parámetros del mensaje (password, remitente, destinatario, asunto)
msg['From'] = "tu_correo@outlook.com"
msg['To'] = "a_quien_va dirigido@gmail.com"
msg['Subject'] = "Envio texto plano y html - prueba"
password = "La contraseña de tu cuenta de correo"


# Enviamos el mensaje a través del servidor SMTP local.
server = smtplib.SMTP('smtp.outlook.com')

server.starttls()

# Nos conectamos y logeamos en el servidor para enviar el correo
server.login(msg['From'], password)

# la función sendmail tiene 3 argumentos: dirección del remitente, dirección del receptor
# y mensaje a enviar - Aqui se envia como un único string.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print ("E-mail enviado correctamente a %s:" % (msg['To']))