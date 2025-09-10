from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    news_list = News.objects.all()
    # Fungsi show_main diperbarui dengan menambahkan News.objects.all() untuk mengambil seluruh objek News yang tersimpan pada database.

    context = {
        'npm' : '2406355634',
        'name': 'Zibeon Jonriano Wisnumoerti',
        'class': 'PBP D',
        'news_list' : news_list
    }

    return render(request, "main.html", context)

# Fungsi create_news digunakan untuk menghasilkan form yang dapat menambahkan data News secara otomatis ketika data di-submit dari form.
def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_news.html", context)

# Fungsi show_news menggunakan get_object_or_404(News, pk=id) untuk mengambil objek News berdasarkan primary key (id). Jika objek tidak ditemukan, akan mengembalikan halaman 404.
def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()  # news.increment_views() digunakan untuk menambah jumlah views pada berita tersebut.

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)

# fungsi baru yang menerima parameter request dengan nama show_xml dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada News.
def show_xml(request):
    news_list = News.objects.all()
    xml_data = serializers.serialize("xml", news_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, news_id):
    try:
        news_item = News.objects.filter(pk=news_id)
        xml_data = serializers.serialize("xml", news_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except News.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, news_id):
    try:
        news_item = News.objects.get(pk=news_id)
        json_data = serializers.serialize("json", [news_item])
        return HttpResponse(json_data, content_type="application/json")
    except News.DoesNotExist:
        return HttpResponse(status=404)