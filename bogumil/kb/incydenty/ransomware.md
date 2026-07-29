# Ransomware — natychmiastowe działanie

_Ransomware to szyfrowanie plików firmy i żądanie okupu. Bogumił pomaga zatrzymać szkody i zaplanować odbudowę._

## Jak rozpoznać

- Pliki mają zmienione rozszerzenie: `.locked`, `.encrypted`, `.WNCRY`, `.ryuk`, lub ciąg losowych liter
- Na pulpicie pojawił się plik `README.txt`, `DECRYPT_FILES.html` lub podobny z żądaniem okupu
- Programy przestały się otwierać — „plik jest uszkodzony" lub błędy przy otwieraniu dokumentów
- Komputer wyraźnie pracuje — dużo aktywności dysku, wentylator głośny — szyfrowanie trwa
- Inne komputery w sieci też mają problemy

---

## PIERWSZE KROKI — natychmiast, kolejność jest krytyczna

### 1. Odetnij od sieci — TERAZ
- **Wyciągnij kabel sieciowy** z komputera lub wyłącz WiFi (przycisk na klawiaturze lub w ustawieniach)
- Jeśli to serwer — wyciągnij kabel sieci, nie gasząc maszyny
- **Cel:** zatrzymać szyfrowanie innych urządzeń w sieci i odciąć komunikację ransomware z serwerami atakujących

### 2. NIE wyłączaj komputera
- Wyłączenie może zniszczyć dowody w pamięci RAM
- Niektóre ransomware mają pułapkę na wyłączenie — szyfrują dysk przy zamknięciu systemu
- Zostaw komputer włączony, odcięty od sieci

### 3. NIE płać okupu — jeszcze
- Płatność nie gwarantuje odzyskania plików (ok. 40% ofiar nie dostaje klucza mimo zapłaty)
- Zapłata finansuje kolejne ataki i może być nielegalna przy sankcjach (np. atakujący z Rosji/Korei Płn.)
- Najpierw sprawdź opcje odzyskania danych

### 4. Napisz do Bogumił
Bogumił przejmie koordynację: oceni szkody, sprawdzi opcje backupu, pomoże z krokami prawnymi.

---

## Pytania diagnostyczne Bogumił zadaje

1. Które komputery są dotknięte? Jeden czy wiele?
2. Czy macie kopię zapasową i kiedy była ostatnia?
3. Jakie rozszerzenie mają zaszyfrowane pliki? (pomaga zidentyfikować rodzaj ransomware)
4. Czy pojawił się plik z żądaniem okupu? Jaką kryptowalutę i ile żądają?
5. Kiedy zauważyłeś problem? (pomaga ocenić zakres szyfrowania)
6. Czy inne urządzenia w sieci też są dotknięte?

---

## Ścieżka odzyskiwania

### Opcja 1 — backup istnieje i jest czysty (najlepsza)
1. Potwierdź że backup pochodzi sprzed ataku (sprawdź datę)
2. Upewnij się że backup NIE jest podłączony do zainfekowanej sieci
3. Wyczyść (reinstaluj Windows) zainfekowane maszyny zanim przywrócisz dane
4. Przywróć z backupu
5. Zmień wszystkie hasła — zakładamy że atakujący miał dostęp do danych logowania

### Opcja 2 — brak backupu, znany ransomware
Sprawdź serwis **No More Ransom** (https://www.nomoreransom.org/pl/) — europejski projekt z darmowymi dekryptorami dla setek rodzajów ransomware. Wgraj próbkę zaszyfrowanego pliku i żądanie okupu — jeśli jest dekryptor, pobierz i użyj.

### Opcja 3 — brak backupu, brak dekryptora
Opcje:
- Przechowaj zaszyfrowane pliki — dekryptor może pojawić się później (serwisy forensiczne często łamią klucze po kilku miesiącach)
- Skontaktuj się z profesjonalną firmą forensiczną (Bogumił poleci sprawdzone firmy w Polsce)
- Zapłata okupu — ostateczność, po konsultacji z prawnikiem

---

## RODO — obowiązek zgłoszenia do UODO

Ransomware niemal zawsze oznacza naruszenie danych osobowych (atakujący miał dostęp do danych przed zaszyfrowaniem).

**Art. 33 RODO: 72 godziny na zgłoszenie do UODO** od momentu stwierdzenia naruszenia.

Bogumił pomaga:
- Ocenić zakres naruszenia (jakie dane były na zainfekowanych maszynach)
- Przygotować projekt zgłoszenia do UODO
- Ocenić czy trzeba też powiadamiać osoby fizyczne (Art. 34)

Formularz UODO: https://uodo.gov.pl/pl/83/191

---

## Po incydencie — co zrobić żeby się nie powtórzyło

- **Backup 3-2-1**: 3 kopie, 2 różne nośniki, 1 poza siedzibą (np. chmura)
- Backup **odłączony od sieci** gdy nie jest aktywnie używany (atakujący szyfrują też podłączone dyski zewnętrzne)
- **Aktualizacje Windows** na wszystkich maszynach — ransomware często używa znanych luk
- **Segmentacja sieci** — serwer plików w osobnym segmencie sieci, nie dostępny bezpośrednio z każdego komputera
- **Ograniczone uprawnienia** — pracownicy nie powinni mieć praw admina na co dzień
- **Szkolenie z phishingu** — większość ransomware trafia przez mail

---

## Zgłaszanie i pomoc

- **CERT Polska** — https://incydent.cert.pl (warto zgłosić, pomagają i zbierają statystyki)
- **Policja — cyberprzestępczość** — https://www.gov.pl/web/bsk/cyberprzestepczosc (jeśli szkody > kilka tysięcy PLN)
- **No More Ransom** — https://www.nomoreransom.org/pl/ (darmowe dekryptory)
- **UODO** — zgłoszenie naruszenia: https://uodo.gov.pl/pl/83/191
