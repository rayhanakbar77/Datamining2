# Datamining2
# Rayhan Akbar Pradana
# A11.2022.14085

# Prediksi Nilai Rata-Rata Siswa

## Ringkasan

Proyek ini bertujuan untuk memprediksi nilai matematika siswa berdasarkan berbagai fitur seperti gender, kelompok, tingkat pendidikan orang tua, jenis makan siang, dan persiapan tes. Dengan menggunakan dataset "Student Study Performance", kita akan melakukan eksplorasi data, pemrosesan fitur, dan membangun model prediksi menggunakan regresi linear.

## Permasalahan

Bagaimana memprediksi nilai matematika siswa berdasarkan faktor-faktor yang ada?
Apakah ada fitur-fitur tertentu yang memiliki pengaruh signifikan terhadap nilai matematika siswa?.

## Tujuan

- Mengidentifikasi fitur-fitur yang mempengaruhi nilai matematika siswa.
- Membangun model yang dapat memprediksi nilai matematika siswa dengan akurasi yang baik.

## Model

Model yang digunakan dalam proyek ini adalah Regresi Linier.

## Alur

1. Pengumpulan Data
   Mengunduh dataset dari Kaggle.
   Mengekstraksi file dataset.
   Eksplorasi Data

2. Memahami struktur data.
   Melakukan visualisasi distribusi harga dan hubungan antar variabel.
   Pra-pemrosesan Data

3. Menggabungkan dataset.
   Mengatasi data yang hilang atau tidak konsisten.
   Pemodelan

4. Membuat model regresi linier.
   Melatih model dengan data yang tersedia.
   Evaluasi Model

5. Mengevaluasi kinerja model menggunakan metrik seperti Mean Absolute Error (MAE) dan Root Mean Squared Error (RMSE).
   Diskusi dan Kesimpulan

6. Menganalisis hasil prediksi.
   Menarik kesimpulan dari proyek ini.

## Dataset

![App Screenshot](./gambar/dataset.png)

Dataset "Student Study Performance" berisi informasi tentang siswa dan nilai mereka dalam mata pelajaran matematika, membaca, dan menulis. Berikut adalah beberapa fitur utama dalam dataset:

- Gender: Gender siswa (male/female)
- Group: Kelompok siswa berdasarkan performa (group A, group B, group C, group D, group E)
- Parent Education Level: Tingkat pendidikan orang tua
- Lunch: Jenis makan siang (standard/free/reduced)
- Test Preparation: Status persiapan tes (none/completed)
- Math Score: Nilai matematika
- Reading Score: Nilai membaca
- Writing Score: Nilai menulis

### Exploratory Data Analysis (EDA)

        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 1000 entries, 0 to 999
        Data columns (total 8 columns):
        #   Column                       Non-Null Count  Dtype
        ---  ------                       --------------  -----
        0   gender                       1000 non-null   object
        1   race_ethnicity               1000 non-null   object
        2   parental_level_of_education  1000 non-null   object
        3   lunch                        1000 non-null   object
        4   test_preparation_course      1000 non-null   object
        5   math_score                   1000 non-null   int64
        6   reading_score                1000 non-null   int64
        7   writing_score                1000 non-null   int64
        dtypes: int64(3), object(5)
        memory usage: 62.6+ KB

- distribusi frekuensi dari setiap kolom kategorikal.
  ![App Screenshot](./gambar/eda.png)

- distribusi kolom numerik berdasarkan kelompok
  ![App Screenshot](./gambar/score.png)

- distribusi kolom numerik berdasarkan gender
  ![App Screenshot](./gambar/gender.png)
- Menampilkan informasi dasar tentang dataset (jumlah baris, kolom, tipe data).
- Menghitung statistik deskriptif untuk fitur numerik.
- Memvisualisasikan distribusi fitur numerik dan kategorikal.
- Mengecek keberadaan nilai kosong dan duplikasi.

### Proses Features Dataset

        df = df.rename(columns = {df.columns[1] : 'group',
                                df.columns[2] : 'parent_education_Level',
                                df.columns[4] : 'test_preparation'})

        df['total_score'] = df['math_score'] + df['reading_score'] + df['writing_score']
        df['mean_score'] = round(df['total_score'] / 3,1)

- Mengubah nama kolom untuk mempermudah analisis.
- Menghitung total score dan mean score dari tiga mata pelajaran.
- Mengubah fitur kategorikal menjadi numerik menggunakan mapping

## Proses Learning/Modeling

1. Preprocessing

Menghapus kolom yang tidak diperlukan.
Mengubah nilai kategorikal menjadi numerik.

2. Membagi Data

Membagi data menjadi set pelatihan dan set pengujian (80% pelatihan, 20% pengujian).

3. Membangun Model

Menggunakan regresi linear untuk membangun model prediksi.

4. Evaluasi Model

Mengukur kinerja model menggunakan metrik seperti MAE, MSE, dan R² score.

## Performa Model

Hasil evaluasi model pada set pengujian

    MAE : 1.2603529331300933e-14
    MSE : 2.786424504257369e-28
    r2_score : 1.0

## Diskusi Hasil dan Kesimpulan

#### Diskusi Hasil

Model regresi linear memberikan gambaran tentang bagaimana fitur-fitur yang ada mempengaruhi nilai matematika siswa.
Fitur-fitur seperti gender, kelompok, jenis makan siang, dan persiapan tes menunjukkan adanya hubungan dengan nilai matematika.

#### Kesimpulan

Model yang dibangun berhasil memprediksi nilai matematika dengan tingkat akurasi yang dapat diterima.
Beberapa fitur memiliki pengaruh signifikan terhadap performa akademik siswa dalam mata pelajaran matematika.
Pendekatan ini dapat digunakan untuk memberikan wawasan kepada pendidik dan orang tua tentang faktor-faktor yang mempengaruhi performa akademik siswa.
