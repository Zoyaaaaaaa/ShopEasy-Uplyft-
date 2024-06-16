from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from psutil import users

# Initialize Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define User and Product models
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Create database tables and populate sample data if empty
with app.app_context():
    db.create_all()
    if not Product.query.first():
        sample_products = [
     Product(name="Desktop Computer", description="High-performance desktop computer for professionals", price=1299.99, stock=10),
    Product(name="Wireless Mouse", description="Ergonomic wireless mouse for comfortable computing", price=39.99, stock=50),
    Product(name="External Hard Drive", description="Portable external hard drive for data backup", price=89.99, stock=30),
    Product(name="USB Flash Drive", description="Compact USB flash drive for easy data transfer", price=19.99, stock=100),
    Product(name="Wireless Keyboard", description="Full-size wireless keyboard for convenient typing", price=49.99, stock=40),
    Product(name="Monitor", description="Ultra-wide monitor for immersive viewing experience", price=699.99, stock=15),
    Product(name="Printer", description="All-in-one printer for printing, scanning, and copying", price=299.99, stock=20),
    Product(name="Router", description="High-speed wireless router for seamless internet connectivity", price=99.99, stock=25),
    Product(name="Graphics Tablet", description="Digital graphics tablet for creative professionals", price=199.99, stock=10),
    Product(name="Portable Charger", description="Compact portable charger for charging on the go", price=29.99, stock=60),
    Product(name="Webcam", description="HD webcam for video conferencing and streaming", price=79.99, stock=20),
    Product(name="Smart Home Hub", description="Centralized smart home hub for home automation", price=149.99, stock=5),
    Product(name="VR Headset", description="Immersive virtual reality headset for gaming and entertainment", price=399.99, stock=10),
    Product(name="Wireless Earbuds", description="True wireless earbuds for crystal-clear audio", price=129.99, stock=30),
    Product(name="Cordless Vacuum Cleaner", description="Efficient cordless vacuum cleaner for hassle-free cleaning", price=299.99, stock=15),
    Product(name="Electric Toothbrush", description="Advanced electric toothbrush for superior dental care", price=79.99, stock=25),
    Product(name="Smart Thermostat", description="Programmable smart thermostat for energy efficiency", price=149.99, stock=10),
    Product(name="Home Security Camera", description="Wireless home security camera for peace of mind", price=199.99, stock=20),
    Product(name="Bluetooth Headset", description="Comfortable Bluetooth headset for hands-free calling", price=59.99, stock=30),
    Product(name="Wireless Charging Pad", description="Qi-compatible wireless charging pad for smartphones", price=49.99, stock=40),
    Product(name="Air Purifier", description="HEPA air purifier for clean and fresh indoor air", price=249.99, stock=15),
    Product(name="Electric Kettle", description="Fast-boiling electric kettle for hot beverages", price=39.99, stock=25),
    Product(name="Portable Bluetooth Keyboard", description="Compact Bluetooth keyboard for mobile typing", price=59.99, stock=20),
    Product(name="Digital Photo Frame", description="Digital photo frame for displaying memories in style", price=89.99, stock=10),
    Product(name="Smart Plug", description="Wi-Fi smart plug for remote control of appliances", price=29.99, stock=30),
    Product(name="Wireless Charging Stand", description="Sleek wireless charging stand for smartphones", price=39.99, stock=40),
    Product(name="Car Dash Cam", description="HD dash cam for recording driving footage", price=129.99, stock=15),
    Product(name="Noise-Canceling Headphones", description="Premium noise-canceling headphones for immersive audio experience", price=299.99, stock=20),
    Product(name="Portable Bluetooth Speaker", description="Compact Bluetooth speaker for music on the go", price=59.99, stock=25),
    Product(name="Smart Light Bulb", description="Wi-Fi smart light bulb for customizable lighting", price=19.99, stock=35),
    Product(name="Wireless Gaming Mouse", description="High-performance wireless gaming mouse for gamers", price=79.99, stock=10),
    Product(name="Electric Scooter", description="Foldable electric scooter for urban commuting", price=399.99, stock=5),
    Product(name="Bluetooth Car Kit", description="Bluetooth car kit for hands-free calling in the car", price=49.99, stock=20),
    Product(name="Fitness Smartwatch", description="Fitness-oriented smartwatch with health tracking features", price=199.99, stock=15),
    Product(name="Smart Doorbell", description="Wi-Fi smart doorbell with video monitoring and two-way audio", price=149.99, stock=10),
    Product(name="Wireless Charging Mat", description="Multi-device wireless charging mat for smartphones and other devices", price=69.99, stock=25),
    Product(name="Electric Standing Desk", description="Height-adjustable electric standing desk for ergonomic work setup", price=599.99, stock=5),
    Product(name="Smart Scale", description="Bluetooth-enabled smart scale for tracking weight and body composition", price=79.99, stock=15),
    Product(name="Robot Vacuum Cleaner", description="Intelligent robot vacuum cleaner for automated cleaning", price=349.99, stock=10),
    Product(name="Wireless Router", description="Dual-band wireless router for high-speed internet", price=129.99, stock=20),
    Product(name="Mini Projector", description="Compact mini projector for portable entertainment", price=199.99, stock=10),
    Product(name="Bluetooth Earphones", description="Wireless Bluetooth earphones for music and calls", price=99.99, stock=25),
    Product(name="Smart Water Bottle", description="Hydration-tracking smart water bottle for staying hydrated", price=49.99, stock=30),
    Product(name="Electric Wine Opener", description="Automatic electric wine opener for effortless wine opening", price=29.99, stock=15),
    Product(name="Wireless Charging Dock", description="Charging dock with wireless charging capabilities for multiple devices", price=89.99, stock=20),
    Product(name="Smart Mirror", description="Interactive smart mirror with built-in display and voice assistant", price=399.99, stock=5),
    Product(name="Wireless Doorbell", description="Wireless doorbell with long-range connectivity and customizable chimes", price=59.99, stock=15),
    Product(name="Smart Ceiling Fan", description="Wi-Fi-enabled smart ceiling fan for smart home integration", price=199.99, stock=10),
    Product(name="Smart Alarm Clock", description="Smart alarm clock with customizable alarms and sleep tracking", price=49.99, stock=20),
    Product(name="Gaming Mouse Pad", description="Large gaming mouse pad for precise mouse movement", price=19.99, stock=40),
    Product(name="Wireless Charging Car Mount", description="Wireless charging car mount for convenient smartphone charging while driving", price=49.99, stock=30),
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

# Define user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

# Routes for user authentication (register, login, logout)
@app.route('/register', methods=["GET", "POST"])
def register():
    # Registration form handling
    if request.method == "POST":
        user = Users(username=request.form.get("username"), password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Login form handling
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user and user.password == request.form.get("password"):
            login_user(user)
            flash('You have successfully logged in!', 'success')
            return redirect(url_for("home"))
        else:
            flash('Invalid username or password', 'danger')
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out!', 'success')
    return redirect(url_for("home"))

# Main route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    products = None
    if request.method == 'POST':
        query = request.form.get('query')
        # Check if the user wants to reset the session
        if 'reset_session' in request.form:
            session.clear()
            flash('Session reset successfully!', 'success')
            return redirect(url_for('home'))
        products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    return render_template("home.html", products=products, session=session)


@app.route("/chat", methods=["POST"])
def chat_response():
    user_message = request.json.get("message")
    response = handle_user_message(user_message)
    return jsonify({"reply": response})

# Function to handle user messages in the chatbot
def handle_user_message(message):
    message = message.lower()
    if "search" in message:
        query = message.replace("search", "").strip()
        products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
        if products:
            response = "Here are the products I found:\n" + "\n".join([f"{p.name}: ${p.price}" for p in products])
        else:
            response = "No products found."
    elif "buy" in message:
        if not current_user.is_authenticated:
            return "Please log in to buy products."
        product_name = message.replace("buy", "").strip()
        product = Product.query.filter(Product.name.ilike(f'%{product_name}%')).first() 
        if product:
            if product.stock > 0:
                if session.get(product_name, False):
                    return f"You have already bought {product_name} in this session."
                product.stock -= 1
                db.session.commit()
                session[product_name] = True
                response = f"You have successfully bought {product_name} for ${product.price}."
            else:
                response = f"Sorry, {product_name} is out of stock."
        else:
            response = "Product not found."
    else:
   
        if current_user.is_authenticated:
            username = current_user.username
            response = f"Hey {username}! I can help you search for products or buy them. Try 'search [product name]'."
        else:
            response = "Hey there! I can help you search for products or buy them. Try 'search [product name]'."
    return response


if __name__ == "__main__":
    app.run(debug=True)
