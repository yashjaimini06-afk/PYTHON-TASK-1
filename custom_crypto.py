"""
Custom Multi-Layer Encryption-Decryption System
Developed in accordance with Main Flow Internship Guidelines.
No external cryptographic libraries utilized.
"""

def vigenere_cipher(text, key, decrypt=False):
    """Layer 1: Polyalphabetic Substitution Cipher (ASCII 32 to 126)"""
    processed_text = []
    key_length = len(key)
    
    for i, char in enumerate(text):
        char_code = ord(char)
        # Handle only printable ASCII characters
        if 32 <= char_code <= 126:
            key_char = key[i % key_length]
            key_shift = ord(key_char) - 32
            
            if decrypt:
                new_code = 32 + ((char_code - 32 - key_shift) % 95)
            else:
                new_code = 32 + ((char_code - 32 + key_shift) % 95)
            processed_text.append(chr(new_code))
        else:
            processed_text.append(char) # Keep unhandled characters as-is
            
    return "".join(processed_text)


def columnar_transposition_encrypt(text, key):
    """Layer 2: Matrix Transposition (Encryption)"""
    col_count = len(key)
    # Pad string to fit perfectly into matrix dimensions
    pad_len = (col_count - (len(text) % col_count)) % col_count
    padded_text = text + ('\x00' * pad_len)
    
    # Create rows
    rows = [padded_text[i:i+col_count] for i in range(0, len(padded_text), col_count)]
    
    # Sort columns according to key characters
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    ciphertext = ""
    for col_idx, _ in key_order:
        for row in rows:
            ciphertext += row[col_idx]
            
    return ciphertext


def columnar_transposition_decrypt(text, key):
    """Layer 2: Matrix Transposition (Decryption)"""
    col_count = len(key)
    row_count = len(text) // col_count
    
    # Reconstruct columns based on key order
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    # Allocate empty grid space
    matrix = [['' for _ in range(col_count)] for _ in range(row_count)]
    
    text_idx = 0
    for col_idx, _ in key_order:
        for row_idx in range(row_count):
            matrix[row_idx][col_idx] = text[text_idx]
            text_idx += 1
            
    # Read row-wise to get padded plaintext
    decrypted_padded = "".join("".join(row) for row in matrix)
    return decrypted_padded.replace('\x00', '')


def encrypt_system(message, sub_key, trans_key):
    """Pipeline: Substitution followed by Transposition"""
    substitution_stage = vigenere_cipher(message, sub_key, decrypt=False)
    final_ciphertext = columnar_transposition_encrypt(substitution_stage, trans_key)
    return final_ciphertext


def decrypt_system(ciphertext, sub_key, trans_key):
    """Pipeline: Reverse Transposition followed by Reverse Substitution"""
    transposition_stage = columnar_transposition_decrypt(ciphertext, trans_key)
    original_plaintext = vigenere_cipher(transposition_stage, sub_key, decrypt=True)
    return original_plaintext


if __name__ == "__main__":
    print("=== MAIN FLOW CUSTOM SECURITY INTERFACE ===")
    secret_msg = "Main Flow Project Entry #2026! @Internship_Task"
    s_key = "CRYPTO"
    t_key = "MATRIX"
    
    print(f"\nOriginal Message : {secret_msg}")
    print(f"Substitution Key : {s_key} | Transposition Key: {t_key}")
    
    # Execution
    encrypted = encrypt_system(secret_msg, s_key, t_key)
    print(f"Encrypted Output : {repr(encrypted)}")
    
    decrypted = decrypt_system(encrypted, s_key, t_key)
    print(f"Decrypted Output : {decrypted}")