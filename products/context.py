def rental_months(request):
    months = request.session.get('months', 1)

    context = {
        'months': months,
    }
    return context
