import numpy as np


def create_matrix(arr, n):  # fungsi untuk membuat matriks
    matrix = np.zeros([n + 1, n + 1], dtype=int)  # n+1 karena input realasi mulai dari angka 1 sedangkan index dalam matriks dimulai dari 0
    for i in arr:
        matrix[i] = 1
    return matrix


def is_reflective(matrix, n):
    for i in range(1, n + 1):
        condition, index = '', ''  # nilai kondisi dan contoh penyangkal
        if matrix[(i, i)] == 1:  # cek jika nilai matriks diagonalnya semua 1, maka relasi bersifat refleksif
            condition, index = True, None  # contoh penyangkal 'None' karena kondisi True yang berarti relasi reflektif
        else:
            condition, index = False, i  # jika nilai matriks diagonalnya ada yang tidak sama dengan 1, maka relasi tidak bersifat refleksif
            return condition, index
    return condition, index


def is_symmetric(matrix, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            condition, row, column = '', '', ''  # nilai kondisi dan contoh penyangkal
            if matrix[(i, j)] == matrix[(j, i)]:  # cek jika matriks (a, b) sama dengan (b, c), maka relasi bersifat simetris
                condition, row, column = True, None, None
            elif matrix[(i, j)] != matrix[(j, i)] and matrix[(i,j)] == 0:  # jika matriks (a, b) tidak sama dengan (b, c), maka i and j akan di ambil untuk contoh penyangkal. matrix[(i, j)] == 0 digunakan agar posisi a dan b tidak terbalik
                condition, row, column = False, i, j
                return condition, row, column
    return condition, row, column


def is_transitive(matrix):
    condition = ''
    a, b, c = int(), int(), int()  # variabel a,b,c untuk contoh penyangkal
    matrix_squared = matrix @ matrix  # sifat transitif merupakan perbandingan matrix awal dan hasil perkalian matrix dengan dirinya sendiri, apabila pada suatu posisi matrix awal bernilai 0, namun pada posisi yang sama hasil matrix perkalian bernilai bukan 0, maka dapat disimpulkan R tidak bersifat transitif /// referensi: https://math.stackexchange.com/questions/228898/how-to-check-whether-a-relation-is-transitive-from-the-matrix-representation
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix[(i, j)] == 0 and matrix_squared[(i,j)] != 0:  # tempat mengecek jika nilai matrix awal 0 dan matrix_squared tidak bernilai 0 maka R tidak transitif
                condition = False
                a = i  # contoh penyangkal a
                c = j  # contoh penyangkal c
            elif matrix[(a, j)] and matrix[(i, c)] == 1:  # mencari contoh penyangkal b
                b = j
                return condition, a, b, c
            else:
                condition = True
    return condition, None, None, None


def partition():  # fungsi untuk mencari kelas ekivalen
    list = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if matrix[i][j] == 1:  # jika suatu barisan bernilai 1, index kolomnya akan diambil lalu diappend ke list yang bernama row
                row.append(j)
            list.append(row)  # setelah mengumpulkan index yang bernilai 1, list row ditambah ke list sehingga berbebentuk 2d list yang menmunjukkan anggota kelas ekivalen

    partition = []
    for i in range(len(list)):
        if list[i] not in partition:  # terdapat problem setelah mengappend index, jika terdapat 2 index misal 1 dan 4, maka saat loop index ke 4, akan menghasilkan index yang yang sama sehingga terdapat kelas ekivalen yang sama persis contoh (1,4),(2),(3),(1,4), sehingga problem ini diselesaikan dengan cara membuat list baru dan mengappend ulang jika data sudah ada list tidak akan di append
            partition.append(list[i])
    return partition, len(partition)


if __name__ == '__main__':
    # INPUT RELATIONS
    n, r = map(int, input().split())
    arr = []
    for i in range(r):
        relations = map(int, input().split())
        relations = tuple(relations)
        arr.append(relations)

    # CREATE MATRIX
    matrix = create_matrix(arr, n)

    # REFLECTIVE
    reflective_condition, index = is_reflective(matrix, n)
    # SYMMETRIC
    symmetric_condition, row, column = is_symmetric(matrix, n)
    # TRANSITIVE
    transitive_condition, a, b, c = is_transitive(matrix)

    # MAIN PROCESS
    if reflective_condition and symmetric_condition and transitive_condition == True:  # jika 3 kondisi yaitu reflective, simetris dan transitif maka function partition() akan dijalankan
        print(matrix)
        print('Relasi merupakan relasi ekivalen.')
        partition, no_of_class = partition()  # memanggil function untuk mencari kelas ekivalen dan akan mereturn anggota kelas ekivalen dan jumlah kelas ekivalen
        print(f'Banyak kelas ekivalen: {no_of_class}')
        for i in partition:
            print(*i, sep=" ")  # print anggota kelas ekivalen tanpa kurung kotak

    else:
        print('Relasi bukan merupakan relasi ekivalen.')
        if reflective_condition == True:  # jika bersifat refleksif, kondisi ini akan dijalankan
            print(f'Relasi bersifat refleksif.')
        elif reflective_condition == False:  # jika tidak bersifat refleksif, kondisi ini akan dijalankan
            print(f'Relasi tidak bersifat refleksif. \nContoh penyangkal: a = {index}, b = {index}')  # akan menampilkan contoh penyangkal refleksif
        if symmetric_condition == True:  # jika bersifat simetris, kondisi ini akan dijalankan
            print(f'Relasi bersifat simetris.')
        elif symmetric_condition == False:  # jika tidak bersifat simetris, kondisi ini akan dijalankan
            print(f'Relasi tidak bersifat simetris. \nContoh penyangkal: a = {row}, b = {column}.')  # akan menampilkan contoh penyangkal simetris
        if transitive_condition == True:
            print(f'Relasi bersifat transitif.')
        elif transitive_condition == False:  # jika tidak bersifat transitif, kondisi ini akan dijalankan
            print(f'Relasi tidak bersifat transitif. \nContoh penyangkal: a = {a}, b = {b}, c = {c}.')  # akan menampilkan contoh penyangkal transitif

