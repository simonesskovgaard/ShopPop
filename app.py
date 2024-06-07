from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from models import Users, Product, Cart
from forms import LoginForm, RegisterForm, ProductForm
import bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shop:pop@localhost:5433/shoppop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/product/<int:pk>')
def product(pk):
    product = Product.query.get_or_404(pk)
    return render_template('product.html', product=product)

@app.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(
            item=form.item.data,
            brand=form.brand.data,
            category=form.category.data,
            price=form.price.data,
            size=form.size.data,
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Your product has been listed!', 'success')
        return redirect(url_for('products'))
    return render_template('sell.html', form=form)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        products = Product.query.filter(Product.brand.ilike(f'%{query}%')).all()
    else:
        products = Product.query.all()
    return render_template('products.html', products=products, query=query)

@app.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_id=current_user.user_id).all()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_cart/<int:pk>')
@login_required
def add_to_cart(pk):
    print(f"Attempting to add product {pk} to cart for user {current_user.user_id}")  
    product = Product.query.get_or_404(pk)
    cart_item = Cart(user_id=current_user.user_id, product_id=pk)
    db.session.add(cart_item)
    db.session.commit()
    
    added_item = Cart.query.filter_by(user_id=current_user.user_id, product_id=pk).first()
    if added_item:
        print(f"Product {pk} successfully added to cart for user {current_user.user_id}")
    else:
        print(f"Failed to add product {pk} to cart for user {current_user.user_id}")
    
    flash('Product added to cart!', 'success')
    return redirect(url_for('products'))

@app.route('/delete_from_cart/<int:cart_id>')
@login_required
def delete_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != current_user.user_id:
        flash('You do not have permission to delete this item.', 'danger')
        return redirect(url_for('cart'))
    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart.', 'success')
    return redirect(url_for('cart'))




if __name__ == '__main__':
    app.run(debug=True)
