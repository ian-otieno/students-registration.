
from django.shortcuts import render, redirect
from .models import Stream, Student

def stream_list(request):
    streams = Stream.objects.all()
    return render(request, 'streams.html', {'streams': streams})

def stream_detail(request, pk):
    stream = Stream.objects.get(pk=pk)
    students = Student.objects.filter(stream=stream)
    return render(request, 'stream_detail.html', {'stream': stream, 'students': students})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        admission_number = request.POST['admission_number']
        stream_pk = request.POST['stream']
        stream = Stream.objects.get(pk=stream_pk)
        student = Student(first_name=first_name, last_name=last_name, admission_number= admission_number,stream=stream)
        student.save()
        return redirect('student_list')
    streams = Stream.objects.all()
    return render(request, 'student_create.html', {'streams': streams})

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.admission_number = request.POST['admission_number']
        stream_pk = request.POST['stream']
        stream = Stream.objects.get(pk=stream_pk)
        student.stream = stream
        student.save()
        return redirect('student_list')
    streams = Stream.objects.all()
    return render(request, 'student_update.html', {'student': student, 'streams': streams})

def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('student_list')

def create_stream(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Stream.objects.create(name=name)
        return redirect('list_streams')
    return render(request, 'create_stream.html')

def delete_stream(request, stream_id):
    Stream.objects.get(id=stream_id).delete()
    return redirect('list_streams')    
