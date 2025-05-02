# pengecekan bilangan
masukin = int(input("masukan bilangan kurang dari 5 atau lebih dari 10"))
#pengecekan kurang dari 5
kurangdari = masukin < 5
print("kurang dari 5 : ", kurangdari)
#lebih dari 10
lebihdari = masukin > 10
print("lebih dari 10 : ", kurangdari)
final = kurangdari or lebihdari
print(final)