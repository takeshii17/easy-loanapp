from django.shortcuts import render


def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


def dashboard_view(request):
    return render(request, "dashboard.html")


def apply_loan_view(request):
    return render(request, "apply_loan.html")


def my_loans_view(request):
    return render(request, "my_loans.html")
