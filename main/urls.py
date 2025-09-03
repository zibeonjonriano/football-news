from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

# File urls.py berisi konfigurasi routing untuk aplikasi main.
# Impor fungsi path dari modul django.urls untuk mendefinisikan pola URL.
# Impor fungsi show_main dari main.views yang akan dipanggil saat URL cocok dengan pola yang ditentukan.
# app_name = 'main' digunakan untuk memberikan namespace unik pada URL dalam aplikasi, sehingga mudah dibedakan saat ada banyak aplikasi dan endpoint dalam proyek Django.
# urlpatterns adalah list berisi objek URLPattern yang dihasilkan oleh fungsi path().
# Pada contoh ini, hanya ada satu route '' (root), yang akan memanggil view show_main.
# Argumen opsional name='show_main' memudahkan kita melakukan reverse URL menggunakan nama, bukan hardcoded string path.