from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "core/index.html")


def index(request):
    expenses = Expense.objects.all()
    sum = 0
    count = 0
    for expense in expenses:
        sum += expense.amount
        count += 1
    context = {
        'miqdori': sum,
        'soni': count,
        'expenses': expenses
    }
    return render(request, 'core/index.html', context)

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Xarajat muvaffaqiyatli qoshildi')
            return redirect('index')
        else:
            expenses = Expense.objects.all()
            miqdori = sum([expense.amount for expense in expenses])
            soni = expenses.count()
            context = {
                'jami_miqdori': miqdori,
                'jami_soni': soni,
                'expenses': expenses,
                'form': form
            }
            return render(request, 'core/index.html', context)
    return redirect('index')
def delete_expense(request, expense_id):

    if request.method == 'POST':
        expense = Expense.objects.get(id=expense_id)
        expense.delete()
        messages.success(request, "Xarajat muvaffaqiyatli ochirildi.")
    return redirect('index')