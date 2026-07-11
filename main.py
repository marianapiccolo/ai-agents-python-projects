from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

cliente = OpenAI()

resposta = cliente.chat.completions.create(
    messages=[{"role": "user", "content": "Por que python é uma boa linguagem de programação?"}],
    model="gpt-4o"
)

mensagem_resposta = resposta.choices[0].message
conteudo_mensagem = mensagem_resposta.content
role_mensagem = mensagem_resposta.role
print("Role:", role_mensagem)
print("Content:", conteudo_mensagem)