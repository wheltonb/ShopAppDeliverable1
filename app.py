from flask import Flask, render_template, request, redirect, url_for, session
from dao.productDAO import productDAO

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'ProjectSecretKey'
productDAO = productDAO()


@app.route('/', methods=['GET', 'POST'])
def homepage():  # index/product list page
    if 'session_user' not in session:
        session['session_user'] = 'Guest' # setting the default value of the user session

    # if block defining actions taken on post method from HTML
    if request.method == 'POST':
        # If logout button is clicked, reset the session_user to 'Guest'

        if 'logout' in request.form: # checks the post method to see if it is the logout button being pushed
            session['session_user'] = 'Guest'  # Reset session_user to "Guest"
            return redirect(url_for('homepage'))  # Redirect to the homepage with the reset session

    products = productDAO.getAllProducts()
    return render_template('index.html', products=products)


@app.route('/product/<int:productID>', methods=['GET', 'POST'])
def show_details(productID):
    # if block defining actions taken on post method from HTML
    if request.method == 'POST':
        if 'logout' in request.form:
            session['session_user'] = 'Guest'
            return redirect(url_for('homepage'))

        if 'add_to_cart' in request.form:
            return "test"

    # If it's a GET request, show the product details
    products = productDAO.getProductById(productID)
    return render_template('product_details.html', products=products)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # extract email and password entry from form data
        email = request.form.get('emailField')
        password = request.form.get('passwordField')
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
