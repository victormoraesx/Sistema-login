from kivymd.uix.screen import MDScreen
#import pywhatkit
import random
import mysql.connector

con = mysql.connector.connect(host='localhost', database='banco_teste3', user='root', password='973985512j')

class ScreenThreeView(MDScreen):
    def enviarCodigo(self):

        global codigo
        global numero

        numeros = '0123456789'
        codigo = "".join(random.sample(numeros, 3))

        numero = self.ids.telefoneTrocarSenha.text
        self.ids.telefoneTrocarSenha.text = ""
        try:
            con = mysql.connector.connect(host='localhost', database='banco_teste3', user='root', password='973985512j')
            cursor = con.cursor()
            cursor.execute(f" SELECT DISTINCT numero FROM tbl_usuarios WHERE numero = '{numero}';")
            linha = cursor.fetchall()
            valorNumero = linha[0][0] 

            if valorNumero == numero:
                #pywhatkit.sendwhatmsg_instantly(f'{numero}', codigo)
                print(codigo)
            else:
                print("Numero errado")
            cursor.close()
        except:
            pass
        

    def validarCodigo(self):

        global codigoOk

        codigoValidar = ''
        codigoVerificador = self.ids.codigoVerificador.text
        codigoValidar = codigo

        if codigoValidar == codigoVerificador:
            self.ids.tela1.size_hint = (0, 0)
            self.ids.tela2.size_hint = (.5, .9)
            self.ids.codigoVerificador.helper_text = ""
            self.ids.codigoVerificador.text = ""
            codigoOk = "S"
        elif codigoValidar != codigoVerificador:
            self.ids.codigoVerificador.helper_text = "Código incorreto"
        elif codigoValidar == 0 or codigoValidar == "":
            self.ids.codigoVerificador.helper_text = "Digite o código"

    def redefinirSenha(self):
        if codigoOk == "S":
            numeroUsuario = numero
            senha = self.ids.senhaRedefinir.text

            comandoSql = f"""UPDATE tbl_usuarios
            SET	senha = '{senha}'
            WHERE numero = '{numeroUsuario}';"""
            cursor = con.cursor()
            cursor.execute(comandoSql)
            con.commit()
            print(cursor.rowcount, "Informações alteradas")
            cursor.close
        self.ids.senhaRedefinir.text = ""
         
