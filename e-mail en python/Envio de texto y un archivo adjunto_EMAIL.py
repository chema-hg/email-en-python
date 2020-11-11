# Importamos las bibliotecas necesarias
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTP

# creamos una instancia del objeto MIMEMultipart
msg = MIMEMultipart()

# Esta es la parte del email que contiene el texto:
part = MIMEText("¡Hola!, te paso un archivo interesante.")
msg.attach(part)

# Esta es la parte binaria (puede ser cualquier extensión):
part = MIMEApplication(open("contenido.txt", "rb").read())
part.add_header('Content-Disposition', 'attachment', filename="contenido.txt")
msg.attach(part)

# Se pueden seguir agregando partes (texto, imágenes, datos binarios, etc.)

# Configuramos los parámetros del mensaje
msg['From'] = "tu_email@outlook.com"
msg['To'] = "correo_del_destinatario@gmail.com"
msg['Subject'] = 'Esto es una prueba de envio de texto y un archivo adjunto'
password = "la contraseña de tu correo"

# Creamos una instancia del servidor y lo iniciamos
server = SMTP('smtp.outlook.com')

server.starttls()

# Nos logeamos en el servidor para poder enviar el e-mail
server.login(msg['From'], password)

# Enviar el mail (o los mails)
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("E-mail enviado correctamente a %s:" % (msg['To']))
