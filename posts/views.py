from django.shortcuts import render, HttpResponse

def main_view(request):
    return HttpResponse("The Ferrari 488 (Type F142M) is a mid-engine sports car produced by the Italian automobile manufacturer Ferrari. The car replaced the 458, being the first mid-engine Ferrari to use a turbocharged V8 since the F40. It was succeeded by the Ferrari F8.")

def html_view(request):
    return render(request, "main.html")
