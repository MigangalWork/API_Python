from flask import Flask, jsonify
from flask_restful import Api, Resource
import requests

app = Flask(__name__) # Crea el servidor
api = Api(app)

products = [
    {'name': 'laptop', 'price': 800, 'quantity': 4},
    {'name': 'mouse', 'price': 40, 'quantity': 10},
    {'name': 'monitor', 'price': 400, 'quantity': 3}
]

@app.route('/')
def principal():
    return {"message": "Welcome to my REST API"}

@app.route('/ping') 
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/products', methods=['GET']) # Por defecto las rutas utilizan el método get. Se usa con POST, DELETE, PUT(actualizar)
def getProducts():
    return jsonify({"products": products})

@app.route('/products/<string:product_name>') # Para que al poner el nombre del producto, te saque solo la parte de la lista de dicho producto
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({'product': productFound[0]})
    else:
        return jsonify({"message": "Product not found"})

# Insomnia como ejemplo de app para mandar request a la API
@app.route('/products', methods=['POST']) # Se pueden tener aunque se llamen igual porque los métodos son distintos
def agregarProducto():
    new_product = {
        "name": requests.json['name'],
        "price": requests.json['price'],
        "quantity": requests.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Successfully", "product": new_product})

@app.route('/products/<string:product_name>', methods=['PUT']) # Para que al poner el nombre del producto, te saque solo la parte de la lista de dicho producto
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = requests.json['name']
        productFound[0]['price'] = requests.json['price']
        productFound[0]['quantity'] = requests.json['quantity']
        return jsonify({
            "message": "Product updated",
            "product": productFound[0]
            })
    else:
        return jsonify({"message": "Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE']) # Para que al poner el nombre del producto, te saque solo la parte de la lista de dicho producto
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound)
        return jsonify({
            "message": "Product deleted",
            "product": products
            })
    else:
        return jsonify({"message": "Product not found"})

'''#Hay que asegurarse de que la serie de datos que saque la clase tiene que ser serializable
class HellowWorld(Resource):
    # Los nombres de las clases son los nombres de los métodos luego del request
    def get(self):
        return {"data": "Hello World"}
    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld")'''# significa que  cuando haces un get al api con helloworld te devuelve lo de la class de arriba

if __name__ == "__main__":
	app.run(debug=True, port=4000) # Inicia el api