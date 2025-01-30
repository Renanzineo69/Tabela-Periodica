import tkinter as tk
from tkinter import messagebox
import json
import os

# Função para exibir os detalhes do elemento em uma janela personalizada
def show_details_custom(element_id):
    try:
        element = elements_data[element_id]
        
        # Obter a cor correspondente à categoria do elemento
        header_color = get_element_color(element['category'])
        
        # Criar uma nova janela para os detalhes
        details_window = tk.Toplevel()
        details_window.title(f"Detalhes de {element['name']}")
        details_window.config(bg='#EAEAEA')
        details_window.resizable(False, False)  # Impede a mudança de tamanho
        set_icon(details_window)

        # Centralizar a janela de detalhes
        window_width = 400
        window_height = 500
        screen_width = details_window.winfo_screenwidth()
        screen_height = details_window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        details_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        # Cabeçalho com a cor da categoria do elemento
        header_label = tk.Label(details_window, text=f"Detalhes do Elemento: {element['name']}", 
                                font=("Helvetica", 16, "bold"), bg=header_color, fg="white", anchor="w", padx=20, pady=10)
        header_label.pack(fill='x')

        # Criar as labels para cada campo de informação com mais estilo
        info_label = tk.Label(details_window, text=f"Símbolo: {element['symbol']}", bg="#EAEAEA", font=("Arial", 12, "bold"), anchor="w", padx=20, pady=5, fg="#333333")
        info_label.pack(padx=20, anchor="w")

        atomic_number_label = tk.Label(details_window, text=f"Número Atômico: {element['atomic_number']}", bg="#EAEAEA", font=("Arial", 12), anchor="w", padx=20, pady=5, fg="#333333")
        atomic_number_label.pack(padx=20, anchor="w")

        atomic_mass_label = tk.Label(details_window, text=f"Massa Atômica: {element['atomic_mass']}", bg="#EAEAEA", font=("Arial", 12), anchor="w", padx=20, pady=5, fg="#333333")
        atomic_mass_label.pack(padx=20, anchor="w")

        group_label = tk.Label(details_window, text=f"Grupo: {element['group']}", bg="#EAEAEA", font=("Arial", 12), anchor="w", padx=20, pady=5, fg="#333333")
        group_label.pack(padx=20, anchor="w")

        period_label = tk.Label(details_window, text=f"Período: {element['period']}", bg="#EAEAEA", font=("Arial", 12), anchor="w", padx=20, pady=5, fg="#333333")
        period_label.pack(padx=20, anchor="w")

        category_label = tk.Label(details_window, text=f"Categoria: {element['category']}", bg="#EAEAEA", font=("Arial", 12, "italic"), anchor="w", padx=20, pady=5, fg="#333333")
        category_label.pack(padx=20, anchor="w")

        # Descrição com 'wraplength' para ajustar o texto e melhor estética
        description_label = tk.Label(details_window, text=f"Descrição: {element['description']}", bg="#EAEAEA", font=("Arial", 11), anchor="w", padx=20, wraplength=300, justify="left", fg="#333333")
        description_label.pack(padx=20, pady=10, fill='both', expand=True)

        # Botão de fechar mais estilizado
        close_button = tk.Button(details_window, text="Fechar", command=details_window.destroy, font=("Arial", 12, "bold"), bg="#4A90E2", fg="white", relief="flat", width=15, height=2)
        close_button.pack(pady=20)

    except KeyError:
        messagebox.showerror("Erro", f"Elemento com ID {element_id} não encontrado!")

# Função para atribuir cores conforme a categoria
def get_element_color(category):
    colors = {
        "Metal alcalino": "#FFEB3B",  # Amarelo claro
        "Metal alcalino-terroso": "#FFC107",  # Amarelo escuro
        "Gás nobre": "#64B5F6",  # Azul claro
        "Metaloide": "#A5D6A7",  # Verde claro
        "Halogênio": "#FF7043",  # Laranja
        "Não-metal": "#7CA67E",  # Verde claro
        "Metal de transição": "#90A4AE",  # Cinza
        "Metal" : "#A7C9F9", # Azul bebê
        "Lantanídeos": "#9F0081",  # Roxo
        "Actinídios" : "#FE60C4"  # Rosa 
    }
    return colors.get(category, "#FFFFFF")  # Branco como padrão, caso não tenha categoria

# Função que define o ícone da janela, se o caminho do ícone existir
def set_icon(root, icon_path="images/favicon.ico"):
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

# Função para carregar os dados dos elementos químicos
def load_data():
    try:
        with open("elementos.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"Dados carregados: {len(data)} elementos")  # Depuração para verificar o número de elementos carregados
            return data
    except Exception as e:
        print(f"Erro ao carregar o arquivo JSON: {e}")
        return {}

# Função para criar a tabela
def create_table(root):
    colunas = 18  # Total de colunas (grupos)

    # Ajuste de tamanho dos botões
    button_width = 8  # Largura do botão
    button_height = 3  # Altura do botão

    column_position = 4  # Para os Lantanídeos e Actinídeos

    for element_id, element_data in elements_data.items():

        period = int(element_data["period"])
        group = int(element_data["group"])

        # Ajuste para os Lantanídeos (ID de 57 a 71) - linha 9
        if 57 <= element_data["atomic_number"] <= 71:  # Lantanídeos
            row = 9  # Colocar os Lantanídeos abaixo da tabela principal (linha 9)

            # Colocar os elementos Lantanídeos em colunas consecutivas
            element_button = tk.Button(root, text=f"{element_data['symbol']}", font=("Comic Sans MS", 9), width=button_width, height=button_height,
                                        bg=get_element_color(element_data["category"]),
                                        command=lambda e=element_id: show_details_custom(e))
            element_button.grid(row=row, column=column_position)  # Colocar o botão na coluna
            column_position += 1  # Incrementa a posição da coluna para o próximo elemento

        # Ajuste para os Actinídeos (ID de 89 a 103) - linha 10
        elif 89 <= element_data["atomic_number"] <= 103:  # Actinídeos
            row = 10 # Colocar os Actinídeos abaixo dos Lantanídeos (linha 10)

            # Colocar os elementos Actinídeos em colunas consecutivas
            element_button = tk.Button(root, text=f"{element_data['symbol']}", font=("Comic Sans MS", 9), width=button_width, height=button_height,
                                        bg=get_element_color(element_data["category"]),
                                        command=lambda e=element_id: show_details_custom(e))
            element_button.grid(row=row, column=column_position - 15)  # Colocar o botão na coluna
            column_position += 1  # Incrementa a posição da coluna para o próximo elemento

        else:
            row = period  # Manter os outros elementos conforme o período e grupo
            element_button = tk.Button(root, text=f"{element_data['symbol']}", font=("Comic Sans MS", 9), width=button_width, height=button_height,
                                        bg=get_element_color(element_data["category"]),
                                        command=lambda e=element_id: show_details_custom(e))
            element_button.grid(row=row, column=group)  # Colocar o botão na posição correta

    root.config(bg='#2b2b2b')  # Cor de fundo da tela principal
    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - root_height / 2)
    position_right = int(screen_width / 2 - root_width / 2)

    root.geometry(f'{root_width}x{root_height}+{position_right}+{position_top}')  # Ajustar posição e tamanho da janela

# Criar a janela principal
root = tk.Tk()
root.title("Tabela Periódica")
set_icon(root)

# Carregar os dados dos elementos
elements_data = load_data()

# Criar a tabela periódica
create_table(root)

# Iniciar o loop principal da interface
root.mainloop()