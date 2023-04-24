from kivymd.uix.screen import MDScreen
import mysql.connector
from kivy.app import App

con = mysql.connector.connect(host='localhost', database='banco_teste3', user='root', password='973985512j')


class ScreenOneView(MDScreen):
    def exibirAtividade(self):
        email = self.ids.emailLogin.text
        senha = self.ids.senhaLogin.text
        print("Você foi para a segunda tela")
        print(email)
        print(senha)
        return
    
    def verificarStatusUsuario(self):
        email = self.ids.emailLogin.text
        senha = self.ids.senhaLogin.text

        cursor = con.cursor()

        cursor.execute(f"SELECT email FROM tbl_usuarios WHERE email = '{email}'")
        valor = cursor.fetchall()

        if valor == []:
            emailVerificador = 'naoLocalizado'
        else:
            emailVerificador = valor[0][0]

        cursor.execute(f"SELECT senha FROM tbl_usuarios WHERE email = '{email}'")
        valor = cursor.fetchall()

        if valor == []:
            senhaVerificador = "naoLocalizado"
        else:
            senhaVerificador = valor[0][0]

        if email == emailVerificador and senha == senhaVerificador:
            App.get_running_app().root.transition.direction = 'left'
            App.get_running_app().root.current = "s2"
        else:
            print("Verifique o email ou senha")
            

    