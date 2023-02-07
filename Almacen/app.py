"""
Flask app
"""

from flask import Flask, request, redirect, Response

from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/article", methods=["GET"])
def article():
    """
    Function to show data
    """
    
  
@app.route("/checksize",methods=['POST'])
def checksize():
  """
  Comprueba disponibilidad de un tamaño de pizza.
  """
  # Aquí va el código Python. Debe capturar el parámetro "size" de la request. Debe
  # retornar siempre "Disponible", excepto para el tamaño "S" que debe retornar "No
  # disponible" y se debe asignar en mensaje, así mensaje = "Lo que corresponda"
  
  v_size = request.form.get("size")
  if v_size == "S": 
    mensaje = "No Disponible"
  else:
    mensaje = "Disponible"
  
  return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
