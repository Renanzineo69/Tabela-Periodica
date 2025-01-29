import tkinter as tk
from tkinter import messagebox
import json

# Carregar os dados dos elementos químicos
def load_data():
    try:
        with open("elementos.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"Dados carregados: {len(data)} elementos")  # Depuração para verificar o número de elementos carregados
            return data
    except Exception as e:
        print(f"Erro ao carregar o arquivo JSON: {e}")
        return {}

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
        "Metal" : "#A7C9F9", #Azul bebê
        "Lantanídeos": "#9F0081",  # Roxo
        "Actinídios" : "#FE60C4"  # Rosa 
    }
    return colors.get(category, "#FFFFFF")  # Branco como padrão, caso não tenha categoria

# Exibir detalhes do elemento
def show_details(element_id):
    try:
        element = elements_data[element_id]
        details = f"Nome: {element['name']}\n"
        details += f"Símbolo: {element['symbol']}\n"
        details += f"Número Atômico: {element['atomic_number']}\n"
        details += f"Massa Atômica: {element['atomic_mass']}\n"
        details += f"Grupo: {element['group']}\n"
        details += f"Período: {element['period']}\n"
        details += f"Categoria: {element['category']}\n"
        details += f"Descrição: {element['description']}"

        # Exibir os detalhes em uma caixa de mensagem
        messagebox.showinfo("Detalhes do Elemento", details)
    except KeyError:
        messagebox.showerror("Erro", f"Elemento com ID {element_id} não encontrado!")

def create_table(root):
    colunas = 18  # Total de colunas (grupos)

    # Ajuste de tamanho dos botões
    button_width = 8  # Largura do botão
    button_height = 3  # Altura do botão

    # Organizar os botões para os elementos na tabela periódica
    column_position = 4  # Para os Lantanídeos e Actinídeos

    for element_id, element_data in elements_data.items():

        period = int(element_data["period"])
        group = int(element_data["group"])

        # Ajuste para os Lantanídeos (ID de 57 a 71) - linha 9
        if 57 <= element_data["atomic_number"] <= 71:  # Lantanídeos
            row = 9  # Colocar os Lantanídeos abaixo da tabela principal (linha 9)

            # Colocar os elementos Lantanídeos em colunas consecutivas
            element_button = tk.Button(root, text=f"{element_data['name']}", width=button_width, height=button_height,
                                       bg=get_element_color(element_data["category"]),
                                       command=lambda e=element_id: show_details(e))
            element_button.grid(row=row, column=column_position)  # Colocar o botão na coluna
            column_position += 1  # Incrementa a posição da coluna para o próximo elemento

        # Ajuste para os Actinídeos (ID de 89 a 103) - linha 10
        elif 89 <= element_data["atomic_number"] <= 103:  # Actinídeos
            row = 10  # Colocar os Actinídeos abaixo dos Lantanídeos (linha 10)

            # Colocar os elementos Actinídeos em colunas consecutivas
            element_button = tk.Button(root, text=f"{element_data['name']}", width=button_width, height=button_height,
                                       bg=get_element_color(element_data["category"]),
                                       command=lambda e=element_id: show_details(e))
            element_button.grid(row=row, column=column_position - 15)  # Colocar o botão na coluna
            column_position += 1  # Incrementa a posição da coluna para o próximo elemento

        else:
            row = period  # Manter os outros elementos conforme o período e grupo
            element_button = tk.Button(root, text=f"{element_data['name']}", width=button_width, height=button_height,
                                       bg=get_element_color(element_data["category"]),
                                       command=lambda e=element_id: show_details(e))
            element_button.grid(row=row, column=group)  # Colocar o botão na posição correta

# Criar a janela principal
root = tk.Tk()
root.title("Tabela Periódica")

# Carregar os dados dos elementos
elements_data = load_data()

# Criar a tabela periódica
create_table(root)

# Iniciar o loop principal da interface
root.mainloop()
