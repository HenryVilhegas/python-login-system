import customtkinter as ctk
import sqlite3
import os

# ================= CAMINHO DO BANCO =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'usuarios.db')

# ================= CONFIG =================
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

# ================= JANELA LOGIN =================
app = ctk.CTk()
app.title('Login da Loja')
app.geometry('350x400')
app.resizable(False, False)

titulo = ctk.CTkLabel(
    app,
    text='Login da Loja',
    font=('Arial', 24, 'bold')
)
titulo.pack(pady=30)

entrada_usuario = ctk.CTkEntry(
    app,
    placeholder_text='Usuário',
    width=250,
    height=40
)
entrada_usuario.pack(pady=10)

entrada_senha = ctk.CTkEntry(
    app,
    placeholder_text='Senha',
    show='*',
    width=250,
    height=40
)
entrada_senha.pack(pady=10)

mensagem = ctk.CTkLabel(app, text='', font=('Arial', 14))
mensagem.pack(pady=10)

# ================= DASHBOARD =================
def abrir_dashboard():
    dashboard = ctk.CTk()
    dashboard.title('Painel da Loja')
    dashboard.geometry('500x400')

    label = ctk.CTkLabel(
        dashboard,
        text='Bem-vindo ao sistema!',
        font=('Arial', 24)
    )
    label.pack(pady=50)

    dashboard.mainloop()

# ================= LOGIN =================
def login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND senha=?",
        (usuario, senha)
    )

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        mensagem.configure(text='Login realizado!', text_color='green')
        app.after(800, lambda: (app.destroy(), abrir_dashboard()))
    else:
        mensagem.configure(text='Usuário ou senha inválidos', text_color='red')

# ================= ENTER =================
def login_com_enter(event):
    login()

botao = ctk.CTkButton(app, text='Entrar', command=login)
botao.pack(pady=20)

app.bind('<Return>', login_com_enter)

app.mainloop()
