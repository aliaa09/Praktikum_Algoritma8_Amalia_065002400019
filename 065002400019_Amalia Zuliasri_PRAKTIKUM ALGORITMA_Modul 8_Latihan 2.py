def pangkat(base, power):
    """Fungsi rekursif untuk menghitung perpangkatan."""
    if power == 0:
        return 1  
    elif power > 0:
        return base * pangkat(base, power - 1)  
    else:
        return 1 / pangkat(base, -power)  

if __name__ == "__main__":
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    
    while True:
        try:
            base_input = input("\nMasukkan Angka: ")
            if base_input == "":  
                print("Program Selesai")
                break
            
            power_input = input("Masukkan Pangkatnya: ")
            if power_input == "":
                print("Program Selesai")
                break

           
            base = int(base_input)
            power = int(power_input)

           
            hasil = pangkat(base, power)
            print(f"Hasilnya adalah: {hasil}")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

