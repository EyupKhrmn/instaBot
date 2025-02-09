from pynput import mouse, keyboard
import time
import threading
import random

def get_positions():
    positions = []
    texts = []
    
    while True:
        print("\n1. Yeni konum ekle")
        print("2. İşlemi başlat")
        secim = input("Seçiminiz (1 veya 2): ")
        
        if secim == "1":
            print("\nFare pozisyonunu belirlemek için 5 saniyeniz var.")
            print("İstediğiniz konuma fareyi götürün ve bekleyin...")
            time.sleep(5)
            
            mouse_controller = mouse.Controller()
            x, y = mouse_controller.position
            positions.append((x, y))
            
            text = input("Bu konuma yazılacak metni girin (Sadece tıklama için boş bırakın): ")
            texts.append(text)
            
            print(f"Konum {len(positions)} eklendi: X={x}, Y={y}")
        
        elif secim == "2":
            if len(positions) > 0:
                return positions, texts
            else:
                print("En az bir konum eklemelisiniz!")
        else:
            print("Geçersiz seçim!")

def get_random_interval_range():
    while True:
        try:
            print("\nRastgele bekleme aralığını belirleyin:")
            min_interval = float(input("Minimum süre (saniye): "))
            max_interval = float(input("Maksimum süre (saniye): "))
            
            if min_interval <= 0 or max_interval <= 0:
                print("Süreler 0'dan büyük olmalı!")
                continue
                
            if min_interval >= max_interval:
                print("Maksimum süre minimum süreden büyük olmalı!")
                continue
                
            return min_interval, max_interval
            
        except ValueError:
            print("Lütfen geçerli sayılar girin!")

def otomatikIslem(positions, texts, durdurmaTus, min_interval, max_interval):
    mouse_controller = mouse.Controller()
    keyboard_controller = keyboard.Controller()
    running = True
    
    def on_press(key):
        nonlocal running
        try:
            if key.char == durdurmaTus:
                running = False
                print("\nProgram durduruldu!")
                return False
        except AttributeError:
            pass
            
    print(f"\nProgram başlatıldı! Durdurmak için '{durdurmaTus}' tuşuna basın.")
    print(f"Bekleme aralığı: {min_interval} - {max_interval} saniye")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    while running:
        for (x, y), text in zip(positions, texts):
            if not running:
                break
                
            mouse_controller.position = (x, y)
            time.sleep(0.1)  # Konum değişimi için kısa bekleme
            mouse_controller.click(mouse.Button.left)
            
            if text:  # Eğer metin varsa yaz
                time.sleep(0.1)  # Tıklama sonrası kısa bekleme
                keyboard_controller.type(text)
            
            # Rastgele bekleme süresi
            random_wait = random.uniform(min_interval, max_interval)
            time.sleep(random_wait)

def main():
    durdurmaTus = 'q'
    positions, texts = get_positions()
    min_interval, max_interval = get_random_interval_range()
    
    thread = threading.Thread(
        target=otomatikIslem, 
        args=(positions, texts, durdurmaTus, min_interval, max_interval)
    )
    thread.start()
    1
if __name__ == "__main__":
    main()
