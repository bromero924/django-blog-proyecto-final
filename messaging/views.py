from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm


@login_required
def inbox_view(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messaging/inbox.html', {'messages': messages})


@login_required
def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()

    return render(request, 'messaging/send_message.html', {'form': form})


@login_required
def message_detail_view(request, pk):
    message = get_object_or_404(Message, pk=pk, receiver=request.user)
    return render(request, 'messaging/message_detail.html', {'message': message})


