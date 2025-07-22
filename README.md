# Gmail_email

**Hola

-Este codigo fue elaborado para poder automatizar el envio de correos electrónicos a través de la cuenta de correo electrónico de Gmail con la herramienta de Python llamada yagmail.

-Github de la herramienta: https://github.com/kootenpv/yagmail

----------------------------------------------------------------------------------------------------------------

- **Como funciona :**

-Primero debes configurar tu cuenta de gmail para poder tener una contraseña para que la herramienta tenga acceso a tu cuenta y enviar correos electrónicos.
Aqui tienes un video que lo explica, el video esta en español pero puedes usar subtitulos: https://www.youtube.com/watch?v=eBm6yLIjv3U

-Despues de tener la contraseña debes configurar en el codigo el usuario y contraseña:

```python
user='email@gmail.com'
password='password'

```
-Debes mantener el .txt tal cual como esta y ya quieres cambiar de .txt  por otro debes modificar la siguiente linea de codigo: 

```python
try: 
    with open ("cambiar el archivo .txt", "r") as file :
        recipients=[line.strip() for line  in file if line.strip()]
except FileNotFoundError:
    print ("El archivo (cambiar) no se encuentra.")
    exit()
except Exception as e:
    print(f'Error al leer el archivo (cambiar): {e}')
    exit()
```

-En la linea de files debes poner todas las rutas de los archivos que deseas enviar a los correos electrónicos. Al igual que subject, messages y signature

Esto seria hasta el momento, es algo sencillo como para probar la funcionalidad de la herramienta y automatizar el envio de correos, Tambien se puede usar para fines de hacking etico.

----------------------------------------------------------------------------------------------------------------

