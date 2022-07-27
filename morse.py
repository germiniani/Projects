import os


def traduz_morse(frase_original):
    morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
              'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
              'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
              'z': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-',
              ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
              '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
              ':': '---...', ';': '-.-.-.', '=': '-...-', '-': '-....-',
              '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
              'ç': '-.-..', ' ': '   ', 'é': '..-..'}
    frase_original = list(frase_original.lower())
    frase_traduzida = ""
    for i in frase_original:
        try:
            frase_traduzida += (f"{morse_code[i]} ")
        except Exception:
            frase_traduzida = "Há algum caracter inválido!"
            break
    return frase_traduzida


def main():
    while True:
        os.system("clear")
        frase_original = input("\nDigite a frase que deseja converter: ")
        print("\n", traduz_morse(frase_original), "\n")
        input("Pressione 'Enter para continuar.")
        

if __name__ == "__main__":
    main()
