# Импортируем необходимые библиотеки и модули
from flask import Flask, render_template
import calculation

# Создаем экземпляр приложения Flask
app = Flask(__name__)


# Определяем маршрут для страницы 404 (страница не найдена)
@app.route("/404")
def index():
    # Отображаем шаблон 404.html
    return render_template("404.html")


# Определяем маршрут для главной страницы
@app.route("/")
def page_elki():
    # Вызываем функцию run() из модуля calculation и получаем результаты
    bar, img = calculation.run()
    # Отображаем шаблон index.html с переданными переменными bar и img
    return render_template("index.html", bar=bar, img=img)


# Запускаем приложение Flask
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
