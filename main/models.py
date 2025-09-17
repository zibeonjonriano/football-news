import uuid
from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'), 
    ]
    # models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
    # News adalah nama model yang kamu definisikan.
    # CATEGORY_CHOICES adalah tuple yang mendefinisikan pilihan kategori berita yang tersedia.
    # id adalah field bertipe UUIDField yang digunakan sebagai primary key dan nilainya di-generate otomatis menggunakan uuid.uuid4.
    # title adalah field bertipe CharField untuk judul berita, dengan panjang maksimal 255 karakter.
    # content adalah field bertipe TextField untuk isi berita yang dapat menampung teks panjang.
    # category adalah field bertipe CharField dengan pilihan terbatas sesuai CATEGORY_CHOICES, dengan nilai default 'update'.
    # thumbnail adalah field bertipe URLField untuk menyimpan URL gambar thumbnail berita (opsional).
    # news_views adalah field bertipe PositiveIntegerField yang menyimpan jumlah view berita, dengan nilai default 0.
    # created_at adalah field bertipe DateTimeField yang otomatis berisi tanggal dan waktu saat data dibuat.
    # is_featured adalah field bertipe BooleanField untuk menandai apakah berita ini ditampilkan sebagai berita unggulan.
    # Method __str__ digunakan untuk mengembalikan representasi string dari objek (dalam hal ini judul berita).
    # Decorator @property digunakan untuk membuat atribut read-only yang nilainya merupakan hasil perhitungan dari atribut lain. Dalam kasus ini, is_news_hot akan bernilai True jika jumlah view berita lebih dari 20.
    # Method increment_views() digunakan untuk menambah jumlah view berita sebesar 1 dan menyimpan perubahan ke database.

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    news_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()