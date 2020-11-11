# importamos los paquetes necesarios
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# creamos una instancia del objeto MIMEMultipart
msg = MIMEMultipart()

# adjuntamos la imagen al cuerpo del mensaje
file = open('imagen.jpeg', 'rb')
imagen = MIMEImage(file.read())
file.close()
msg.attach(imagen)

# configuramos los parametros del mensaje
password = "la contraseña de tu correo"
msg['From'] = "tu_correo@outlook.com"
msg['To'] = "correo_del_destinatario@gmail.com"
msg['Subject'] = "Envío de una imagen adjunta al correo"


# creamos e iniciamos el servidor
server = smtplib.SMTP('smtp.outlook.com')

server.starttls()

# Nos logeamos en el servidor para poder enviar el e-mail
server.login(msg['From'], password)

# Enviamos el mensaje a través del servidor.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("E-mail enviado correctamente a %s:" % (msg['To']))
