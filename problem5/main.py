def remove_duplicates(array):
    # count = 0
    Hasil = []
    for i in array :
        H = array.count(i)
        # print (H, end="")
        if H >= 2 :
            if i not in Hasil :
                Hasil.append(i)
                # print (i, end="")
        else : 
            Hasil.append(i)
            # print(i, end="")
    Jumlah = len(Hasil)
    return Jumlah

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4