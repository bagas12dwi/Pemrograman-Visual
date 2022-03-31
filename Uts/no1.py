def hurufPertama(string):
    print('Menampilkan huruf pertama dari string:')
    print(string.split()[0][0])
    for word in string.split():
        print('%s' % word[0], end = ' ')
    print()

def hurufTerakhir(string):
    print('Menampilkan huruf terakhir dari string:')
    for word in string.split():
        print('%s' % word[-1], end = ' ')
    print()
    

def pilihan(string, choice):
    print('Menampilkan huruf ke %s dari string:' % choice)
    for word in string.split():
        print('%s' % word[choice], end = ' ')
    print()

string = input('Masukkan Kata : ')
hurufPertama(string)
hurufTerakhir(string)
pilihan(string, 2)