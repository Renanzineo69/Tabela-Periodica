import tkinter as tk
from tkinter import messagebox
import json

# Carregar os dados dos elementos químicos
def load_data():
    try:
        with open("elementos.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"Dados carregados: {data}")  # Depuração para verificar os dados carregados
            return data
    except Exception as e:
        print(f"Erro ao carregar o arquivo JSON: {e}")
        return {}

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

# Criar a interface gráfica
def create_table(root):
    colunas = 18  # Total de colunas (grupos)
    row = 1  # Começar na primeira linha
    col = 1  # Começar na primeira coluna
    
    # Iterar sobre os dados dos elementos no JSON
    for element_id, element_data in elements_data.items():
        # Colocar os elementos de acordo com seu período e grupo
        period = int(element_data["period"])
        group = int(element_data["group"])

        # Criar um botão para cada elemento
        element_button = tk.Button(root, text=f"{element_data['name']}", width=5, height=2,
                                   command=lambda e=element_id: show_details(e))
        element_button.grid(row=period, column=group)  # Colocar o botão na posição correta

# Criar a janela principal
root = tk.Tk()
root.title("Tabela Periódica")

# Carregar os dados dos elementos
elements_data = load_data()

# Criar a tabela periódica
create_table(root)

# Iniciar o loop principal da interface
root.mainloop()

