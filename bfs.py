#awal = A
#tujuan = G
#jalur

peta1 =  {'A':set(['B']),
         'B':set(['A','C']),
         'C':set(['B','D','H','I']),
         'D':set(['C','E','F','H','M']),
         'E':set(['D']),
         'F':set(['D','G','M']),
         'G':set(['F','H']),
         'H':set(['C','D','G','L']),
         'I':set(['C','J','K']),
         'J':set(['I']),
         'K':set(['I','L']),
         'L':set(['H','K']),
	 'M':set(['D','F'])}

print()
print("*********BFS***********")
awal = input("Input Awal: ")
akhir = input("Input Tujuan: ")
print("***********************")
print()

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

print(bfs(peta1,awal,akhir))
print()
print("Link Github: https://github.com/Xalvom/python-bfs-dfs")
