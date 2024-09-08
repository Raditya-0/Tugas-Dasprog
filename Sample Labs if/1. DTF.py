# Input dan validasi waktu acara streaming (GMT+2)
while True:
    stream_time_gmt2 = input("Masukkan waktu acara streaming (GMT+2) dalam format HH:MM:SS: ").strip()
    if len(stream_time_gmt2) == 8 and stream_time_gmt2[2] == ':' and stream_time_gmt2[5] == ':':
        try:
            stream_hour, stream_minute, stream_second = map(int, stream_time_gmt2.split(":"))
            if 0 <= stream_hour < 24 and 0 <= stream_minute < 60 and 0 <= stream_second < 60:
                break
        except ValueError:
            pass
    print("Format waktu tidak valid. Coba lagi.")

# Input dan validasi waktu saat ini (GMT+7)
while True:
    current_time_gmt7 = input("Masukkan waktu saat ini (GMT+7) dalam format HH:MM:SS: ").strip()
    if len(current_time_gmt7) == 8 and current_time_gmt7[2] == ':' and current_time_gmt7[5] == ':':
        try:
            current_hour, current_minute, current_second = map(int, current_time_gmt7.split(":"))
            if 0 <= current_hour < 24 and 0 <= current_minute < 60 and 0 <= current_second < 60:
                break
        except ValueError:
            pass
    print("Format waktu tidak valid. Coba lagi.")

# Mengonversi waktu acara streaming dari GMT+2 ke GMT
stream_hour_gmt = (stream_hour - 2) % 24

# Mengonversi waktu saat ini dari GMT+7 ke GMT
current_hour_gmt = (current_hour - 7) % 24

# Konversi ke detik untuk menghitung selisih waktu
stream_time_in_seconds = stream_hour_gmt * 3600 + stream_minute * 60 + stream_second
current_time_in_seconds = current_hour_gmt * 3600 + current_minute * 60 + current_second

# Menghitung selisih waktu
if current_time_in_seconds > stream_time_in_seconds:
    print("See you on the next Pear Event!")
else:
    wait_time_seconds = stream_time_in_seconds - current_time_in_seconds
    hours = wait_time_seconds // 3600
    minutes = (wait_time_seconds % 3600) // 60
    seconds = wait_time_seconds % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

