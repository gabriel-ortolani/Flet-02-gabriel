import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 30

    def atualizar_cores(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            campo_altura.border_color = ft.Colors.WHITE
            campo_peso.border_color = ft.Colors.WHITE

        else:
            campo_altura.border_color = ft.Colors.BLACK
            campo_peso.border_color = ft.Colors.BLACK
        page.update()
    # Função para alternar tema
    def trocar_tema(e):
        if switch_tema.value:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        atualizar_cores(e)
        page.update()

    # Título e tema
    titulo = ft.Text("Calculadora de IMC", size=30, weight=ft.FontWeight.BOLD)
    switch_tema = ft.Switch(label="Tema escuro", on_change=trocar_tema)

    cabecalho = ft.Row(
        [switch_tema],
        alignment=ft.MainAxisAlignment.END
    )

    subtitulo = ft.Text("Informe seus dados abaixo:", size=18)

    # Campos de entrada
    campo_peso = ft.TextField(
        label="Peso (kg)",
        width=250,
        text_align=ft.TextAlign.CENTER,
        value=""
    )

    campo_altura = ft.TextField(
        label="Altura (m)",
        width=250,
        text_align=ft.TextAlign.CENTER,
        value=""
    )

    # Mensagem de resultado
    mensagem = ft.Text(
        "Seu resultado será exibido aqui!",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_400,
        text_align=ft.TextAlign.CENTER
    )

    # Função de cálculo
    def calcular_imc(e):
        try:
            peso = float(campo_peso.value.replace(',', '.'))
            altura = float(campo_altura.value.replace(',', '.'))

            if peso <= 0 or altura <= 0:
                mensagem.value = "Por favor, insira valores válidos!"
                mensagem.color = ft.Colors.RED
            else:
                imc = peso / (altura ** 2)
                if imc < 18.5:
                    mensagem.value = f"Seu IMC é {imc:.2f}. Abaixo do peso."
                    mensagem.color = ft.Colors.BLUE
                elif 18.5 <= imc < 24.9:
                    mensagem.value = f"Seu IMC é {imc:.2f}. Peso normal."
                    mensagem.color = ft.Colors.GREEN
                elif 25 <= imc < 29.9:
                    mensagem.value = f"Seu IMC é {imc:.2f}. Sobrepeso."
                    mensagem.color = ft.Colors.ORANGE
                else:
                    mensagem.value = f"Seu IMC é {imc:.2f}. Obesidade."
                    mensagem.color = ft.Colors.RED
        except ValueError:
            mensagem.value = "Digite números válidos."
            mensagem.color = ft.Colors.RED

        page.update()

    # Função de limpar
    def limpar_campos(e):
        campo_peso.value = ""
        campo_altura.value = ""
        mensagem.value = "Seu resultado será exibido aqui!"
        mensagem.color = ft.Colors.BLUE_400
        page.update()

    # Botões
    botao_calcular = ft.OutlinedButton(text="Calcular IMC", on_click=calcular_imc)
    botao_limpar = ft.OutlinedButton(text="Limpar", on_click=limpar_campos)

    botoes = ft.Row([botao_calcular, botao_limpar], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    # Layout final
    layout = ft.Column(
        controls=[
            cabecalho,
            titulo,
            subtitulo,
            campo_peso,
            campo_altura,
            mensagem,
            botoes,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25,
    )

    page.add(layout)

ft.app(target=main)
