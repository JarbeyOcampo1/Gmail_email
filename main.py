import yagmail

#User credentials
user='xxxocampocuervo321xxx@gmail.com'
password='atyd ljqq icqe itej'

#Connections and error handle 
try: 
    yag = yagmail.SMTP(user, password)
except Exception as e: 
    print (f'Error de conexión o autenticación {e}')
    exit()

#Body

#Read files from .xt
with open ("emails.txt", "r") as file :
    recipients=[line.strip() for line  in file if line.strip()]
    
subjects='Hola este correo es de prueba'

messages='Libreria yagmail'

files=[r'C:\Users\Jaime\Desktop\campus.pdf',r'C:\Users\Jaime\Desktop\Factura_Sara.pdf']

print("\n Correo enviados : ", recipients)

#Send email
yag.send(recipients, subjects, messages, attachments=files)