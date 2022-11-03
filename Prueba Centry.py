import requests    #Primero importar libreria para lograr conectarse a Centry con el Access Token.
import json        #Se importa la libreria para convertir la respuesta de centry en formato JSON con el fin de trabajar en Python.

id_producto = '5ad90853f82f452c796f4834'      #ID del producto a editar que se agregará en la URL.
access_token = 'd5cd42cf628928b5ed0d4f05100643201164fb2d49766d0e7df973c87e8937b2'                             #Código de acceso para conectarse a la aplicación de Centry (Reclutamiento).

url = "https://www.centry.cl/conexion/v1/products/"+id_producto+".json"   #URL de Centry a la que se conectará, previamente asignado la ID del producto.
payload={}                                 #Payload es el equivalente al Body de la solicitud en Postman, particularmente este se encuentra vacío ya que es un 'Get'.
headers = {                                #Headers es lo que va junto con la solicitud, incluido el Access Token.
  'Authorization': 'Bearer '+access_token, 'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload)    #Extraído de Postman (Get/Read), guarda la respuesta entregada por Centry en response.

respuesta_centry = response.json()                                        #Se crea una variable donde se incluye el JSON del producto otorgado por Centry.


#Al cumplir con los pasos anteriores donde ya dispongo con el JSON completo del producto, el siguiente paso es cambiar el stock de las variantes del producto
#para lo cual extraigo 'variants' y lo guardo en una variable de nombre VARIABLES.

VARIABLES = respuesta_centry['variants']

#El stock de un producto se encuentra en el espacio de 'quantity', entonces al ya tener todas las variantes dentro de VARIABLES, puedo cambiar el stock en cada una de ellas.

for stock in VARIABLES:
    stock['quantity'] = 50

#Lo anterior recorre cada una de las variantes, otorgandole un valor de 50 a cada 'quantity' independiente de cuantas tenga el producto.

#Al concluir la tarea de asignar un stock de 50 a cada variante, puedo modificar el JSON que me otorgó Centry al momento de pedir el producto.
#Los siguientes cambios sobreescribirán la respuesta otorgada por Centry (respuesta_centry), de acuerdo a las tareas solicitadas.
respuesta_centry['name'] = "Francisco Muñoz"  #Cambia el título de una publicación  ocupando tu nombre como título.
respuesta_centry['price_compare'] = 9990      #Cambia el precio  9990 (price_compare).
respuesta_centry['variants'] = VARIABLES      #Cada una de las variantes del producto debe tener un stock de 50 (Se reemplazó el JSON completo de 'variants' por el mismo pero con stock de 50 en cada variante).

#Para finalizar, se vuelve a subir la información actualizada del producto, en funcion de lo que contenga "respuesta_centry".
payload = json.dumps(      #Recordar que Payload es el equivalente a Body en Postman.
  respuesta_centry
)


response = requests.request("PUT", url, headers=headers, data=payload)  #Extraído de Postman (Put/Update), actualiza la información del producto.

print("Prueba Finalizada")