a = int(input("Masukkan Angka pertama : "))
b = int(input("Masukkan Angka kedua : "))

hasilAnd = a & b
hasilOr = a | b
hasilXor = a ^ b

print("Hasil dari operasi bitwise AND antara a: " + str(a) + ", b: " + str(b) + " -> (a and b) = " + str(hasilAnd))
print("Hasil dari operasi bitwise OR antara a: " + str(a) + ", b: " + str(b) + " -> (a or b) = " + str(hasilOr))
print("Hasil dari operasi bitwise XOR antara a: " + str(a) + ", b: " + str(b) + " -> (a xor b) = " + str(hasilXor))