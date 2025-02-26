import json

def load_data(json_path="elementos.json"):
    """ Carrega os dados dos elementos químicos a partir de um arquivo JSON """
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"Dados carregados: {len(data)} elementos")
            return data
    except Exception as e:
        print(f"Erro ao carregar o arquivo JSON: {e}")
        return {}
