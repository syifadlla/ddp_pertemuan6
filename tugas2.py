#Buat lah output dari menggunakan bahasa pemprograman python dengan : 

jumlah = 0
string = ''
for i in range (1, 20, 2):
    jumlah += i
    string += f'{i}'
    if i == 19 :
        string += '='
    else :
        string+= '+'
print(f'{string} {jumlah}')