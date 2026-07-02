import streamlit as st
from google import genai

# Mengatur konfigurasi halaman web
st.set_page_config(page_title="Generator RPP Deep Learning", layout="wide")

st.title("⛪ Generator RPP / Modul Ajar Katolik")
st.subheader("Berbasis Pembelajaran Mendalam (Deep Learning) - Cetak A4 Resmi")
st.write("Isi formulir di bawah ini untuk merancang RPP secara otomatis menggunakan AI.")

# --- SIDEBAR INPUT ---
st.sidebar.header("🔑 Pengaturan API Key")
api_key = st.sidebar.text_input("Masukkan Google GenAI API Key Anda:", type="password")

st.sidebar.header("✍️ Identitas Sekolah & Penulis")
sekolah = st.sidebar.text_input("Nama Sekolah:", "SMP Negeri 1 Metro")
kepala_sekolah = st.sidebar.text_input("Nama Kepala Sekolah:", "Fatimah, S.Pd. M.M.")
nip_kepala_sekolah = st.sidebar.text_input("NIP Kepala Sekolah:", "19670705 199202 2 002")
penulis = st.sidebar.text_input("Nama Penulis Modul:", "Antonius Tamtama, S.S")
nip_penulis = st.sidebar.text_input("NIP Penulis:", "198211212024211003")

# --- FORM UTAMA INPUT ---
col1, col2 = st.columns(2)

with col1:
    mapel = st.text_input("Mata Pelajaran:", "Pendidikan Agama Katolik")
    kelas_fase = st.text_input("Kelas / Fase:", "Kelas 8 / Fase D")
    elemen = st.selectbox("Elemen Pembelajaran:", ["Yesus Kristus", "Peserta Didik", "Gereja", "Masyarakat"])
    topik_bahasan = st.text_input("Topik / Pokok Bahasan:", "Yesus yang mengutus Roh Kudus")

with col2:
    tujuan_pembelajaran = st.text_area("Tujuan Pembelajaran:", "Murid Memahami Yesus yang mengutus Roh Kudus")
    kktp = st.text_area("Kriteria Ketercapaian Pembelajaran (KKTP):", "1. Mengidentifikasi alasan Yesus mengutus Roh Kudus...")
    waktu = st.number_input("Jumlah Pertemuan (1 Pertemuan = 120 Menit):", min_value=1, max_value=10, value=2)

st.header("⚙️ Parameter Pembelajaran Mendalam")
col3, col4 = st.columns(2)

with col3:
    dimensi_profil_lulusan = st.text_input("Dimensi Profil Lulusan:", "Keimanan dan Ketakwaan terhadap Tuhan YME, Penalaran Kritis")
    praktik_pedagogis = st.text_input("Praktik Pedagogis:", "Diskusi, Kateketis")
    lingkungan_pembelajaran = st.text_input("Lingkungan Pembelajaran:", "Ruang Kelas")

with col4:
    kemitraan_pembelajaran = st.text_input("Kemitraan Pembelajaran:", "Orang Tua, Lingkungan / Kring")
    pemanfaatan_digital = st.text_input("Pemanfaatan Digital:", "Canva for Education, Video, LCD Projector")
    persiapan_pembelajaran = st.text_area("Persiapan Guru:", "Guru menyiapkan presentasi materi pembelajaran, LKPD")

# --- PROSES GENERATE ---
if st.button("🚀 Generate RPP / Modul Ajar", type="primary"):
    if not api_key:
        st.error("Silakan masukkan API Key Anda di sidebar terlebih dahulu!")
    else:
        with st.spinner(f"Sedang merancang RPP untuk {waktu} pertemuan... Mohon tunggu sekitar 15-20 detik."):
            try:
                client = genai.Client(api_key=api_key)
                
                prompt_text = f"""
                Buatkan Rencana Pelaksanaan Pembelajaran (RPP) / Modul Ajar berbasis Pembelajaran Mendalam (Deep Learning) secara LENGKAP untuk {waktu} pertemuan. 
                Gunakan Alkitab, ajaran sosial gereja Katolik, Katekismus gereja katolik dan Kitab hukum kanonik sebagai referensi utama. 
                Setiap 1 pertemuan terdiri dari 120 menit. Bagi waktu di setiap pertemuan agar sesuai dengan kegiatan awal, kegiatan inti, dan penutup.
                
                PENTING: Anda harus menyusun output ini menggunakan format HTML murni yang rapi dan elegan agar langsung siap dicetak di kertas A4.
                Jangan gunakan markdown biasa (seperti ## atau **). Gunakan tag HTML seperti <h1>, <h2>, <p>, <ul>, <li>, dan <table>.
                
                Detail Kelas & Desain:
                - Sekolah: {sekolah} | Penulis: {penulis}
                - Mata Pelajaran: {mapel} | Kelas/Fase: {kelas_fase} | Elemen: {elemen}
                - Topik/Pokok Bahasan: {topik_bahasan} | Tujuan Pembelajaran: {tujuan_pembelajaran}
                - Total Waktu Rencana: {waktu} Pertemuan | KKTP: {kktp}
                - Dimensi Profil Lulusan: {dimensi_profil_lulusan} | Praktik Pedagogis: {praktik_pedagogis}
                - Lingkungan: {lingkungan_pembelajaran} | Kemitraan: {kemitraan_pembelajaran}
                - Digital: {pemanfaatan_digital} | Persiapan: {persiapan_pembelajaran}
                
                Struktur RPP harus mengikuti susunan berikut:
                - Judul Modul yang menarik di bagian atas.
                - 1. Identitas RPP & Desain Pembelajaran (Buat rapi di dalam tabel HTML).
                - 2. Langkah Pembelajaran: Wajib dijabarkan detail satu per satu dari Pertemuan 1 sampai Pertemuan ke-{waktu}. Setiap pertemuan memuat Kegiatan Awal (15 mnt), Kegiatan Inti (90 mnt), Kegiatan Akhir (15 mnt).
                - 3. Asesmen Formatif & Lembar Kerja Murid (LKM) untuk tiap pertemuan.
                - 4. Asesmen Sumatif (20 soal pilihan ganda HOTS dan Kunci Jawaban).
                - 5. Referensi / Daftar Pustaka resmi Katolik.
                
                Di akhir halaman dokumen, buatlah layout tanda tangan kiri-kanan menggunakan tabel HTML transparan:
                Sebelah kiri: Mengetahui, Kepala Sekolah {kepala_sekolah} (NIP: {nip_kepala_sekolah})
                Sebelah kanan: Metro, Penulis {penulis} (NIP: {nip_penulis})
                """
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt_text,
                )
                
                # Simpan hasil ke dalam session state agar tidak hilang saat halaman memuat ulang
                st.session_state['rpp_html'] = response.text
                st.success("🎉 RPP Berhasil Dibuat!")
                
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menghubungi Gemini API: {e}")

# --- TAMPILAN HASIL & TOMBOL CETAK ---
if 'rpp_html' in st.session_state:
    st.markdown("---")
    st.header("📄 Hasil Pratinjau Dokumen RPP")
    
    # Skrip JavaScript untuk memicu cetak jendela browser pada area tertentu saja
    print_js = """
    <script>
    function printDiv() {
        var printContents = document.getElementById('printableArea').innerHTML;
        var originalContents = document.body.innerHTML;
        document.body.innerHTML = "<html><head><title>Cetak RPP</title><style>@page { size: A4; margin: 25mm; } body { font-family: Arial, sans-serif; line-height: 1.6; }</style></head><body>" + printContents + "</body></html>";
        window.print();
        document.body.innerHTML = originalContents;
        window.location.reload();
    }
    </script>
    <button onclick="printDiv()" style="background-color: #4CAF50; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; margin-bottom: 20px;">
        🖨️ Cetak Langsung ke Kertas A4 / Simpan ke PDF
    </button>
    """
    
    # Render tombol cetak HTML/JS
    st.components.v1.html(print_js, height=60)
    
    # Tampilkan pratinjau dokumen di dalam container khusus yang bisa dicetak
    html_content = f"""
    <div id="printableArea" style="padding: 30px; border: 1px solid #ccc; background-color: white; color: black; font-family: Arial, sans-serif; line-height: 1.6;">
        {st.session_state['rpp_html']}
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)