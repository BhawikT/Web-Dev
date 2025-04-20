from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def reviews(request):
    reviews = Review.objects.all().order_by('-created_at')  # Get all reviews ordered by creation date
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new review
            return redirect('reviews')  # Redirect to the same page to show updated reviews
    else:
        form = ReviewForm()

    return render(request, 'reviews.html', {'reviews': reviews, 'form': form})
