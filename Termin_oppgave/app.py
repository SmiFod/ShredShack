from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
 
app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
 
# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
 
# Mock database for products
products = [  # List of available products
    {"id": 1, "name": "Ashwaganda", "price": 29.99, "image": "images/Ashwaganda.png"},
    {"id": 2, "name": "Bcaa", "price": 19.99, "image": "images/Bcaa.png"},
    {"id": 3, "name": "Creatine", "price": 14.99, "image": "images/Creatine.png"},
    {"id": 4, "name": "Multi Vitamines", "price": 24.99, "image": "images/Multi_vitamines.png"},
    {"id": 5, "name": "Whey Protein", "price": 9.99, "image": "images/Protein.png"},
    {"id": 6, "name": "Preworkout", "price": 12.99, "image": "images/PreWorkout.png"}
]
cart = {}  # Stores cart items as {product_id: {name, price, quantity}}
 
# Create the database tables if they don't exist
with app.app_context():
    db.create_all()
 
@app.route('/')
def index():
    return redirect(url_for('login'))
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # No need for a confirmation password here
 
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')
 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']  # New field for confirmation
 
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
        elif len(password) < 7:
            flash('Password must be at least 7 characters long.', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match.', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')
 
@app.route('/home')
def home():
    if 'user' not in session:
        flash('Please log in to view the home page.', 'danger')
        return redirect(url_for('login'))
    return render_template('home.html', products=products)
 
@app.route('/cart')
def view_cart():
    if 'user' not in session:
        flash('Please log in to view your cart.', 'danger')
        return redirect(url_for('login'))
   
    # Ensure the cart items have the right structure
    cart_items = [{"name": item["name"], "price": item["price"], "quantity": item["quantity"]} for item in cart.values()]
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart=cart_items, total=total)
 
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'user' not in session:
        flash('Please log in to add items to your cart.', 'danger')
        return redirect(url_for('login'))
 
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        if product_id in cart:
            cart[product_id]['quantity'] += 1
        else:
            cart[product_id] = {"name": product['name'], "price": product['price'], "quantity": 1}
        flash(f'{product["name"] } added to cart!', 'success')
    return redirect(url_for('home'))
 
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user' not in session:
        flash('Please log in to proceed to checkout.', 'danger')
        return redirect(url_for('login'))
 
    if request.method == 'POST':
        cart.clear()
        flash('Checkout successful! Thank you for your purchase.', 'success')
        return redirect(url_for('home'))
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('checkout.html', cart=cart, total=total)
 
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))
 
if __name__ == '__main__':
    app.run(debug=True)