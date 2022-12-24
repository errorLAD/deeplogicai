from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import * 

import pdfplumber
import PyPDF2

from .forms import MyfileUploadForm
from .models import file_upload

def home(request):
        
      if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract the text from the PDF file
            pdf_file = request.FILES['pdf_file']
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ""
            for page in range(pdf_reader.getNumPages()):
                text += pdf_reader.getPage(page).extractText()

            # Save the text and file name to the Text model
            text_model = Text(text=text, file_name=pdf_file.name)
            text_model.save()

            return render(request, 'store/index.html', {'form': form, 'text': text})
           
        else:
            return HttpResponse('error')
      else:
            form = MyfileUploadForm()
            context = {"form": form,}
            return render(request, 'store/index.html',  context)






def show_file(request):  
    return render(request, 'store/view.html', context)
