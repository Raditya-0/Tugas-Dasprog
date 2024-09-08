print("\nTAXI FARE CALCULATOR\n")

start_odometer = float(input("Enter beginning odometer reading => ")) # Untuk input lokasi awal
end_odometer = float(input("Enter ending odometer reading => ")) # Untuk input lokasi akhir

jarak = end_odometer - start_odometer # Mencari selisih untuk menemukan jarak
uang = jarak * 1.50 # Jarak dikali dengan biaya taksi untuk menemukan tarif

print(f"You traveled a distance of {jarak:.1f} miles. At $1.50 per mile, your fare is ${uang:.2f}")