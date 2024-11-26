from flask import Flask, render_template
from dao.productDAO import productDAO

app = Flask(__name__)
productDAO = productDAO()


@app.route('/')
def show_products(): # index/product list page
    products = productDAO.getAllProducts()
    return render_template('index.html', products=products)

@app.route('/product/<int:productID>')
def show_details(productID):  # put application's code here
    products = productDAO.getProductById(productID)
    return render_template('', products=products)

if __name__ == '__main__':
    app.run()

