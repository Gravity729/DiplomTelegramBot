from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Маршрут для корневого пути, чтобы вернуть index.html
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Маршрут для получения данных о курсах
def get_courses():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, description_short, description, image FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return [{"name": name, "price": price, "description_short": description_short, "description": description, "image": image} for name, price, description_short, description, image in courses]

@app.route('/get_courses', methods=['GET'])
def get_courses_route():
    courses = get_courses()
    return jsonify(courses)

# Маршрут для обработки запросов к изображениям
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(port=5001)
