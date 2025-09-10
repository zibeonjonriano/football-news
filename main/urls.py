from django.urls import path
from main.views import show_main, create_news, show_news, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-news/', create_news, name='create_news'),
    path('news/<str:id>/', show_news, name='show_news'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
]

# File urls.py berisi konfigurasi routing untuk aplikasi main.
# Impor fungsi path dari modul django.urls untuk mendefinisikan pola URL.
# Impor fungsi show_main dari main.views yang akan dipanggil saat URL cocok dengan pola yang ditentukan.
# app_name = 'main' digunakan untuk memberikan namespace unik pada URL dalam aplikasi, sehingga mudah dibedakan saat ada banyak aplikasi dan endpoint dalam proyek Django.
# urlpatterns adalah list berisi objek URLPattern yang dihasilkan oleh fungsi path().
# Pada contoh ini, hanya ada satu route '' (root), yang akan memanggil view show_main.
# Argumen opsional name='show_main' memudahkan kita melakukan reverse URL menggunakan nama, bukan hardcoded string path.