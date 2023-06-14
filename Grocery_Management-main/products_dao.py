import mysql_connection

def get_products(cnx):
    cursor = cnx.cursor()
    query = ("SELECT product.product_id, product.name, product.uom_id, product.price_per_unit, uom.uom_name FROM product inner join uom on product.uom_id = uom.uom_id")

    cursor.execute(query)
    
    response = []
    for (product_id, name, uom, price_per_unit, uom_name) in cursor:
        response.append({
        "product_id": product_id, 
        "name" : name, 
        "uom" : uom, 
        "price_per_unit" : price_per_unit, 
        "uom_name" : uom_name
            })

    return response


def add_products(cnx, product):
    cursor = cnx.cursor()
    query = ("insert into product(name, uom_id, price_per_unit) values(%s, %s, %s)")

    data = (product["name"], product["uom_id"], product["price_per_unit"])

    cursor.execute(query, data)
    cnx.commit()
    
def delete_products(cnx, product_id):
    cursor = cnx.cursor()
    query = (f"delete from product where product_id = {product_id}")
    cursor.execute(query)
    cnx.commit()
    
