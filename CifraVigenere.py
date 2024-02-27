def vigenere_encrypt(msg, key):
    msg_encrypt = ""
    len_key = len(key)
    
    for i in range(len(msg)):
        # Convertendo caracteres para valores numéricos de 0 a n-1
        value_char = ord(msg[i])
        value_key  = ord(key[i % len_key]) 

        # Calculando o valor cifrado
        value_encrypt = (value_char + value_key)

        # Convertendo o valor cifrado de volta para o caracter correpondentewe
        msg_encrypt += chr(value_encrypt)

    return msg_encrypt

def vigenere_decrypt(msg_cipher, key):
    msg_decrypt = ""
    len_key = len(key)

    for i in range(len(msg_cipher)):
        # Convertendo caracteres cifrados para valores númericos de 0 a n-1
        value_char = ord(msg_cipher[i]) 
        value_key = ord(key[i % len_key])

        # Calculando o valor decifrado
        value_decrypt = (value_char - value_key)

        # Convertendo o valor decifrado de volta para o caractere correspondente
        msg_decrypt += chr(value_decrypt)

    return msg_decrypt


msg = input(str("Digite uma mensagem: "))
key = "CHAVE"

msg_encrypt = vigenere_encrypt(msg, key)
print("Mensagem Cifrada: ", msg_encrypt)
 
msg_decrypt = vigenere_decrypt(msg_encrypt, key)
print("Mensagem Decifrada: ", msg_decrypt)