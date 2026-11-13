from django.shortcuts import render


def home(request):

    fruits = ['banana', 'laranja', 'morango', 'uva']

    return render(
        request,
        'home.html',
        {
            'name': 'Joca da Silva',
            'age': 24,
            'tel': '(21) 998877665',
            'fruits': fruits
        }
    )
