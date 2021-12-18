def handle_uploaded_file(f):
    with open('HomePage/static/worksheets/worksheet '+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
