import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración
relay_host = "192.168.88.143"   # Servidor relay Outlook/Exchange
relay_port = 25                     # Usualmente 25, a veces 587 (sin TLS)
remitente = "cess@nuevaeps.com.co"  # Cuenta genérica configurada en el relay
destinatario = "cesar.solano@nuevaeps.com.co"

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje["From"] = remitente
mensaje["To"] = destinatario
mensaje["Subject"] = "Prueba de envío desde Python sin contraseña"

cuerpo = """
Hola,

Este es un correo de prueba enviado a través del relay Outlook/Exchange sin autenticación.

Saludos,
Script Python
"""
mensaje.attach(MIMEText(cuerpo, "plain"))

try:
    # Conexión al relay (sin autenticación)
    with smtplib.SMTP(relay_host, relay_port) as servidor:
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
    print("Correo enviado correctamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
