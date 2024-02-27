def find_vigenere_key(ciphertext, key_length):
    # Lista de contadores para cada posição da chave
    key_counters = [[] for _ in range(key_length)]
    
    # Iterar sobre o texto cifrado e contar a frequência dos caracteres em cada posição da chave
    for i, char in enumerate(ciphertext):
        key_index = i % key_length
        if char != ' ':
            key_counters[key_index].append(char)
    
    # Encontrar o caractere mais frequente em cada posição da chave
    key = ''
    for counter in key_counters:
        # Contar a frequência de cada caractere na posição da chave
        char_frequency = {}
        for char in counter:
            char_frequency[char] = char_frequency.get(char, 0) + 1
        
        # Encontrar o caractere mais frequente
        most_common_char = max(char_frequency, key=char_frequency.get)
        
        # Adicionar o caractere mais frequente à chave
        key += most_common_char
    
    return key

def vigenere_decrypt(msg_encrypt, key):
    msg_decrypt = ""
    key_index = 0

    for char in msg_encrypt:
        if 32 <= ord(char) <= 127:
            shift = ord(key[key_index]) - 32
            char_decrypt = chr(((ord(char) - 32 - shift) % 96) + 32)
            
            msg_decrypt += char_decrypt
            key_index = (key_index + 1) % len(key)
            
    return msg_decrypt

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Ler o texto cifrado de um arquivo
filename = 'texto_cripto_chave20.txt'
ciphertext = read_file(filename)

# Tamanho da chave conhecido
key_length = 20

# Encontrar a chave
key = find_vigenere_key(ciphertext, key_length)
print("Chave encontrada:", key)

# Decifrar o texto usando a chave encontrada
plaintext = vigenere_decrypt(ciphertext, key)
print("Texto decifrado:", plaintext)
