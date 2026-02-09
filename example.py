#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text-to-Speech Kullanım Örnekleri
Bu dosya TTS sisteminin farklı kullanım senaryolarını gösterir.
"""

from tts import TextToSpeech


def example_1_basic_speech():
    """Örnek 1: Basit metin okuma (gTTS ile)"""
    print("\n" + "="*50)
    print("Örnek 1: Basit Metin Okuma (gTTS)")
    print("="*50)

    try:
        tts = TextToSpeech(engine='gtts', language='tr')
        tts.speak("Merhaba! Ben bir metin okuma programıyım.")
    except Exception as e:
        print(f"Hata: {e}")


def example_2_save_to_file():
    """Örnek 2: Ses dosyası olarak kaydetme"""
    print("\n" + "="*50)
    print("Örnek 2: Ses Dosyası Olarak Kaydetme")
    print("="*50)

    try:
        tts = TextToSpeech(engine='gtts', language='tr')
        text = "Bu metin bir MP3 dosyası olarak kaydedilecek."
        tts.save_to_file(text, "output.mp3")
    except Exception as e:
        print(f"Hata: {e}")


def example_3_pyttsx3_offline():
    """Örnek 3: Offline motor (pyttsx3) kullanımı"""
    print("\n" + "="*50)
    print("Örnek 3: Offline Motor (pyttsx3)")
    print("="*50)

    try:
        tts = TextToSpeech(engine='pyttsx3', language='tr')
        tts.speak("Ben internet bağlantısı olmadan çalışıyorum!")
    except Exception as e:
        print(f"Hata: {e}")


def example_4_speed_control():
    """Örnek 4: Ses hızı kontrolü (pyttsx3)"""
    print("\n" + "="*50)
    print("Örnek 4: Ses Hızı Kontrolü")
    print("="*50)

    try:
        tts = TextToSpeech(engine='pyttsx3', language='tr')

        print("\nYavaş konuşma (100 kelime/dakika):")
        tts.set_speed(100)
        tts.speak("Ben yavaş konuşuyorum.")

        print("\nNormal konuşma (150 kelime/dakika):")
        tts.set_speed(150)
        tts.speak("Ben normal hızda konuşuyorum.")

        print("\nHızlı konuşma (200 kelime/dakika):")
        tts.set_speed(200)
        tts.speak("Ben hızlı konuşuyorum.")
    except Exception as e:
        print(f"Hata: {e}")


def example_5_english_speech():
    """Örnek 5: İngilizce metin okuma"""
    print("\n" + "="*50)
    print("Örnek 5: İngilizce Metin Okuma")
    print("="*50)

    try:
        tts = TextToSpeech(engine='gtts', language='en')
        tts.speak("Hello! I am a text to speech program.")
    except Exception as e:
        print(f"Hata: {e}")


def example_6_long_text():
    """Örnek 6: Uzun metin okuma"""
    print("\n" + "="*50)
    print("Örnek 6: Uzun Metin Okuma")
    print("="*50)

    long_text = """
    Türkiye, Asya ve Avrupa kıtaları arasında yer alan bir ülkedir.
    Başkenti Ankara'dır. En kalabalık şehri İstanbul'dur.
    Türkiye'nin nüfusu yaklaşık 85 milyon civarındadır.
    """

    try:
        tts = TextToSpeech(engine='gtts', language='tr')
        tts.save_to_file(long_text.strip(), "long_text.mp3")
    except Exception as e:
        print(f"Hata: {e}")


def example_7_compare_engines():
    """Örnek 7: Motor karşılaştırması"""
    print("\n" + "="*50)
    print("Örnek 7: Motor Karşılaştırması")
    print("="*50)

    text = "Bu metin hem gTTS hem de pyttsx3 ile okunacak."

    try:
        print("\n1. gTTS (Online, Yüksek Kalite):")
        tts_gtts = TextToSpeech(engine='gtts', language='tr')
        tts_gtts.speak(text)

        print("\n2. pyttsx3 (Offline, Hızlı):")
        tts_pyttsx3 = TextToSpeech(engine='pyttsx3', language='tr')
        tts_pyttsx3.speak(text)
    except Exception as e:
        print(f"Hata: {e}")


def interactive_mode():
    """İnteraktif mod - Kullanıcıdan metin al ve oku"""
    print("\n" + "="*50)
    print("İnteraktif Mod")
    print("="*50)
    print("Çıkmak için 'q' yazın")

    try:
        tts = TextToSpeech(engine='gtts', language='tr')

        while True:
            text = input("\nOkunacak metni girin: ").strip()

            if text.lower() == 'q':
                print("Çıkılıyor...")
                break

            if text:
                tts.speak(text)
            else:
                print("Lütfen bir metin girin.")

    except KeyboardInterrupt:
        print("\n\nProgram kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"Hata: {e}")


def main():
    """Ana fonksiyon - Tüm örnekleri çalıştır"""
    print("\n" + "="*60)
    print("TEXT-TO-SPEECH KULLANIM ÖRNEKLERİ")
    print("="*60)

    # Tüm örnek fonksiyonlarının listesi
    examples = [
        ('1', example_1_basic_speech, "Basit metin okuma (gTTS)"),
        ('2', example_2_save_to_file, "Ses dosyası olarak kaydetme"),
        ('3', example_3_pyttsx3_offline, "Offline motor (pyttsx3)"),
        ('4', example_4_speed_control, "Ses hızı kontrolü"),
        ('5', example_5_english_speech, "İngilizce metin okuma"),
        ('6', example_6_long_text, "Uzun metin okuma ve kaydetme"),
        ('7', example_7_compare_engines, "Motor karşılaştırması"),
        ('8', interactive_mode, "İnteraktif mod"),
    ]

    print("\nHangi örneği çalıştırmak istersiniz?")
    for num, _, description in examples:
        print(f"{num}. {description}")
    print("9. Tüm örnekleri çalıştır")
    print("0. Çıkış")

    try:
        choice = input("\nSeçiminiz (0-9): ").strip()

        if choice == '9':
            # Tüm örnekleri çalıştır (interaktif mod hariç)
            for num, func, _ in examples:
                if func != interactive_mode:
                    func()
            print("\n✓ Tüm örnekler tamamlandı!")
        elif choice == '0':
            print("Çıkılıyor...")
        else:
            # Seçilen örneği çalıştır
            example_found = False
            for num, func, _ in examples:
                if choice == num:
                    func()
                    example_found = True
                    break
            if not example_found:
                print("Geçersiz seçim!")

    except KeyboardInterrupt:
        print("\n\nProgram kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"Hata oluştu: {e}")


if __name__ == '__main__':
    main()
