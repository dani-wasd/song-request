from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is the requests index.")

# In your views.py file
song_requests = []

def submit_song_request(request):
    if request.method == 'POST':
        song_title = request.POST.get('song_title')
        song_requests.append(song_title)
        # Additional logic for handling the song request
        return redirect('success_page')

    return render(request, 'submit_song.html')