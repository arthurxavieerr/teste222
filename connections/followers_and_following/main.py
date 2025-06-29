import re

# Função para extrair nomes de usuário do HTML do Instagram (padrão conforme exemplo)
def extrair_usuarios(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
    # Extrai padrões do tipo https://www.instagram.com/usuario"
    return set(re.findall(r'https://www.instagram.com/([a-zA-Z0-9_.]+)"', conteudo))

followers = extrair_usuarios("followers_1.html")
following = extrair_usuarios("following.html")

nao_segue_de_volta = following - followers

print("Usuários que você segue e não te seguem de volta:")
for usuario in sorted(nao_segue_de_volta):
    print(usuario)