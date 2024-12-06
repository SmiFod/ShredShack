from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample product data
products = [
    {"name": "Ashwaganda", "image": "Ashwaganda.png"},
    {"name": "Bcaa", "image": "Bcaa.png"},
    {"name": "Creatine", "image": "Creatine.png"},
    {"name": "Multi Vitamins", "image": "Multi_vitamines.png"},
    {"name": "Pre Workout", "image": "PreWorkout.png"},
    {"name": "Protein", "image": "Protein.png"},
    {"name": "Shred Shack", "image": "Shred_Shack.png"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)