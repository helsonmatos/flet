import flet as ft

def main(page):

    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor preencha o seu nome."
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Campo de senha obrigatório."
            page.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")
            page.clean()
            page.add(ft.Text(f"Ola, {nome}\nSeja Bem vindo!"))

    entrada_nome = ft.TextField(label="Digite o seu nome.")
    entrada_senha = ft.TextField(label="Digite a sua senha.")
    
    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("clique em mim", on_click=login)
    )

ft.app(target=main)