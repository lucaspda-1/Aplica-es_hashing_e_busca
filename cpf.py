from random import randint, choice
import string
import timeit

# Dicionário dos códigos fiscais por estado
codigos_fiscais = {
    1: ('DF', 'GO', 'MT', 'MS', 'TO'),
    2: ('AC', 'AP', 'AM', 'PA', 'RO', 'RR'),
    3: ('CE', 'MA', 'PI'),
    4: ('AL', 'PB', 'PE', 'RN'),
    5: ('BA', 'SE'),
    6: 'MG',
    7: ('ES', 'RJ'),
    8: 'SP',
    9: ('PR', 'SC'),
    0: 'RS'
}

def validar(sequence, estado=False):
    # Obter números da sequência do CPF; ignorar outros caracteres
    cpf = [int(char) for char in sequence if char.isdigit()]

    # Verificar se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os números são iguais, por exemplo, '111.111.111-11'
    # Essas sequências de CPFs são inválidas, embora passem nas validações de checksum
    if cpf == cpf[::-1]:
        return False
    
    # Validar dígitos de checksum
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    
    # Obter estado de origem
    if estado:
        codigo = cpf[8]
        print(f'Região fiscal: {", ".join(codigos_fiscais[codigo])}')

    return True

def gerar_dados_pessoais():
    # Geração de nome aleatório
    nome = ''.join(choice(string.ascii_uppercase) for _ in range(6))

    # Geração de número de telefone aleatório
    telefone = '({}) {}-{}'.format(randint(10, 99), randint(1000, 9999), randint(1000, 9999))

    # Geração de senha aleatória
    senha = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))

    return nome, telefone, senha


def gerar(estado_origem=None):
    # Gerar os primeiros dígitos (e garantir que não sejam todos iguais)
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break
    
    # O usuário pode informar o estado de origem digitando a abreviação do estado.
    # Se a entrada não for válida, o programa irá apenas gerar um CPF aleatório.
    if estado_origem is not None:
        if estado_origem.isalpha and len(estado_origem) == 2:
            for k, v in codigos_fiscais.items():
                if estado_origem in v:
                    cpf[8] = k

    # Gerar os dígitos de checksum
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    # Retornar CPF como string
    cpf_string = ''.join(map(str, cpf))

    # Gerar dados pessoais
    nome,telefone, senha = gerar_dados_pessoais()

    return cpf_string, nome,telefone, senha


