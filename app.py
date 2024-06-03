from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создание объекта приложения Flask
app = Flask(__name__)

# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация расширения SQLAlchemy
db = SQLAlchemy(app)

# Определение моделей данных
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Создание всех таблиц базы данных (можно заменить на миграции)
with app.app_context():
    db.create_all()

# Маршруты и другие настройки Flask можно добавить ниже

# Пример маршрута
@app.route('/')
def index():
    return 'Hello, World!'

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)