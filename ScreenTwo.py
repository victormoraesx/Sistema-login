from kivymd.uix.screen import MDScreen
import mysql.connector
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout


con = mysql.connector.connect(host='localhost', database='banco_teste3', user='root', password='973985512j')

class ScreenTwoView(MDScreen):
    text = StringProperty()
    hint_text = StringProperty()
    def verificarSenhaConfirmar(self):
        global janela1
        senha = self.ids.senhaCadastro.text
        senhaConfirmar = self.ids.confirmarSenhaCadastro.text
         
        if senha == senhaConfirmar:
            self.registrarUsuario()
        else:
            print("Senha incorreta")
        return

    def criarTabela(self):
        cursor = con.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS banco_Usuarios")

        cursor.execute("CREATE TABLE IF NOT EXISTS tbl_usuarios3 ("
               "nome VARCHAR(255),"
               "senha VARCHAR(255),"
               "email VARCHAR(255),"
               "numero INT"
               ")")
        
        cursor.close()

    def registrarUsuario(self):
        nome = self.ids.nomeCadastro.text
        senha = self.ids.senhaCadastro.text
        email = self.ids.emailCadastro.text
        numero = self.ids.telefoneCadastro.text

        if nome and senha and email and numero > '':
            comandoSql = """ INSERT INTO tbl_usuarios (nome, senha, email, numero) VALUES ( """
            dadosUsuario = '\'' + nome + '\',' + '\'' + senha  + '\',' + '\'' + email + '\',' + '\'' + '+5511' + numero + '\'' + ')'
            comando = comandoSql + dadosUsuario
            cursor = con.cursor()
            cursor.execute(comando)
            con.commit()
            print(cursor.rowcount, "Informações adicionadas")
            cursor.close
            self.resetarDadosCadastro()
        elif nome or senha or email or numero == '':
            print("Falta informações")

    def resetarDadosCadastro(self):
        self.ids.nomeCadastro.text = ""
        self.ids.senhaCadastro.text = ""
        self.ids.emailCadastro.text = ""
        self.ids.telefoneCadastro.text = ""
        self.ids.confirmarSenhaCadastro.text = ""