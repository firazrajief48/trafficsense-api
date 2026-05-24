def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def is_intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

class TrafficCounter:
    def __init__(self, garis_virtual):
        self.garis_virtual = garis_virtual
        self.jejak_kendaraan = {}
        self.kendaraan_terhitung = set()
        self.total_count = 0
        self.count_per_kelas = {'Motorcycle': 0, 'Car': 0, 'Bus': 0, 'Truck': 0}

    def update_count(self, tracking_id, titik_tengah_sekarang, nama_kelas):
        if tracking_id in self.jejak_kendaraan:
            titik_tengah_sebelum = self.jejak_kendaraan[tracking_id]

            if is_intersect(self.garis_virtual[0], self.garis_virtual[1],
                            titik_tengah_sebelum, titik_tengah_sekarang):
                if tracking_id not in self.kendaraan_terhitung:
                    self.total_count += 1
                    if nama_kelas in self.count_per_kelas:
                        self.count_per_kelas[nama_kelas] += 1
                    self.kendaraan_terhitung.add(tracking_id)

        self.jejak_kendaraan[tracking_id] = titik_tengah_sekarang