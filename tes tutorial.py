data = [None,None]

data[0] = {'menu' : 'nasi_goreng', 'bahan': "['nasi', 'ayam']", 'year':'2003'}

print(data)

x = 'ayam'
hash = 0
for i in x:
    h = ord(i)
    hash += h

print(hash%100)



