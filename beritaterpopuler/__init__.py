from bs4 import BeautifulSoup
import requests
"""
method = fungsi
Field / Atribute = variable
"""

class beritaterpopuler:
    def __init__(self, url):
        self.description = "To get the newestearthquake in Indonesia from bmkg.go.id"
        self.result = None
        self.url = url
    def ekstrasi_data(self):
        """
        10 Berita terpopuler Berdasarkan Kompas.com
        A
        1.Istri Pamer Harta, Ini Alasan LHKPN Pejabat Kemensetneg Esha Rahmansah Tak Bisa Ditelusuri
        Dibaca 22.974 kali
        B
        2.Isak Tangis Iringi Jenazah Syabda Perkasa Belawa dan Ibunya Saat Tiba di Rumah Duka
        Dibaca 15.648 kali
        C
        3.Viral, Foto Istrinya Pamer Tas Mewah Hermes dan Gucci, Sekda Riau: Itu KW, Belinya di Mangga Dua
        Dibaca 15.375 kali
        D
        4.Kronologi Syabda Perkasa Belawa Meninggal Kecelakaan, Pahlawan Piala Thomas Berpulang...
        Dibaca 14.137 kali
        E
        5.Kabar Duka, Tunggal Putra Indonesia Syabda Perkasa Belawa Meninggal Dunia
        Dibaca 13.526 kali
        F
        6.Luhut ke IMF: Kalian Jangan Macam-macam...
        Dibaca 13.431 kali
        G
        7.Saat "Netizen" Bantu KPK Bongkar Pejabat yang Pamer Harta...
        Dibaca 8.932 kali
        H
        8.Sempat Terbengkalai di Bandara YIA, 38 Calon Jemaah Umrah Asal Rembang Pulang,
        Seorang Perantara Dilaporkan sebagai Penipu
        Dibaca 8.370 kali
        I
        9.Kala Megawati Semprot Ribuan Kades yang Minta Anggaran Jumbo...
        Dibaca 7.712 kali
        J
        10.Kapolda Jateng Resmi Pecat 5 Polisi yang Jadi Calo Penerimaan Bintara Polri 2022
        Dibaca 7.358 kali
        :return:
        """
        try:
            content = requests.get(self.url)
        except Exception:
            return None
        if content.status_code == 200:
            soup = BeautifulSoup(content.text, "html.parser")

            result = soup.find("div", {"class":"most__list  clearfix"})
            result = soup.findChildren("h4")

            i = 0
            A = None
            B = None
            C = None
            D = None
            E = None
            F = None
            G = None
            H = None
            I = None
            J = None
            for res in result:
                if i == 1:
                    A = res.text
                elif i == 2:
                    B = res.text
                elif i == 3:
                    C = res.text
                elif i == 4:
                    D = res.text
                elif i == 5:
                    E = res.text
                elif i == 6:
                    F = res.text
                elif i == 7:
                    G = res.text
                elif i == 8:
                    H = res.text
                elif i == 9:
                    I = res.text
                elif i == 10:
                    J = res.text
                i = i + 1



            hasil = dict()
            hasil["A"] =  A
            hasil["B"] =  B
            hasil["C"] =  C
            hasil["D"] =  D
            hasil["E"] =  E
            hasil["F"] =  F
            hasil["G"] =  G
            hasil["H"] =  H
            hasil["I"] =  I
            hasil["J"] =  J
            self.result = hasil
        else:
            return None


    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data Berita Terpopuler dari situs Kompas.com")
            return
        print("\n10 Berita Terpopuler berdasarkan situs berita Kompas.com")
        print(f"1. {self.result['A']}")
        print(f"2. {self.result['B']}")
        print(f"3. {self.result['C']}")
        print(f"4. {self.result['D']}")
        print(f"5. {self.result['E']}")
        print(f"6. {self.result['F']}")
        print(f"7. {self.result['G']}")
        print(f"8. {self.result['H']}")
        print(f"9. {self.result['I']}")
        print(f"10. {self.result['J']}")

    def run (self):
        self.ekstrasi_data()
        self.tampilkan_data()


if __name__ == '__main__':
    berita_di_Kompas = beritaterpopuler("https://www.kompas.com/")
    print("deskripsi class", berita_di_Kompas.description)
    berita_di_Kompas.run()

    berita_di_Indonesia = beritaterpopuler("https://www.kompas.com/")
    print("deskripsi class", berita_di_Indonesia.description)
    berita_di_Indonesia.run()
    # berita_di_Kompas.ekstrasi_data()
    # berita_di_Kompas.tampilkan_data()
