import sys

if __name__ == "__main__":
    morse_dict = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7':  '--...', '8':  '---..', '9':  '----.',
        '0': '-----'
        }
    ret = ""
    if (len(sys.argv) > 1):
        stri = ' '.join(sys.argv[1::])
        if not all(chr.isalnum() or chr.isspace() for chr in stri):
            print("ERROR")
            exit()
        for j in range(len(stri)):
            if (stri[j] == ' '):
                ret += '/'
            else:
                ret += morse_dict[(stri[j].upper())]
            if (j != len(stri) - 1):
                ret += " "
        print(ret)
