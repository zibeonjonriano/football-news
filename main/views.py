from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406355634',
        'name': 'Zibeon Jonriano Wisnumoerti',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)