# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga mahasiswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin mahasiswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Melalui permasalahan diatas, sebagai seorang data scientist berupaya untuk mengidentifikasi berbagai faktor yang mempengaruhi banyaknya mahasiswa yang dropout. Selain identifikasi, tahapan analisis melalui visual dan juga membuat sistem machine learning untuk dapat menklasifikan mahamahasiswa yang droup kemudian ditampilkan dalam sebuah dashboard untuk memonitor berbagai faktor.

### Deskripsi Permasalahan

Terdapat beberapa hal yang bisa diambil dari latar belakang diatas khususnya bagian permasalahan utama adalah banyaknya mahasiswa yang dropout. Melalui permasalahan utama tersebut dapat dibagi ke dalam beberapa bagian kecil untuk nantinya di analisis dalam menemukan jawaban atau kesimpulan yang mampu memberikan solusi dari permasalahan Jaya Jaya Institut. Penyebab banyak mahasiswa dropout bisa didukung oleh beberapa kemungkinan diantaranya

Main Problem : Banyaknya mahasiswa Dropout Sejak Jaya Jaya Institut Didirikan

- Latar belakang keluarga yang berbeda masing-masing mahasiswa
- Status pernikahan mahasiswa
- Nilai studi ujian performa mahasiswa
- Bidang atau Jurusan mahasiswa
- Waktu kehadiran kelas mahasiswa
- Jenis aplikasi mahasiswa ke sekolah

Sebelum ke tahapan pemahaman data perlu disusun beberapa problem statement untuk menentukan permasalahan dengan lebih jelas. Pertanyaan tersebut disusun untuk dapat menjawab solusi melalui insight data.

#### Problem Statement

Berikut beberapa pertanyaan yang disusun untuk dijadikan acuan dalam menggali insight data nantinya untuk mencari jawaban serta solusi yang dibutuhkan :
- Bagaimana perbandingan mahasiswa yang lulus dan dropout?
- Bagaimana persebaran data mahasiswa yang dropout berdasarkan status pernikahan?
- Bagaimana perbandingan mahasiswa dropout berdasarkan gender?
- Bagaimana perbandingan data Umur mahasiswa pada saat pendaftaran ke Jaya Jaya Institut?
- Apa pengaruh bidang atau jurusan mahasiswa terhadap mahasiswa dropout dan lulus?
- Bagaimana persebaran mahasiswa International pada masing-masing Jurusan?
- Bagaimana pengaruh waktu kehadiran mahasiswa terhadap mahasiswa yang dropout?
- Bagaimana pengaruh kewarganegaraan mahasiswa dapat berpengaruh terhadap mahasiswa dropout?
- Apakah ada pengaruh Educational Special Needs terhadap performa mahasiswa dropout?
- Apakah ada pengaruh mahasiswa yang Debtor terhadap performa mahasiswa?
- Apakah ada pengaruh penerima beassiswa terhadap Status mahasiswa dropout atau lulus?
- Bagaimana korelasi Status mahasiswa dengan fitur yang lainnya?

#### Goals

Tujuan dari pembuatan proyek ini adalah sebagai berikut
- Mendapatkan insight melalui hubungan performa mahasiswa dengan beberapa paramater atau variabel yang ada pada data Jaya Jaya Institut.
- Membuat dashboard untuk dapat dianalisis secara visual disesuaikan dengan kebutuhan Jaya Jaya Institut untuk dapat memantau dan menganalisis performa mahasiswa.
- Menemukan jawaban serta memberikan solusi kepada Jaya Jaya Institut terkait permasalahan performa mahasiswa.
- Membuat sistem berbasis machine learning untuk menklasifikasikan mahasiswa yang memiliki potensi dropout tinggi dengan mahasiswa yang tidak. 

### Cakupan Proyek

Beberapa tahapan yang dilakukan pada proyek ini adalah sebagai berikut

1. Pengumpulan Data dan Pemahaman Data
   
   Tahapan ini terdiri dari beberapa bagian seperti import library yang dibutuhkan untuk proyek, import dataset karyawan sesuai ketentuan, memahami isi data melalui info() & describe(), mengecek nilai NaN atau NULL pada data, mengecek duplikat data serta mengecek data unik berupa kategori pada masing-masing kolom. Perlu dilakukan untuk melihat karakteristik dari tiap kolom bahkan termasuk kolom yang bertipe numerik untuk melihat nilai mean, min, max, standar deviasi dan kuartalnya.

2. Data Cleaning & Preparation

   Tahapan data preparation terbagi menjadi dua bagian yaitu data preparation untuk analisis dan data preparation untuk modeling. Hal ini dilakukan karena keduanya punya behaviour yang berbeda. 

   a. Data Preparation for Analysis

   Analisis digunakan untuk melihat pola kolom-kolom yang sekiranya berpengaruh dengan Status sehingga data yang digunakan merupakan data real sesuai yang ada di dataset. Pada analisis tahapan data preparation berfokus pada menghilangkan nilai NaN atau NULL dan penyesuaian nama kategori pada kolom.

   b. Data Preparation for Modeling

   Data prep untuk modeling dilakukan sebagai tahapan menyesuaikan dataset dengan environment model algoritma machine learning dalam membaca data. Beberapa aturan yang umum sebelum membuat model machine learning adalam membuat data yang dipunya mudah dibaca oleh sistem.

3. Exploratory Data Analysis berdasarkan problem statement yang disusun

   Menggunakan data preparation untuk analisis, data yang sebelumnya sudah diolah serta diseusaikan akan dibuat ke dalam bentuk visual tertentu misal bar chart, boxplot maupun histogram. Fokus dari EDA ini adalam membentuk visual yang menghubungkan data Status dengan variabel tertentu yang sesuai dengan pertanyan di awal problem statement. Hal tersebut dilakukan agar lingkup dari proyek tidak melebar kemana-mana dalam pembahasannya.

4. Pengembangan Sistem Klasifikasi Mahasiswa Status Dropout dan Graduated berbasis Machine Learning

   Tahapan modeling menggunakan data preparation untuk modeling. Ada beberapa algoritma yang akan digunakan yaitu 
   - Algoritma K-Nearest Neighbor
   - Algoritma SVM
   - Algoritma Decision Tree
   - Algoritma Random Forest
   - Algoritma Boosting Algorithm
   
   Dari kelima algoritma diatas akan dipilih satu dengan nilai akurasi yang paling tinggi melalui tahao evaluasi. Kemudian hasil model dikonversi ke dalam bentuk .pkl yang akan digunakan pada sistem klasifikasi mahasiswa Status Dropout dan Graduated.

5. Membuat Dashboard Analysis Mahasiswa Status Dropout dan Graduated menggunakan Metabase yang terintegrasi dengan Supabase

   Dashaboard analisis akan dibuat di metabase melalui docker. Dataset yang digunakan merupakan data hasil olahan pada bagian Data Preparation for Analysis. Dataset diupload ke supabase kemudian dikoneksikan ke metabase.

6. Membuat Sistem Prediksi Menggunakan Streamlit

   Sistem prediksi dibuat untuk dapat menemukan mahasiswa yang memiliki potensi Dropout. Sistem akan melakukan klasifikasi mahasiswa Graduated dan Dropout melalui beberapa ciri-ciri atau parameter yang diberikan.


### Persiapan

Sumber data : [Dataset Mahasiswa Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment - notebook :

```
python -m venv main-ds
main-ds\Scripts\activate
pip install -r requirements.txt

Notebook dikerjakan di Google Collaboratory
a. numpy==1.26.4
b. pandas==2.2.2
c. matplotlib==3.8.0
d. seaborn==0.13.2
```

Setup environment - shell/terminal :

```
mkdir Proyek_Analisis_Solusi_Performa_Mahasiswa
cd Proyek_Analisis_Solusi_Performa_Mahasiswa
pipenv install
pipenv shell
pip install -r requirements.txt
```

#### Run Aplikasi Sistem Klasifikasi Mahasiswa Dropout

![predictapp](https://raw.githubusercontent.com/Abito21/Proyek_Analisis_Solusi_Performa_Mahasiswa/main/pictures/abidindraswara-predictappstreamlit.png)

Sistem klasifikasi saat ini bisa dijalankan melalui Google Collaboratory pada cell dengan menjalankan kode program yang berada di file `predict.py`. Atau bisa menjalankan di lokal dengan update kode upload dan kode model di sesuaikan

Jalankan di terminal
```bash
streamlit run predict.py
```

Atau dapat diakses secara online pada link berikut : [Students Predict App]()

Step menggunakan aplikasi prediksi :
1. Buka Streamlit Student Predict App
2. Upload File format csv
3. Klik Button Prediksi
4. Muncul tabel hasil prediksi
5. Selamat mencoba!

## Business Dashboard

Dashboard yang dibuat merupakan hasil analisis dari EDA based on Question. Setidaknya beberapa variabel utama yang dibandingkan dengan variabel Status untuk menganalisis masing-masing persebaran datanya. Beberapa variabel tersebut diantaranya Marital Status, Gender, Umur pada saat Mendaftar, Bidang Keilmun atau Jurusan, Waktu Kehadiran Kuliah, Debtor dan Scholarship Holder. Terdapat filter untuk beberapa data yang disajikan secara total yaitu Filter Status untuk menyaring beberapa informasi berdasarkan mahasiswa Enrolled, mahasiswa Graduated dan mahasiswa Dropout. Dashboard disajikan seringkas mungkin agar mudah dibaca oleh tim analisis Jaya Jaya Institut.

![dashboard](https://raw.githubusercontent.com/Abito21/Proyek_Analisis_Solusi_Performa_Mahasiswa/main/pictures/abidindraswara-dashboard.png)

## Conclusion

Hasil analisis yang sudah dibuat pada tahapan EDA - Based on Questions dapat diambil kesimpulan dari beberapa alasan utama yaitu Marital Status, Gender, Umur pada saat Mendaftar, Bidang Keilmun atau Jurusan, Waktu Kehadiran Kuliah, Debtor dan Scholarship Holder. Berikut penjelasan kesimpulan secara detail untuk masing-masing alasan diatas
- Berdasarkan Marital Status atau Status Pernikahannya mahasiswa yang single lebih banyak daripada yang tidak dan mahasiswa yang single memiliki presentase Graduated lebih besar 51.4%. Mahasiswa yang memiliki peluang dropout kebanyakan memiliki Status Pernikahan yaitu married 47.2%, divorced 46,2% dan legally separated 66.7%. Marital Status memberikan pengaruh pada performa mahasiswa karena dimungkinkan adanya distraksi selama studi berlangsung.
- Gender laki-laki memiliki data presentase data Status Dropout lebih besar yaitu sebesar 45.1%. Dibandingkan dengan perempuan yang justru presentasenya menghasilkan kelulusan mahasiswa sebesar 57.9%. Hal tersebut terjadi kemungkinan karena secara penelitian perempuan lebih rajin dan bisa melakukan multitastking dalam pekerjaan harian serta studinya secara bersamaan sehingga memberikan peluang kepada perempuan untuk dapat lulus studi dengan baik.
- Secara umur sebagian besar mahasiswa yang mendaftar ke Jaya Jaya Institut merupakan mahasiswa dengan umur muda antara 18 hingga 30 tahun. Usia muda memiliki produktivitas lebih baik dibandingkan usia 30 tahun ke atas memungkinkan penyelesaian studi hingga lulus. Namun tidak dipungkiri bahwa usia muda dengan faktor faktor lain seperti yang sudah disebutkan diatas seperti Marital Status, Gender, Bidang Keilmun atau Jurusan, Waktu Kehadiran Kuliah dan Debtor mampu memberikan dampak Status Dropout pada mahasiswa.
- Bidang Keilmuan atau Jurusan tertentu seperti urusan Basic Education, Biofuel Production Technologies, Informatics Engineering, Equinculture dan Management (evening attendance) mempunyai data mahasiswa dengan Status Dropout lebih banyak dibandingkan Status Graduated. Jurusan yang paling banyak diminati serta lulus adalah jurusan Nursing dan Social Service. Kebidangan yang berbasis Teknik maupun Basic Education memiliki peluang Dropout banyak. Hal ini dapat disebabkan karena bisa jadi tingginya kriteria kelulusan, ilmu advance yang tidak mudah untuk diselesaikan, minat yang kurang dan bisa jadi segi biaya studi pada jurusan tersebut yang mahal.
- Waktu kehadiran kuliah terdiri dari kelas siang dan kelas malam. Melalui hasil visual analisis didapati bahwa mahasiswa yang hadir pada kelas siang memiliki presentase untuk lulus lebih banyak dibandingkan yang dropout. Sedangkan kelas malam memiliki presentase 42.9% Dropout, 41.6% Graduated dan sisanya masih berkuliah. Hal ini bisa terjadi karena kelas siang mampu memberikan konsentrasi lebih baik dibandingkan yang kelas malam. Kelas malam umumnya biasa diisi oleh mahasiswa yang memang memiliki prioritas utama diluar seperti bekerjam ataupun berkeluarga. Sehingga bisa menyebabkan peluang dropout yang tinggi.
- Debtor atau mahasiswa yang memiliki tanggungan pinjaman/kredit memiliki presentase kelulusan yang lebih sedikit daripada yang dropout. Memiliki tingkat performa yang buruk dan fokus belajar yang tidak bagus.
- Mahasiswa Scholarship Holder/penerima beasiswa memiliki motivasi yang tinggi untuk lulus terlihat dari data secara presentase mahasiswa yang lulus dengan keterangan penerima beasiswa sebesar 76%. Sebaliknya yangbukan penerima beasiswa presentase lulusnya hanya sebesar 41% tidak mencapai setengah populasi mahasiswa keseluruhan yang bukan penerima beasiswa.

Terdapat juga beberapa variabel yang memilii hubungan cukup kuat dengan variabel Status. Melalui korelasi matrix terdapat beberapa variaebal berikut korelasi matrix Tuition_fees_up_to_date, Curriculum_units semester 1 & semester 2, GDP dan Previous_qualification.

Melalui model machine learning yang dibuat dari kelima algoritma terdapat algoritma terbaik dengan nilai akurasi tinggi yaitu XGBoost. Model machine learning dibuat untuk pada mengklasifikasikan mahasiswa yang memiliki potensi Dropout dan Graduated sehingga bisa diambil tindakan preventif awal agar Mahasiswa Dropout dapat dikurangi. Akurasi yang didapatkan cukup stabil menggunakan XGBoost dari training dan testing sehingga sistem prediksi mampu memberikan nilai yang mendekati klasifikasi yang baik.

### Rekomendasi Action Items

Terdapat beberapa hal yang dapat dilakukan oleh Jaya Jaya Institut agar dapat meminimalisir mahasiswa yang Dropout diantaranya

- Program khusus bagi mahasiswa dengan (Marital Status) Status Pernikahan Non-Single diantaranya memberikan kemudahan kelas online atau hybrid. Menyediakan fleksibilitas pembelajaran tatap muka maupun online untuk memberikan ruang belajar bagi mahasiswa dengan Status Pernikahan Non-Single.
- Waktu Kehadiran (Daytime_evening_attended) untuk dapat mengadakan proporsi kelas siang yang lebih besar daripada proporis kelas malam. Selain itu untuk kelas malam bisa diadakan kelas online agar aktifitas kehadiran tatap muka di malam hari menjadi lebih minimal dan bisa fokus ke pembelajaran.
- Jaya Jaya Institut perlu menyediakan mekanisme kredit maupun pembayaran studi bertahap untuk memudahkan mahasiswa melunasi biaya studinya. Hal ini berlaku untuk kredit maupun angsuran khusus untuk biaya studi. Sehingga mahasiswa tidak terbebani masalah biaya kuliah dan mampun menyisihkan uang saku mahasiswa dengan baik.
- Membuat semacam sistem untuk mengingatkan ke mahasiswa mengenai tenggang pembayaran biaya studi per semester agar memudahkan informasi mahasiswa dan menghindari adanya pinjaman yang membebani mahasiswa.
- Pertimbangan peningkatan atau penyerapan penerima beasiswa bagi mahasiswa dengan kriteria tertentu diantaranya beasiswa bagi mahasiswa yang kurang mampu,  beasiswa bagi mahasiswa berprestasi dan beasiswa bagi mahasiswa dengan nilai akademik tinggi. Hal ini dimaksudkan agar mahasiswa memiliki motivasi tinggi dalam menyelesaikan studinya dengan baik.