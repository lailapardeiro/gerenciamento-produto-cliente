import base64

usuarioLogin = "admin"
senhaLogin = b'MTIz'

class Autenticacao:

  def autenticar(self, usuario, senha):
    senhaCriptografada = base64.b64encode(senha.encode())

    if usuario == usuarioLogin and senhaCriptografada == senhaLogin:
      print("Acesso permitido!")
      return True
    else:
      print("Acesso negado! Usuário/senha invalido")
      return False