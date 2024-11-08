from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# 1. Ініціалізація Flask додатку
app = Flask(__name__)

# 2. Налаштування бази даних SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Ініціалізація SQLAlchemy
db = SQLAlchemy(app)

# 4. Створення моделі для продукту
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Product({self.id}, '{self.name}', {self.price})"

# 5. Ініціалізація бази даних (створення таблиці)
@app.before_request
def create_tables():
    db.create_all()

# 6. Маршрут для створення нового продукту (POST)
@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created'}), 201

# 7. Маршрут для отримання продукту за id (GET)
@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})

# 8. Маршрут для оновлення продукту за id (PUT)
@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()

    product.name = data['name']
    product.price = data['price']
    
    db.session.commit()
    return jsonify({'message': 'Product updated'})

# 9. Маршрут для видалення продукту за id (DELETE)
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})

# 10. Запуск додатку
if __name__ == '__main__':
    app.run(debug=True)