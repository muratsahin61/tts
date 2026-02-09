#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text-to-Speech (TTS) Modülü
Bu modül hem online (gTTS) hem offline (pyttsx3) TTS motorlarını destekler.
"""

import os
import sys
from typing import Optional


class TextToSpeech:
    """
    Text-to-Speech sınıfı

    Hem online (gTTS) hem offline (pyttsx3) TTS motorlarını destekler.
    Türkçe ve diğer dillerde metin okuma ve ses dosyası oluşturma özellikleri sağlar.
    """

    def __init__(self, engine: str = 'gtts', language: str = 'tr'):
        """
        TTS nesnesini başlatır

        Args:
            engine (str): Kullanılacak motor ('gtts' veya 'pyttsx3')
            language (str): Dil kodu (örn: 'tr' için Türkçe, 'en' için İngilizce)

        Raises:
            ValueError: Geçersiz motor seçimi
            ImportError: Gerekli kütüphane yüklü değilse
        """
        self.engine = engine.lower()
        self.language = language

        if self.engine not in ['gtts', 'pyttsx3']:
            raise ValueError(f"Geçersiz motor: {engine}. 'gtts' veya 'pyttsx3' kullanın.")

        # Motor başlatma
        if self.engine == 'gtts':
            try:
                from gtts import gTTS
                self.gTTS = gTTS
            except ImportError:
                raise ImportError(
                    "gTTS kütüphanesi yüklü değil. "
                    "Yüklemek için: pip install gTTS"
                )

        elif self.engine == 'pyttsx3':
            try:
                import pyttsx3
                self.tts_engine = pyttsx3.init()
                # Türkçe için hız ayarı
                self.tts_engine.setProperty('rate', 150)

                # Dil ayarı (mümkünse)
                try:
                    voices = self.tts_engine.getProperty('voices')
                    # Türkçe ses aramaya çalış
                    for voice in voices:
                        if language in voice.id.lower() or language in voice.name.lower():
                            self.tts_engine.setProperty('voice', voice.id)
                            break
                except Exception:
                    # Ses ayarı başarısız olursa devam et
                    pass
            except ImportError:
                raise ImportError(
                    "pyttsx3 kütüphanesi yüklü değil. "
                    "Yüklemek için: pip install pyttsx3"
                )

    def set_speed(self, rate: int = 150):
        """
        Ses hızını ayarlar (sadece pyttsx3 için)

        Args:
            rate (int): Konuşma hızı (varsayılan: 150 kelime/dakika)
        """
        if self.engine == 'pyttsx3':
            self.tts_engine.setProperty('rate', rate)
        else:
            print("Uyarı: Ses hızı ayarı sadece pyttsx3 motoru için geçerlidir.")

    def speak(self, text: str):
        """
        Metni sesli olarak okur

        Args:
            text (str): Okunacak metin

        Raises:
            Exception: Ses çalma hatası
        """
        if not text or not text.strip():
            print("Hata: Boş metin okunamaz.")
            return

        try:
            if self.engine == 'gtts':
                # gTTS ile sesli okuma
                import tempfile
                from playsound import playsound

                # Geçici dosya oluştur
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                    temp_file = fp.name

                # Ses dosyasını oluştur
                tts = self.gTTS(text=text, lang=self.language, slow=False)
                tts.save(temp_file)

                # Sesi çal
                print(f"Okunuyor: {text[:50]}..." if len(text) > 50 else f"Okunuyor: {text}")
                playsound(temp_file)

                # Geçici dosyayı sil
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

            elif self.engine == 'pyttsx3':
                # pyttsx3 ile sesli okuma
                print(f"Okunuyor: {text[:50]}..." if len(text) > 50 else f"Okunuyor: {text}")
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()

        except ImportError as e:
            print(f"Hata: Gerekli kütüphane yüklü değil - {e}")
            print("playsound kütüphanesini yükleyin: pip install playsound")
        except Exception as e:
            print(f"Ses çalma hatası: {e}")
            print("İpucu: Sisteminizde ses çalma desteği olmayabilir.")

    def save_to_file(self, text: str, filename: str):
        """
        Metni ses dosyası olarak kaydeder

        Args:
            text (str): Kaydedilecek metin
            filename (str): Çıkış dosya adı (örn: 'output.mp3')

        Returns:
            bool: Başarılı ise True, değilse False
        """
        if not text or not text.strip():
            print("Hata: Boş metin kaydedilemez.")
            return False

        try:
            if self.engine == 'gtts':
                # gTTS ile kaydetme
                if not filename.endswith('.mp3'):
                    filename += '.mp3'

                tts = self.gTTS(text=text, lang=self.language, slow=False)
                tts.save(filename)
                print(f"✓ Ses dosyası kaydedildi: {filename}")
                return True

            elif self.engine == 'pyttsx3':
                # pyttsx3 ile kaydetme
                if not filename.endswith('.mp3'):
                    # pyttsx3 genellikle wav formatını destekler
                    if not filename.endswith('.wav'):
                        filename += '.wav'

                self.tts_engine.save_to_file(text, filename)
                self.tts_engine.runAndWait()
                print(f"✓ Ses dosyası kaydedildi: {filename}")
                return True

        except Exception as e:
            print(f"Dosya kaydetme hatası: {e}")
            return False


def main():
    """
    Komut satırından kullanım için ana fonksiyon
    """
    import argparse

    parser = argparse.ArgumentParser(
        description='Text-to-Speech (Metin Okuma) Programı',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler:
  %(prog)s -t "Merhaba Dünya"
  %(prog)s -t "Merhaba Dünya" -o output.mp3
  %(prog)s -t "Hello World" -e pyttsx3 -l en
        """
    )

    parser.add_argument('-t', '--text', type=str, required=True,
                        help='Okunacak metin')
    parser.add_argument('-e', '--engine', type=str, default='gtts',
                        choices=['gtts', 'pyttsx3'],
                        help='TTS motoru (varsayılan: gtts)')
    parser.add_argument('-l', '--language', type=str, default='tr',
                        help='Dil kodu (varsayılan: tr)')
    parser.add_argument('-o', '--output', type=str,
                        help='Çıkış dosya adı (opsiyonel)')
    parser.add_argument('-s', '--speed', type=int, default=150,
                        help='Konuşma hızı (sadece pyttsx3, varsayılan: 150)')

    args = parser.parse_args()

    try:
        # TTS nesnesi oluştur
        tts = TextToSpeech(engine=args.engine, language=args.language)

        # Hız ayarla (pyttsx3 için)
        if args.engine == 'pyttsx3':
            tts.set_speed(args.speed)

        # Dosyaya kaydet veya sesli oku
        if args.output:
            tts.save_to_file(args.text, args.output)
        else:
            tts.speak(args.text)

    except Exception as e:
        print(f"Hata: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
