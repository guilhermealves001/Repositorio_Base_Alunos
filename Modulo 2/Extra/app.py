from flask import Flask, render_template
# cria uma instância de um servidor flask
app = Flask(__name__)
# cria rota para a página principal do site 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')
# executa o servidor flask
if __name__ == '__main__':
    app.run(debug=True)

# no terminal, executar o arquivo app.py

#python app.py

# o servidor flask vai ser executado e rodar no endereço
# 127.0.0.1:5000