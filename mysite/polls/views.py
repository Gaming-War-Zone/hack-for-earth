from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import SoilCondition


def index(request):
    if request.method == 'POST':
        print(request.POST.get('my_field'))
        print(request.method)
        """
        print(form['my_field'].value())
        print(form.data['my_field'])
        if form.is_valid():
            print(form.cleaned_data['my_field'])
            print(form.instance.my_field)
            form.save()
            print(form.instance.id)  # now this one can access id/pk
        """
    ideal_readings = SoilCondition.objects
    context = {'Ideal_readings': ideal_readings}
    return render(request, 'polls/index.html', context)
# Create your views here.


def results(request):
    if request.POST:
        form_data = request.POST.dict()
        mydata = SoilCondition.objects.all().values()[0]
        readings = {}
        results = {}
        shortages = {}
        for data in form_data:
            if data =='potassium reading':
                readings['K']=form_data.get(data)
            if data =='phosphorus reading':
                readings['P'] = form_data.get(data)
            if data =='nitrogen reading':
                readings['N'] = form_data.get(data)
            if data == 'acres':
                readings['acres'] = form_data.get('acres')
        nitrogen_calc = int(mydata['I_N']) * 0.9 <= int(readings['N']) <= int(mydata['I_N'])
        potassium_calc = int(mydata['I_K']) * 0.9 <= int(readings['K']) <= int(mydata['I_K'])
        phosphorus_calc = int(mydata['I_P']) * 0.9 <= int(readings['P']) <= int(mydata['I_P'])
        if nitrogen_calc:
            results['Nitrogen'] = "Your nitrogen levels are good, no need for additional nitrogen"
        if not nitrogen_calc:
            if int(readings['N']) < 0.9*int(mydata['I_N']):
                shortages['Nitrogen'] = {'shortage':round(abs(int(readings['N']) - int(mydata['I_N']))), 'percentage':round((1-(int(readings['N'])/int(mydata['I_N'])))*100), 'required':abs(int(readings['N']) - int(mydata['I_N']))*2*int(readings['acres'])}

        if potassium_calc:
            results['Potassium'] = "Your potassium levels are good, no need for additional nitrogen"
        if not potassium_calc:
            if int(readings['K']) < 0.9*int(mydata['I_K']):
                shortages['Potassium'] = {'shortage':round(abs(int(readings['K']) - int(mydata['I_K']))), 'percentage':round((1-(int(readings['K'])/int(mydata['I_K'])))*100), 'required':abs(int(readings['K']) - int(mydata['I_K']))*1.2046*int(readings['acres'])}

        if phosphorus_calc:
            results['Phosphorus'] = "Your phosphorus levels are good, no need for additional nitrogen"
        if not phosphorus_calc:
            if int(readings['P']) < 0.9*int(mydata['I_P']):
                shortages['Phosphorus'] = {'shortage':round(abs(int(readings['P']) - int(mydata['I_P']))), 'percentage':round((1-(int(readings['P'])/int(mydata['I_P'])))*100), 'required':abs(int(readings['P']) - int(mydata['I_P']))*2.2913*int(readings['acres'])}
        context = {'results':results, 'shortages':shortages}
        print(results)
        print(shortages)
    else:
        context = {}


    return render(request, 'polls/detail.html', context)



def vote(request):
    context = {}
    return render(request, 'polls/shop.html', context)
