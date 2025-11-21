def encrypt(pwd):
    encrypted = ""
    for ch in pwd:
        ascii_val = ord(ch)
        # range 65-90
        if 'A' <= ch <= 'Z':
            shifted = ascii_val + 7
            if shifted > ord('Z'):
                shifted -= 26
            encrypted += chr(shifted)
        # range 97-122
        elif 'a' <= ch <= 'z':
            shifted= ascii_val + 14
            if shifted > ord('z'):
                shifted -= 26
            encrypted += chr(shifted)
        # range 48-57
        elif '0' <= ch <= '9':
            shifted = ascii_val + 3
            if shifted > ord('9'):
                shifted -= 10
            encrypted += chr(shifted)
        else:
            shifted = ascii_val + 9
            # range 32-47
            if 32 <= ascii_val <= 47:
                if shifted > 47:
                    shifted = 32 + (shifted - 48)
                encrypted += chr(shifted)
            # range 58-64
            elif 58 <= ascii_val <= 64:
                if shifted > 64:
                    shifted = 58 + (shifted - 65)
                encrypted += chr(shifted)
            # range 91-96
            elif 91 <= ascii_val <= 96:
                if shifted > 96:
                    shifted = 91 + (shifted - 97)
                encrypted += chr(shifted)
            # range 123-126
            elif 123 <= ascii_val <= 126:
                if shifted > 126:
                    shifted = 123 + (shifted - 127)
                encrypted += chr(shifted)
            else:
                if shifted > 126:
                    shifted = 32 + (shifted - 127)
                encrypted += chr(shifted)
    return encrypted
        

def decrypt(pwd):
    decrypted = ""
    for ch in pwd:
        ascii_val = ord(ch)
        # range 65-90
        if 'A' <= ch <= 'Z':
            shifted = ascii_val - 7
            if shifted < ord('A'):
                shifted += 26
            decrypted += chr(shifted)
        # range 97-122
        elif 'a' <= ch <= 'z':
            shifted= ascii_val - 14
            if shifted < ord('a'):
                shifted += 26
            decrypted += chr(shifted)
        # range 48-57
        elif '0' <= ch <= '9':
            shifted = ascii_val - 3
            if shifted < ord('0'):
                shifted += 10
            decrypted += chr(shifted)
        else:                           
            shifted = ascii_val - 9
             # range 32-47
            if 32 <= ascii_val <= 47:
                if shifted < 32:
                    shifted = 47 - (31 - shifted)
                decrypted += chr(shifted)
            # range 58-64
            elif 58 <= ascii_val <= 64:
                if shifted < 58:
                    shifted = 64 - (57 - shifted)
                decrypted += chr(shifted)
            # range 91-96
            elif 91 <= ascii_val <= 96:
                if shifted < 91:
                    shifted = 96 - (90 - shifted)
                decrypted += chr(shifted)
            # range 123-126
            elif 123 <= ascii_val <= 126:
                if shifted < 123:
                    shifted = 126 - (122 - shifted)
                decrypted += chr(shifted)
            else:
                # fallback: printable ASCII inverse wrap (32-126)
                if shifted < 32:
                    shifted = 126 - (31 - shifted)
                decrypted += chr(shifted)
    return decrypted
