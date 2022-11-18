from django.shortcuts import render

from plotlyTest1.models import CO2
import plotly.express as px
from plotlyTest1.forms import DateFrom

# Create your views here.
def chart(request):
    co2 = CO2.objects.all()
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start:
        co2 = co2.filter(date__gte=start)
    if end:
        co2 = co2.filter(date__lte=end)

    fig = px.line(
        x = [c.date for c in co2],
        y = [c.average for c in co2],
        title = "CO2 ppm",
        labels = {'x': 'Date', 'y': 'ppm'}
    )
    fig.update_layout(title={
        'font_size': 22,
        'xanchor':  'center',
        'x': 0.5
 
    })

    chart = fig.to_html()

    context = {'chart': chart, 'form': DateFrom()}
    return render(request, 'core/chart.html', context)