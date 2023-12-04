KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 1:
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0
    
    
    def _luo_lista(self, koko):
        return [0] * koko
    
    def kuuluu(self, n):
        for i in self.lukujono:
            if n == i:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        if self.alkioiden_lkm >= len(self.lukujono):
            self.jatka_listaa()
        
        self.lukujono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def jatka_listaa(self):
        uusi_lista = self._luo_lista(len(self.lukujono) + self.kasvatuskoko)
        self.kopioi_lista(self.lukujono, uusi_lista)
        self.lukujono = uusi_lista

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            self.lukujono.append(0)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdistetaulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdistetaulu.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdistetaulu.lisaa(b_taulu[i])

        return yhdistetaulu

    @staticmethod
    def leikkaus(a, b):
        leikkaustaulu = IntJoukko()
        a_taulu = a.to_int_list()

        for i in a_taulu:
            if b.kuuluu(i):
                leikkaustaulu.lisaa(i)

        return leikkaustaulu

    @staticmethod
    def erotus(a, b):
        erotustaulu = IntJoukko()
        a_taulu = a.to_int_list()

        for i in a_taulu:
            if not b.kuuluu(i):
                erotustaulu.lisaa(i)

        return erotustaulu

    def __str__(self):
        return f"{{{', '.join([str(i) for i in self.to_int_list()])}}}"