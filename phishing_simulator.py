from flask import Flask, render_template, request

app = Flask(__name__)

# Página inicial simulando uma página de login
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Simulador de Phishing</title>
        </head>
        <body>
            <h1>Bem-vindo!</h1>
            <p>Insira suas credenciais abaixo para continuar.</p>
            <form action="/login" method="post">
                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email" required><br><br>
                <label for="password">Senha:</label><br>
                <input type="password" id="password" name="password" required><br><br>
                <button type="submit">Entrar</button>
            </form>
        </body>
    </html>
    """

# Rota para capturar os dados inseridos
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    # Apenas exibe os dados no console
    print(f"Tentativa de login capturada:")
    print(f"Email: {email}")
    print(f"Senha: {password}")
    
    return """
    <html>
        <head>
            <title>Simulador de Phishing</title>
        </head>
        <body>
            <h1>Obrigado!</h1>
            <p>Seus dados foram enviados com sucesso. (Simulação)</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
