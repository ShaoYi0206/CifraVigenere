def vigenere_encrypt(msg, key):
    msg_encrypt = ""
    key_index = 0
    
    for char in msg:
        if 32 <= ord(char) <= 127: 
            shift  = ord(key[key_index]) - 32
            char_encrypt = chr(((ord(char) - 32 + shift) % 96) + 32)
            
            msg_encrypt += char_encrypt
            
            key_index = (key_index + 1) % len(key)            
            
    return msg_encrypt

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


msg = input(str("Digite uma mensagem: "))
key = "KEY"

msg_encrypt = vigenere_encrypt(msg, key)
print("Mensagem Cifrada: ", msg_encrypt)
 
msg_decrypt = vigenere_decrypt(msg_encrypt, key)
print("Mensagem Decifrada: ", msg_decrypt)
