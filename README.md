# 🎙️ Text-to-Speech (Metin Okuma) Sistemi

Türkçe destekli, kullanımı kolay bir Text-to-Speech (Yazıyı Sese Çevirme) sistemi. Hem online hem offline çalışabilir.

## 📝 Açıklama

Bu proje, Python kullanarak yazılı metinleri sesli okumak için geliştirilmiş bir sistemdir. İki farklı TTS motoru destekler:
- **gTTS (Google Text-to-Speech)** - Online, yüksek kaliteli ses
- **pyttsx3** - Offline, hızlı ve internet bağlantısı gerektirmeyen

## 🚀 Hızlı Başlangıç

```python
from tts import TextToSpeech

# Basit kullanım
tts = TextToSpeech(engine='gtts', language='tr')
tts.speak("Merhaba Dünya!")

# Dosyaya kaydetme
tts.save_to_file("Bu metin bir ses dosyasına dönüşecek", "output.mp3")
```

## 📦 Kurulum

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/muratsahin61/tts.git
cd tts
```

### 2. Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

### Sistem Gereksinimleri
- Python 3.7 veya üzeri
- İnternet bağlantısı (gTTS için)
- Ses çıkışı olan sistem

## 💻 Kullanım Örnekleri

### Örnek 1: Basit Metin Okuma (gTTS)
```python
from tts import TextToSpeech

tts = TextToSpeech(engine='gtts', language='tr')
tts.speak("Merhaba! Ben bir metin okuma programıyım.")
```

### Örnek 2: Offline Kullanım (pyttsx3)
```python
from tts import TextToSpeech

# İnternet bağlantısı olmadan çalışır
tts = TextToSpeech(engine='pyttsx3', language='tr')
tts.speak("Ben internet olmadan çalışıyorum!")
```

### Örnek 3: Ses Dosyası Oluşturma
```python
from tts import TextToSpeech

tts = TextToSpeech(engine='gtts', language='tr')
tts.save_to_file("Bu metin bir MP3 dosyası olacak", "output.mp3")
```

### Örnek 4: Ses Hızı Kontrolü (pyttsx3)
```python
from tts import TextToSpeech

tts = TextToSpeech(engine='pyttsx3', language='tr')

# Yavaş konuşma
tts.set_speed(100)
tts.speak("Ben yavaş konuşuyorum")

# Hızlı konuşma
tts.set_speed(200)
tts.speak("Ben hızlı konuşuyorum")
```

### Örnek 5: İngilizce Metin Okuma
```python
from tts import TextToSpeech

tts = TextToSpeech(engine='gtts', language='en')
tts.speak("Hello! I am a text to speech program.")
```

### Örnek 6: Komut Satırından Kullanım
```bash
# Metni sesli okuma
python tts.py -t "Merhaba Dünya"

# Dosyaya kaydetme
python tts.py -t "Merhaba Dünya" -o output.mp3

# pyttsx3 motoru ile
python tts.py -t "Merhaba Dünya" -e pyttsx3

# İngilizce metin
python tts.py -t "Hello World" -e gtts -l en

# Özel hız ayarı (pyttsx3)
python tts.py -t "Hızlı konuşma" -e pyttsx3 -s 200
```

### Örnek 7: İnteraktif Örnekler
```bash
python example.py
```

## ⚙️ Özellikler

- ✅ **İki Motor Desteği**: gTTS (online) ve pyttsx3 (offline)
- ✅ **Türkçe Karakterler**: Türkçe özel karakterler tam destek
- ✅ **Çoklu Dil**: Türkçe, İngilizce ve diğer diller
- ✅ **Ses Kontrolü**: Konuşma hızı ayarlama (pyttsx3)
- ✅ **Dosya Kaydetme**: MP3/WAV formatında kaydetme
- ✅ **Canlı Okuma**: Metni anında sesli okuma
- ✅ **Hata Yönetimi**: Kullanıcı dostu hata mesajları
- ✅ **Komut Satırı**: Terminal'den doğrudan kullanım
- ✅ **API Kullanımı**: Python kodunda kütüphane olarak kullanım

## 🔧 Motorlar

### gTTS (Google Text-to-Speech)
**Artıları:**
- ✅ Yüksek ses kalitesi
- ✅ Doğal insan sesi
- ✅ Çok sayıda dil desteği
- ✅ Türkçe karakterler için mükemmel

**Eksileri:**
- ❌ İnternet bağlantısı gerekir
- ❌ Google servisleri gerekli
- ❌ Biraz daha yavaş

**Kullanım:**
```python
tts = TextToSpeech(engine='gtts', language='tr')
```

### pyttsx3
**Artıları:**
- ✅ Offline çalışır (internet gereksiz)
- ✅ Çok hızlı
- ✅ Ses hızı kontrolü
- ✅ Sistem seslerini kullanır

**Eksileri:**
- ❌ Ses kalitesi gTTS'den düşük
- ❌ Robotik ses tonu
- ❌ Dil desteği sisteme bağlı

**Kullanım:**
```python
tts = TextToSpeech(engine='pyttsx3', language='tr')
```

## 🌍 Dil Desteği

### Desteklenen Başlıca Diller (gTTS)
- 🇹🇷 Türkçe (`tr`)
- 🇬🇧 İngilizce (`en`)
- 🇩🇪 Almanca (`de`)
- 🇫🇷 Fransızca (`fr`)
- 🇪🇸 İspanyolca (`es`)
- 🇮🇹 İtalyanca (`it`)
- 🇷🇺 Rusça (`ru`)
- 🇯🇵 Japonca (`ja`)
- 🇨🇳 Çince (`zh-CN`)
- 🇰🇷 Korece (`ko`)
- 🇸🇦 Arapça (`ar`)

### Dil Değiştirme Örneği
```python
# Türkçe
tts_tr = TextToSpeech(engine='gtts', language='tr')
tts_tr.speak("Merhaba")

# İngilizce
tts_en = TextToSpeech(engine='gtts', language='en')
tts_en.speak("Hello")

# Almanca
tts_de = TextToSpeech(engine='gtts', language='de')
tts_de.speak("Guten Tag")
```

## 📚 API Referansı

### TextToSpeech Sınıfı

#### `__init__(engine='gtts', language='tr')`
TTS nesnesini başlatır.

**Parametreler:**
- `engine` (str): Motor seçimi - `'gtts'` veya `'pyttsx3'`
- `language` (str): Dil kodu (örn: `'tr'`, `'en'`)

#### `speak(text)`
Metni sesli okur.

**Parametreler:**
- `text` (str): Okunacak metin

#### `save_to_file(text, filename)`
Metni ses dosyası olarak kaydeder.

**Parametreler:**
- `text` (str): Kaydedilecek metin
- `filename` (str): Çıkış dosya adı

**Dönüş:** `bool` - Başarılı ise `True`

#### `set_speed(rate=150)`
Konuşma hızını ayarlar (sadece pyttsx3 için).

**Parametreler:**
- `rate` (int): Konuşma hızı (kelime/dakika)

## ❓ Sık Sorulan Sorular

### Ses çıkmıyor, ne yapmalıyım?
1. Ses kartınızın çalıştığından emin olun
2. Sistem ses seviyesini kontrol edin
3. `playsound` kütüphanesinin doğru yüklendiğini kontrol edin
4. Linux'ta `python3-pyaudio` ve `ffmpeg` yükleyin:
   ```bash
   sudo apt-get install python3-pyaudio ffmpeg
   ```

### gTTS "İnternet bağlantısı hatası" veriyor?
- İnternet bağlantınızı kontrol edin
- Offline kullanım için `pyttsx3` motorunu kullanın:
  ```python
  tts = TextToSpeech(engine='pyttsx3')
  ```

### Türkçe karakterler düzgün okunmuyor (pyttsx3)?
pyttsx3 sisteminizde yüklü Türkçe ses paketlerine bağlıdır. En iyi Türkçe desteği için gTTS kullanın:
```python
tts = TextToSpeech(engine='gtts', language='tr')
```

### Hangi motoru seçmeliyim?
- **İnternet varsa ve kalite önemliyse** → `gtts`
- **Offline çalışma gerekiyorsa** → `pyttsx3`
- **Hız kontrolü gerekiyorsa** → `pyttsx3`

### Ses dosyaları nereye kaydediliyor?
Varsayılan olarak programın çalıştığı dizine kaydedilir. Tam yol belirtebilirsiniz:
```python
tts.save_to_file("Metin", "/tam/yol/output.mp3")
```

### Diğer dilleri nasıl kullanırım?
`language` parametresini değiştirin:
```python
tts = TextToSpeech(engine='gtts', language='en')  # İngilizce
tts = TextToSpeech(engine='gtts', language='de')  # Almanca
tts = TextToSpeech(engine='gtts', language='fr')  # Fransızca
```

### Birden fazla cümleyi nasıl okutabilirim?
Metinleri birleştirerek veya döngü kullanarak:
```python
sentences = ["İlk cümle.", "İkinci cümle.", "Üçüncü cümle."]
for sentence in sentences:
    tts.speak(sentence)

# veya
full_text = " ".join(sentences)
tts.speak(full_text)
```

### MP3 yerine WAV formatı kullanabilir miyim?
Evet, `pyttsx3` ile:
```python
tts = TextToSpeech(engine='pyttsx3')
tts.save_to_file("Metin", "output.wav")
```

## 🛠️ Sorun Giderme

### ModuleNotFoundError: No module named 'gtts'
```bash
pip install gTTS
```

### ModuleNotFoundError: No module named 'pyttsx3'
```bash
pip install pyttsx3
```

### playsound hatası (Linux)
```bash
sudo apt-get install python3-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-tools
```

### pyttsx3 "No module named '_bsddb'" hatası (Linux)
```bash
pip install pyttsx3==2.90
# veya
sudo apt-get install python3-espeak
```

### macOS'ta ses çıkmıyor
macOS'ta pyttsx3 otomatik olarak çalışmalıdır. gTTS için `playsound` yerine `afplay` kullanabilirsiniz.

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request'lerinizi göndermekten çekinmeyin.

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📧 İletişim

Sorularınız için issue açabilirsiniz.

## 🙏 Teşekkürler

- [gTTS](https://github.com/pndurette/gTTS) - Google Text-to-Speech
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) - Offline TTS motoru
- [playsound](https://github.com/TaylorSMarks/playsound) - Ses çalma kütüphanesi

---

**Not:** Bu proje eğitim ve kişisel kullanım amaçlıdır. Google TTS kullanırken Google'ın kullanım şartlarına uygun hareket edin.
