'''
Semana 3 -> Atividade avaliativa
Gabriele Cardoso das Virgens - 2010840
31/08/2023

'''

MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, key, mode):
    # Definindo o alfabeto utilizado, incluindo caracteres acentuados.
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    # Inicialização da variável para armazenar o resultado da criptografia/descriptografia.
    new_data = ''
    
    # Itera sobre cada caractere no dado de entrada 'data'.
    for c in data:
        # Procura o índice do caractere 'c' no alfabeto.
        index = alphabet.find(c)
        
        # Verifica se o caractere não foi encontrado no alfabeto.
        if index == -1:
            new_data += c  # Se não for encontrado, adiciona o caractere diretamente à saída.
        else:
            # Calcula o novo índice baseado na chave e no modo de operação (criptografar ou descriptografar).
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            
            # Garante que o índice esteja dentro dos limites do alfabeto utilizando operação de módulo.
            new_index = new_index % len(alphabet)
            
            # Adiciona o caractere correspondente ao novo índice à saída.
            new_data += alphabet[new_index:new_index+1]
    
    # Retorna a nova sequência de caracteres resultante da criptografia/descriptografia.
    return new_data


# Tests
key = 7
original = 'a aula de segurança é muito legal'
print('  Original:', original)
ciphered = caesar(original, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = caesar(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)