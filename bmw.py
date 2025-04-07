print("=== BMW SÖZLÜĞÜNE HOŞ GELDİN GARDİYAN! ===\n")

bmw_sozlugu = {
    "E30": "BMW'nin eski ama karizma kasası, jant koy jilet gibi dursun.",
    "E36": "Gençliğin hayali, driftin adıdır.",
    "E46": "Yarı klasik, yarı modern. Sahip olan kraldır.",
    "E60": "Arka stoplar ay gibi parlar, 5.20 hastası çoktur.",
    "F30": "Yeni nesil dizel canavar. Karaduman bırakır, ortalığı kaplar.",
    "KARADUMAN": "Dizel egzozundan çıkan yoğun siyah duman. Artistlikte seviye atlatır.",
    "M3": "BMW’nin drift makinesi, piste çıkınca rakip tanımaz.",
    "ŞASEDEN YÜRÜYEN": "Ağır modifiye yapılmış, orijinaline elveda demiş araba.",
    "ÇAT PAT": "Egzoz patlaması efekti. Gece duyulursa camdan baktırır."
}

print("Bak elimizdeki kelimeler şöyle:\n")
for kelime in bmw_sozlugu.keys():
    print(f"- {kelime}")

print("\nAnlamadığın bir kelime varsa yaz, açıklayalım gardaş 😎")
word = input("KELİME: ").upper()

if word in bmw_sozlugu:
    print(f"\n✅ {word} demek: {bmw_sozlugu[word]}")
else:
    print("\n❌ Bu kelime BMW camiasında henüz tanımlanmamış. Ama belki sen eklersin, kim bilir 😄")
