import os				#Manejo de sistema operativo.
import sys				#Manejo de sistema operativo.
import requests      #Manejo de request con Python.
import json			#Manejo de json con Python.
import time			#Manejo de timpo con Python.

print("Por favor ingrese la URL a escanear (Ejemplo: https://www.yourwebsite.com) ") # Mensajito para saber qué hacer.

web = input() #Ingresar URL.
os.system('cls') #Limpiar pantalla.

print ("Ejecutando Análisis en https://urlscan.io/ ")

headers = {'API-Key':'1c2c94c5-a66a-4792-8396-14ff493a08d9','Content-Type':'application/json'} # Registrarse en www.urlscan.io para generar su propia API y cambiar el valor de la clave API-Key por la suya.
data = {"url": web , "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))

print("Respuesta del servidor: ",response) #Nos devuelve el código de respuesta del servidor
print("Raw de urlscan.io: ",response.json()) #Nos devuelve el contenido de la solicitud que hicimos en formato json.

response_json = response.json() # Genero un diccionario response_json con los datos que me devuelve la consulta, para poder extraer lo que necesito.

url = response_json['api'] # Extraigo sólo el valor de la clave 'api', que sería la URL que contiene los resultados del escaneo.

time.sleep(30) 	#Acá pongo un temporizador porque los resultados demoran en publicarse sobre la URL generada y a veces arroja error 404.
						#Si ven que no genera el archivo, puede que necesiten subir el temporizador un poco más.

response =requests.get(url) # Consumo toda la web desde la URL generada.

print(response.url) #Esto lo puedo sacar, es sólo para verificar que está consumiendo la URL correctamente.

if response.status_code == 200: 	# Si pasaron 30 segundos y generó un código 200 como respuesta, quiere decir que ya tiene datos.
												#(Acá también puede armar un while con el 404, hasta que genere el 200)
	content = response.content #Pasamos el contenido de la consulta a un diccionario
	
	file = open('resultado.json','wb') 	# Paso los datos a un documento
	file.write(content)						# Paso los datos a un documento
	file.close									# Paso los datos a un documento

os.system('cls') #Limpiar pantalla.
print ("Los resultados se han guardado en el archivo 'resultado.json' ")
print("Fin del Script")

sys.exit()


