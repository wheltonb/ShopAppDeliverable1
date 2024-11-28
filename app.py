from flask import Flask, render_template, request, redirect, url_for, session
from dao.productDAO import productDAO
from services.UserService import UserService

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'ProjectSecretKey'
productDAO = productDAO()
userService = UserService()


@app.route('/', methods=['GET', 'POST'])
def homepage():  # index/product list page

    if 'session_user' not in session:
        session['session_user'] = 'Guest' # setting the default value of the user session

    if request.method == 'POST':
        # If logout button is clicked, reset the session_user to 'Guest'
        if 'logout' in request.form:    # checks the post method to see if it is the logout button being pushed
            session['session_user'] = 'Guest'  # Reset session_user to "Guest"
            print("User logged out, session reset.")  # Debugging message
            return redirect(url_for('homepage'))  # Redirect to the homepage with the reset session

    session.setdefault('cart', [])
    products = productDAO.getAllProducts()
    cart = session.get('cart', [])
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # take email and password from the login form
        email = request.form.get('emailField')
        password = request.form.get('passwordField')

        userToLogin = userService.verifyUser(email, password)

        if userToLogin:
            products = productDAO.getAllProducts()

            if userToLogin.isManager:
                session['session_user'] = "Admin"
                session['user_email'] = userToLogin.userEmail
                return render_template("index.html", products=products)

            else:
                session['session_user'] = "User"
                session['user_email'] = userToLogin.userEmail
                return render_template("index.html", products=products)

        else:
            return render_template("login.html", errorMessage="Incorrect email or password")

    return render_template("login.html")





    return render_template('login.html')


if __name__ == '__main__':
    app.run()
