import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk  # Importando o ttk para usar o Notebook


# Função para exibir os parágrafos encontrados com as palavras-chave
def exibir_paragrafos_com_palavra_chave():
    palavra_chave = simpledialog.askstring("Palavra-chave", "Digite a palavra ou frase para busca:")

    if palavra_chave:  # Verifica se o usuário não deixou o campo vazio
        paragrafos_encontrados = []

        # Buscar nos parágrafos a palavra-chave fornecida
        for i, paragrafo in enumerate(paragrafos):
            if palavra_chave.lower() in paragrafo.text.lower():  # Busca sem diferenciar maiúsculas/minúsculas
                paragrafos_encontrados.append(f"Parágrafo {i + 1}: {paragrafo.text.strip()}")

        if paragrafos_encontrados:
            # Exibe os resultados em abas
            exibir_resultados_em_abas(paragrafos_encontrados)
        else:
            messagebox.showinfo("Nenhuma correspondência", "Nenhum parágrafo encontrado com a palavra-chave.")
    else:
        messagebox.showerror("Erro", "Você deve digitar uma palavra ou frase para busca.")


# Função para exibir os resultados encontrados em abas
def exibir_resultados_em_abas(paragrafos_encontrados):
    # Criando uma nova janela para os resultados
    janela_resultados = tk.Toplevel(root)
    janela_resultados.title("Resultados da Busca")
    janela_resultados.geometry("600x400")  # Definindo o tamanho da janela (largura x altura)

    # Criando o notebook (abas) na nova janela
    notebook = ttk.Notebook(janela_resultados)
    notebook.pack(fill="both", expand=True)

    # Dividindo os resultados em páginas (abas)
    aba_index = 1
    paragrafo_por_aba = 5  # Quantidade de parágrafos por aba (ajuste conforme necessário)
    for i in range(0, len(paragrafos_encontrados), paragrafo_por_aba):
        aba = tk.Frame(notebook)
        notebook.add(aba, text=f"Aba {aba_index}")
        aba_index += 1

        # Exibindo os parágrafos encontrados dentro da aba
        texto_resultados = tk.Text(aba, wrap="word", height=180, width=840)
        texto_resultados.pack(padx=10, pady=10)

        # Adicionando os parágrafos encontrados à área de texto
        for paragrafo in paragrafos_encontrados[i:i + paragrafo_por_aba]:
            texto_resultados.insert(tk.END, paragrafo + "\n\n")

        texto_resultados.config(state=tk.DISABLED)  # Desativa a edição


# Obter os dados do site
url = 'https://cariacica.camarasempapel.com.br/Arquivo/Documents/legislacao/html_impressao/C1372023.html?identificador=30003A004C00'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Obter todos os parágrafos
paragrafos = extracao.find_all('p')

# Criar a janela principal com tkinter
root = tk.Tk()
root.title("Busca por Palavras-chave")
root.geometry("200x100")  # Definindo o tamanho da janela principal

# Botão para iniciar a busca por palavras-chave
botao_busca = tk.Button(root, text="Buscar Palavras-chave", command=exibir_paragrafos_com_palavra_chave)
botao_busca.pack(padx=10, pady=10)

# Iniciar a interface gráfica
root.mainloop()
