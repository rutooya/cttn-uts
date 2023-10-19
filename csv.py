import csv

# print('Data mahasiswa berdasarkan angkatan dan jenis kelamin')
# with open('mahasiswa.csv','r') as datafile:
#     list_data = datafile.readlines()
#     for i in range(1, len(list_data)):
#         data = list_data[i].strip()
#         split_data = data.split(',')
#         print('Angkatan', split_data[0])
#         print('Pria:', split_data[1])
#         print('Wanita:', split_data[2])
#         print()

print('Data mahasiswa berdasarkan angkatan dan jenis kelamin')
with open('mahasiswa.csv','r', newline=''):
    reader = csv.DictReader(datafile)
    print(reader)
    for row in reader:
        print('Angkatan ', row['tahun'])
        print('Pria: ', row['pria'])
        print('Wanita: ', row['wanita'])