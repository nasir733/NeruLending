from django.shortcuts import render
from django.views import View


class ChromeExtentionIndexView(View):
    def get(self, request):
        return render(request, "chromeextention-index.html")
