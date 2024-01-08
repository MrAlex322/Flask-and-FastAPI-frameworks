from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "4ghkiz2!1c43&=(3nd2bvqaj18jhfip5-=f79#e_+-e)ai18o!"


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        context = {
            'login': 'Авторизация'
        }
        return render_template('form.html', **context)
    elif request.method == 'POST':
        session['login'] = request.form.get('login')
        session['email'] = request.form.get('email')
        return redirect(url_for('success'))


@app.route('/success/', methods=['GET', 'POST'])
def success():
    if 'login' in session:
        context = {
            'login': session['login'],
            'email': session['email'],
            'title': 'Добро пожаловать'
        }
        if request.method == 'POST':
            session.pop('login', None)
            session.pop('email', None)
            return redirect(url_for('submit'))
        return render_template('success.html', **context)
    else:
        return redirect(url_for('submit'))


if __name__ == '__main__':
    app.run(debug=True)
