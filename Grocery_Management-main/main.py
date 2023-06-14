from flask import Flask, render_template, request
import jsonify
import requests
import mysql_connection
import products_dao

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def Home():
    cnx = mysql_connection.get_connection()
    products = products_dao.get_products(cnx)

    if request.method == 'POST':
        del_id = int(request.form['product_id'])
        products_dao.delete_products(cnx, del_id) 
    
    return render_template('index.html', result = products)


@app.route('/add' , methods=['POST',"GET"])
def add():
    print("Mandar")
    if request.method == 'POST':

        cnx = mysql_connection.get_connection()

        p_name = (request.form['product_name'])
        price_per_unit = int(request.form['price/unit'])
        uom= int(request.form['uom'])

        product = {"name" : p_name, "uom_id" : uom, "price_per_unit":price_per_unit}
        products_dao.add_products(cnx, product)
        
        return render_template('add.html')
    else:
        return render_template('add.html')


if __name__=="__main__":
    app.run(debug=True)
