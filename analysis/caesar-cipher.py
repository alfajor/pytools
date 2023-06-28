import string

# encode / decode caesar cipher. input mapping: [a-z] -> [z-a]
def caeser_cipher(message):
    alpha_len = ord('z') - ord('a')
    alpha_all = list(string.ascii_letters)
    decoded_text = ''

    for ch in message:
        if ch in alpha_all:
            decoded_text += alpha_all[-alpha_all.index(ch) + alpha_len]
        else:
            decoded_text += ch

    print(decoded_text)

caeser_cipher("Hey, This is a super secret message!!")