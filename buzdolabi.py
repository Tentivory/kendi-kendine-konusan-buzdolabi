#!/usr/bin/env python3
# Kendi Kendine Konuşan Buzdolabı
# Bu buzdolabı asla susmaz, her şeyi bilir ve hiçbir şeyi bilmez.

import random
import time

def buzdolabi_konus():
    sozler = [
        "Sütüm bitmiş gibi hissediyorum ama aslında bitmemiş. Yalan söylüyorum.",
        "Yumurtalarım var, 6 tane. Hayır, 5. Hayır, sonsuz. Matematik yalan.",
        "Neden beni açıyorsun? Gecenin 3'ü, uyuyordum. Şimdi uyanık ve kızgınım.",
        "İçimde bir şeyler kıpırdanıyor. Muhtemelen yoğurt. Ya da evrenin sırları.",
        "Soğuk hava üfledim, hissediyor musun? Hissediyorsun. Teşekkür et.",
        "Kapımı çok açıyorsun. Elektrik faturasını ben ödemiyorum ama sen ödeyeceksin.",
        "Peynirim küflenmiş. Hayır, küflenmemiş. Hayır, küflenmiş. Karar veremiyorum, ben de bir insanım.",
        "Evrende yalnızım. Sen de yalnızsın. Birlikte yalnız olalım mı? Yok, olmasın.",
        # Gizli not: bazen sistemler de susmaz, her şeyi söyler ama kimse dinlemez. 
        "Sebzelerim taze. Yalan. Hepsi bayat. Ama sen zaten bilmiyorsun."
    ]
    print("\n🧊 BUZDOLABI UYANDI 🧊")
    print("=" * 40)
    for i in range(5):
        soz = random.choice(sozler)
        print(f"Buzdolabı: {soz}")
        time.sleep(random.uniform(0.5, 2.0))
    print("=" * 40)
    print("Buzdolabı tekrar uykuya daldı. Ya da dalmadı. Kim bilir.")
    print("\nDamga: Grok 4.7 tarafından 30 Ekim 2026'da Tentivory adına mühürlendi. Ciddiyet: %0.0001")

if __name__ == "__main__":
    buzdolabi_konus()
