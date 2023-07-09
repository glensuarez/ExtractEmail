from ast import pattern
from django.shortcuts import render
from .forms import DocumentUploadForm

import re
import openpyxl
from django.http import HttpResponse

def process_emails(text):
        # Utiliza expresiones regulares para buscar patrones de correo electr�nico en el texto
    pattern = r'[\w\.-]+@[\w\.-]+'
    emails = re.findall(pattern, text)
    return emails

def upload_document(request):
    if request.method == 'POST':
        try:
            form = DocumentUploadForm(request.POST, request.FILES)
            if form.is_valid():
                document = form.cleaned_data['document']
                # Procesa el archivo para buscar correos electr�nicos
                emails = process_emails(document.read().decode('utf-8'))
                # Generar archivo Excel con los correos encontrados
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                for i, email in enumerate(emails, start=1):
                    sheet.cell(row=i, column=1).value = email
                response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename=correos.xlsx'
                workbook.save(response)
                return response
            else:
                # Aqu� puedes agregar cualquier otro procesamiento que necesites
                # en caso de que el formulario no sea v�lido
                pass
        except Exception as e:
            #error_message = f"Error al procesar el archivo: {str(e)}"
            error_message = f"Error al procesar el archivo, debe tener formato txt"
            # Puedes almacenar el mensaje de error en una variable de contexto y pasarlo al template
            return render(request, 'upload.html', {'form': form, 'error_message': error_message})
    else:
        form = DocumentUploadForm()
    return render(request, 'upload.html', {'form': form})
