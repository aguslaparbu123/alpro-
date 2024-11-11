def hitung_total_daya(daya, lama_pemakaian):
    total_hari = daya * lama_pemakaian
    return total_hari 

def hitung_pemakaian_bulanan(total_daya):
    total_bulan = total_daya / 1000 * 30  # Konversi ke kWh dan hitung selama 30 hari
    return total_bulan

def hitung_biaya_listrik(pemakaian_bulanan):
    harga_per_bulan = pemakaian_bulanan * 1500
    return harga_per_bulan

def main():
    a = int(input('Masukan lama pemakaian TV per jam: '))
    b = int(input('Masukan lama pemakaian kipas per jam: '))
    c = int(input('Masukan lama pemakaian lampu per jam: '))
    
    tv = int(input('Masukan daya TV: '))
    kipas = int(input('Masukan daya kipas: '))
    lampu = int(input('Masukan daya lampu: '))
    
    total_daya_tv = hitung_total_daya(tv, a)
    total_daya_kipas = hitung_total_daya(kipas, b)
    total_daya_lampu = hitung_total_daya(lampu, c)
    
    pemakaian_bulanan_tv = hitung_pemakaian_bulanan(total_daya_tv)
    pemakaian_bulanan_kipas = hitung_pemakaian_bulanan(total_daya_kipas)
    pemakaian_bulanan_lampu = hitung_pemakaian_bulanan(total_daya_lampu)
    
    
    biaya_tv = hitung_biaya_listrik(pemakaian_bulanan_tv)
    biaya_kipas = hitung_biaya_listrik(pemakaian_bulanan_kipas)
    biaya_lampu = hitung_biaya_listrik(pemakaian_bulanan_lampu)
    
    total_biaya = biaya_tv + biaya_kipas + biaya_lampu
    
    print(f'Total pemakaian TV per bulan: {pemakaian_bulanan_tv: ,.2f} kWh')
    print(f'Total pemakaian kipas per bulan: {pemakaian_bulanan_kipas: ,.2f} kWh')
    print(f'Total pemakaian lampu per bulan: {pemakaian_bulanan_lampu: ,.2f} kWh')
    print()
    print(f'Biaya penggunaan listrik TV sebulan: Rp {biaya_tv: ,.2f}')
    print(f'Biaya penggunaan listrik kipas sebulan: Rp {biaya_kipas: ,.2f}')
    print(f'Biaya penggunaan listrik lampu sebulan: Rp {biaya_lampu: ,.2f}')
    print(f'Biaya penggunaan listrik keseluruhan sebulan: Rp {total_biaya: ,.2f}')

# Memanggil fungsi utama
main()
