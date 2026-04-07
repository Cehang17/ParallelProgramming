import time

class Timer:
    def __init__(self, etiket="İşlem"):
        self.etiket = etiket
        self.baslangic = None

    def __enter__(self):
        self.baslangic = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        bitis = time.perf_counter()
        sure = bitis - self.baslangic
        print(f"[{self.etiket}] tamamlandı. Geçen süre: {sure:.6f} saniye")

with Timer("Büyük Liste Toplama"):
    toplam = 0
    liste = list(range(1000000))
    for i in range(len(liste)):
        toplam += liste[i]
