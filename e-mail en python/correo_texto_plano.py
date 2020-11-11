# importamos los paquetes necesarios
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# creamos una instancia del objeto MIMEMultipart
msg = MIMEMultipart()
 
 
mensaje = "Enviando un mensaje de texto plano desde python"
 
# Configuramos los parámetros del mensaje
password = "la password que tengas de tu cuenta de outlook"
msg['From'] = "tu_correo@outlook.com" #tu dirección de correo, este es ficticio
msg['To'] = "a_quien_va_dirigido@gmail.com" #a quien va dirigido, este es ficticio
msg['Subject'] = "Primer envio - prueba" #el asunto del correo
 
# Lo agregamos al cuerpo del mensaje como texto plano
msg.attach(MIMEText(mensaje, 'plain'))
 
# Nos conectamos al servidor
server = smtplib.SMTP('smtp.outlook.com')
 
server.starttls()
 
# Nos logueamos en el servidor para poder enviar el correo
server.login(msg['From'], password)
 
 
# enviamos el mensaje a través del servidor.
server.sendmail(msg['From'], msg['To'], msg.as_string())

# cerramos la conexión
server.quit()
 
print ("Enviado con éxito el e-mail a %s:" % (msg['To']))
