class Caesar:
    def __init__(self) -> None:
        pass
    def encrypt(self, message, shift):
        encrypted_message = ""
        for char in message:
            encrypted_char = chr((ord(char) + shift) % 256)
            encrypted_message += encrypted_char
        return encrypted_message
    
    def decrypt(self, encrypted_message, shift):
        decrypted_message = ""
        for char in encrypted_message:
            decrypted_char = chr((ord(char) - shift) % 256)
            decrypted_message += decrypted_char
        return decrypted_message