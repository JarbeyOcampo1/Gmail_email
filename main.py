import yagmail
import os

#User credentials
user='youremail@gmail.com'
password='yourpassword'

#Connections and error handle 
try: 
    yag = yagmail.SMTP(user, password)
except Exception as e: 
    print (f'Error de conexión o autenticación {e}')
    exit()

#Body
#Read files from .xt
try: 
    with open ("emails.txt", "r") as file :
        recipients=[line.strip() for line  in file if line.strip()]
except FileNotFoundError:
    print ("El archivo emails.txt no se encuentra.")
    exit()
except Exception as e:
    print(f'Error al leer el archivo emails.txt: {e}')
    exit()

files=[r'rute/to/your/file1', r'rute/to/your/file2']  # Add your file paths here
subjects=" title of the email"
messages="""
    <p> text </p>
    <p> text </p>
"""
signature="""
    <p> text </p>
"""
#Combine messages and signature
content = messages + signature

#Verifaction of files
for file in files:
    if not os.path.isfile(file):
        print(f'Archivo no encontrado: {file}')
        exit()

#Send email
try:
    yag.send(recipients, subject=subjects, contents=content, attachments=files)
    print("Correo enviado correctamente a todos los destinatarios.")
    print("\n Correo enviados : ", recipients)
except Exception as e:
    print (f'Error al enviar el correo: {e}')
    exit()


