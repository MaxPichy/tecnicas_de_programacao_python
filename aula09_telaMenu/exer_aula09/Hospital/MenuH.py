import tkinter as tk
from tkinter import Menu, Label, Button, messagebox
import subprocess
import sys
import os

try:
    from PIL import Image, ImageTk
except:
    os.system(f'"{sys.executable}" -m pip install pillow')
    from PIL import Image, ImageTk

class MenuH:
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title("MENU HOSPITAL")

        self.largura = 1000
        self.altura = 700

        self.centralizar_tela()
        self.carregar_imagem_fundo()
        self.criar_menu()
        self.carregar_img()
        self.criar_botoes()

        self.tela.mainloop()

    # CENTRALIZAR TELA   
    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        print(largura_screen, altura_screen)
        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        self.tela.resizable(False, False)
 
    # IMAGEM FUNDO   
    def carregar_imagem_fundo(self):
        try:
            imagem = Image.open('icones/fundo_hospital.webp')
            imagem = imagem.resize((1000, 700))
            self.imagem_fundo = ImageTk.PhotoImage(imagem)

            self.lbl_fundo = Label(self.tela, image=self.imagem_fundo)
            self.lbl_fundo.place(x=0, y=0)
        except (FileNotFoundError, EOFError):
            self.tela.configure(bg="#afcfe4")

    # CRIAR MENU   
    def criar_menu(self):
        barra_menus = Menu(self.tela)
        opcoes_menus_arquivos = Menu(barra_menus, tearoff=0)
        opcoes_menus_gestao = Menu(barra_menus, tearoff=0)
        opcoes_novo = Menu(opcoes_menus_arquivos, tearoff=0)

        barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
        opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo)

        opcoes_novo.add_command(label="Cadastrar Consulta", command=self.abrir_consultas)
        opcoes_novo.add_command(label="Cadastrar Paciente", command=self.abrir_pacientes)

        opcoes_menus_arquivos.add_command(label="Abrir")
        opcoes_menus_arquivos.add_command(label="Salvar")

        opcoes_menus_arquivos.add_separator()
        opcoes_menus_arquivos.add_command(label="Sair", command=self.logout)

        barra_menus.add_cascade(label="Gestão", menu=opcoes_menus_gestao)
        opcoes_menus_gestao.add_command(label="Consultas", command=self.abrir_consultas)
        opcoes_menus_gestao.add_command(label="Pacientes", command=self.abrir_pacientes)
        opcoes_menus_gestao.add_command(label="Tratamentos", command=self.abrir_tratamentos)
        
        self.tela.config(menu=barra_menus)

    # ÍCONES
    def carregar_img(self):
        self.icone_consultas = self.carregar_png("icones/consulta.png", 80, 80)
        self.icone_pacientes = self.carregar_png("icones/paciente.png", 80, 80)
        self.icone_tratamentos = self.carregar_png("icones/tratamento.png", 80, 80)
        self.icone_logout = self.carregar_png("icones/logout.png", 80, 80)

    def carregar_png(self, caminho, largura, altura):
        if os.path.exists(caminho):
            try:
                img = Image.open(caminho)
                img = img.resize((largura, altura))
                return ImageTk.PhotoImage(img)
            except:
                return None
        return None
    
    def criar_placeholder(self, largura, altura, texto):
        from PIL import ImageDraw, ImageFont
        
        img = Image.new('RGBA', (largura, altura), color=(100, 149, 237, 255))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", int(largura/2))
        except:
            font = ImageFont.load_default()
        
        # Centraliza o texto
        bbox = draw.textbbox((0, 0), texto, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = ((largura - text_width)/2, (altura - text_height)/2)
        draw.text(position, texto, fill="white", font=font)
        return ImageTk.PhotoImage(img)

    # BOTÕES   
    def criar_botoes(self):
        Button(self.tela, text="Consultas", image=self.icone_consultas, 
               compound="top", command=self.abrir_consultas, width=120, height=100).place(x=100, y=200)

        Button(self.tela, text="Pacientes", image=self.icone_pacientes, 
               compound="top", command=self.abrir_pacientes, width=120, height=100).place(x=320, y=200)

        Button(self.tela, text="Tratamentos", image=self.icone_tratamentos, 
               compound="top", command=self.abrir_tratamentos, width=120, height=100).place(x=540, y=200)

        Button(self.tela, text="Logout", image=self.icone_logout, 
               compound="top", command=self.logout, width=120, height=100).place(x=760, y=200)
 
    # MÉTODOS PARA CHAMAR TELAS
    def abrir_consultas(self):
        try:
            subprocess.run([sys.executable, 'ConsultasH.py'])
        except FileNotFoundError:
            messagebox.showinfo("Aviso", "Módulo de Consultas em desenvolvimento")
       
    def abrir_pacientes(self):
        try:
            subprocess.run([sys.executable, 'PacientesH.py'])
        except FileNotFoundError:
            messagebox.showinfo("Aviso", "Módulo de Pacientes em desenvolvimento")
        
    def abrir_tratamentos(self):
        try:
            subprocess.run([sys.executable, 'TratamentosH.py'])
        except FileNotFoundError:
            messagebox.showinfo("Aviso", "Módulo de Tratamentos em desenvolvimento")
        
    def logout(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair do sistema?")
        if resposta:
            self.tela.destroy()
            try:
                subprocess.run([sys.executable, 'LoginH.py'])
            except FileNotFoundError:
                pass

# EXECUTAR
if __name__ == "__main__":
    MenuH()