from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/product')
def product():
    return render_template('product.html')


if __name__ == '__main__':
    app.run(debug=True)
