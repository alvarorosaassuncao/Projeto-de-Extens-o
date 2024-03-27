from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Dados de exemplo para usuários cadastrados
USERS = {'Alvaro': '123', 'usuario2': 'senha2'}

# Nova rota para a página de conteúdos
@app.route('/')
def conteudos():
    return render_template('conteudos.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            # Autenticado com sucesso, redireciona para a página inicial
            return redirect(url_for('index'))
        else:
            return 'Credenciais inválidas. Tente novamente.'
    return render_template('login.html')

# Rota originalmente designada para a página inicial
@app.route('/index')
def index():
    return render_template('index.html')

# Rotas existentes do seu site
@app.route('/curso_css')
def curso_css():
    return render_template('css.html')

@app.route('/curso_python')
def curso_python():
    return render_template('python.html')

@app.route('/curso_javascript')
def curso_javascript():
    return render_template('javascript.html')

@app.route('/contato')
def contato():
    # Seu código para a página de contato
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)
