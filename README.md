
# ShredShack Webstore

ShredShack is a modern gym supplement webstore built using Flask. The project includes essential e-commerce features such as user registration, login, a product listing page, a cart system, and a checkout page. 

---

## Project Structure

```
termin_oppgave/
├── app.py
├── static/
│   ├── styles.css
│   ├── images/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── cart.html
│   ├── checkout.html
└── README.md
```

---

## Features

- **User Authentication**:
  - Register and login functionality with password hashing using `bcrypt`.
  - Flash messages to notify the user (e.g., "User registered", "Incorrect password").
- **Home Page**:
  - Displays a list of 7 gym supplements.
  - Easy-to-add product images.
- **Cart System**:
  - Fully functional cart where users can add products.
  - Items appear with a multiplier if added multiple times.
- **Checkout**:
  - Checkout process to review purchases.
- **Database Integration**:
  - SQLite for persistent user storage.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ShredShack.git
   cd ShredShack
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy flask-bcrypt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open the app in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage

### 1. Register
- Navigate to `/register` to create a new account.

### 2. Login
- Navigate to `/login` to access your account.

### 3. Browse Products
- View products on the home page and add them to the cart.

### 4. Manage Cart
- Visit `/cart` to manage items in your cart.

### 5. Checkout
- Go to `/checkout` to review and confirm your purchase.

---

## Code Overview

### `app.py`
Main application file, handling routes, database setup, and core functionality.

### Templates (`templates/`)
- **`base.html`**: Shared layout for all pages.
- **`home.html`**: Product listing page.
- **`login.html`**: Login form.
- **`register.html`**: Registration form.
- **`cart.html`**: Displays items in the cart.
- **`checkout.html`**: Review and confirm purchases.

### Static Files (`static/`)
- **`styles.css`**: Stylesheet for modern design.
- **`images/`**: Placeholder folder for product images.

---

## Screenshots

### Home Page
![Home Page Screenshot](static/images/homepage_example.png)

### Cart Page
![Cart Page Screenshot](static/images/cart_example.png)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributors

- **Your Name** - Developer and Maintainer.

Feel free to contribute to this project by submitting issues or pull requests!
