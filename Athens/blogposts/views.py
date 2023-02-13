from django.shortcuts import render
from .models import MarkdownFile

# Create your views here.
def markdown_view(request, pk):
	markdown_file = MarkdownFile.objects.get(pk=pk)
	markdown_content = markdown_file.get_html()
	return render(request, 'markdown.html', {'markdown_content': markdown_content})


def home_view(request):
    files = MarkdownFile.objects.all()
    return render(request, 'home.html', {'files': files})