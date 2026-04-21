from django import forms

class ExcelImportForm(forms.Form):
    excel_file = forms.FileField(label='Excel файл', help_text='Файл с листами: category, products')