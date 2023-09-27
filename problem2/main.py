Abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 
         'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

def caesar(offset, input_str):
    print("\'", end="")
    str = ''
    for a in range (len(input_str)) :
        Hasil_akhir = Abjad.index(input_str[a]) + offset
        str += Abjad [ Hasil_akhir % 26]
    for Hasil in str :
        print(Hasil, end='')
    print("\'", end="")
    return str

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl