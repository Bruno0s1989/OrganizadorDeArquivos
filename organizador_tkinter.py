import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime

def organizar_arquivos(pasta):
    pastas_destino = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt"],
        "Planilhas": [".xlsx", ".csv"],
        "Vídeos": [".mp4", ".mkv", ".avi"],
        "Músicas": [".mp3", ".wav", ".flac"],
        "Outros": []
    }

    
    for pasta_destino in pastas_destino.keys():
        caminho_pasta = os.path.join(pasta, pasta_destino)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

    
    with open(os.path.join(pasta, "log.txt"), "a", encoding="utf-8") as log_file:
        log_file.write(f"Organização iniciada em: {datetime.now()}\n")

        
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)

            
            if os.path.isdir(caminho_arquivo) or arquivo.startswith('.'):
                continue

            
            if not os.path.exists(caminho_arquivo):
                log_file.write(f"Arquivo não encontrado: {caminho_arquivo}\n")
                continue

            
            _, extensao = os.path.splitext(arquivo)

            
            movido = False
            for pasta_destino, extensoes in pastas_destino.items():
                if extensao.lower() in extensoes:
                    shutil.move(caminho_arquivo, os.path.join(pasta, pasta_destino, arquivo))
                    log_file.write(f"Movido: {arquivo} -> {pasta_destino}\n")
                    movido = True
                    break

            
            if not movido:
                shutil.move(caminho_arquivo, os.path.join(pasta, "Outros", arquivo))
                log_file.write(f"Movido: {arquivo} -> Outros\n")

        log_file.write(f"Organização concluída em: {datetime.now()}\n\n")

    messagebox.showinfo("Concluído", "Organização de arquivos finalizada!")


def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        organizar_arquivos(pasta_selecionada)


def sobre():
    messagebox.showinfo("Sobre", "Organizador de Arquivos\nVersão 1.0\nDesenvolvido por [Bruno Silva]")


if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Organizador de Arquivos")
    root.geometry("400x150")

    
    style = ttk.Style()
    style.configure("TButton", padding=6, font=("Arial", 10))

    
    frame = ttk.Frame(root)
    frame.pack(pady=20)

    
    btn_selecionar = ttk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta)
    btn_selecionar.grid(row=0, column=0, padx=10)

    
    btn_sobre = ttk.Button(frame, text="Sobre", command=sobre)
    btn_sobre.grid(row=0, column=1, padx=10)

    
    btn_sair = ttk.Button(frame, text="Sair", command=root.quit)
    btn_sair.grid(row=0, column=2, padx=10)

    
    root.mainloop()