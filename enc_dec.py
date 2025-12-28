
def shift_in_range(ch, shift, start, end):
    n = end - start + 1
    return chr(start + ((ord(ch) - start + shift) % n))

def encrypt(pwd):
    out = ""
    for ch in pwd:
        o = ord(ch)
        if 65 <= o <= 90:        # A-Z
            out += shift_in_range(ch, 7, 65, 90)
        elif 97 <= o <= 122:    # a-z
            out += shift_in_range(ch, 14, 97, 122)
        elif 48 <= o <= 57:     # 0-9
            out += shift_in_range(ch, 3, 48, 57)
        elif 32 <= o <= 47:
            out += shift_in_range(ch, 9, 32, 47)
        elif 58 <= o <= 64:
            out += shift_in_range(ch, 9, 58, 64)
        elif 91 <= o <= 96:
            out += shift_in_range(ch, 9, 91, 96)
        elif 123 <= o <= 126:
            out += shift_in_range(ch, 9, 123, 126)
        elif 0 <= o <= 31:
            out += shift_in_range(ch, 5, 0, 31)
        else:
            out += ch
    return out
#print(encrypt("Computer"))


def decrypt(pwd):
    out = ""
    for ch in pwd:
        o = ord(ch)
        if 65 <= o <= 90:        # A-Z
            out += shift_in_range(ch, -7, 65, 90)
        elif 97 <= o <= 122:    # a-z
            out += shift_in_range(ch, -14, 97, 122)
        elif 48 <= o <= 57:     # 0-9
            out += shift_in_range(ch, -3, 48, 57)
        elif 32 <= o <= 47:
            out += shift_in_range(ch, -9, 32, 47)
        elif 58 <= o <= 64:
            out += shift_in_range(ch, -9, 58, 64)
        elif 91 <= o <= 96:
            out += shift_in_range(ch, -9, 91, 96)
        elif 123 <= o <= 126:
            out += shift_in_range(ch, -9, 123, 126)
        elif 0 <= o <= 31:  # CONTROL CHARACTERS
            out += shift_in_range(ch, -5, 0, 31)
        else:
            out += ch
    return out
