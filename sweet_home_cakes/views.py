from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, redirect


def handler404(request, *args, **argv):
    return render(request, '404.html')


def handler500(request, *args, **argv):
    return render(request, '404.html')