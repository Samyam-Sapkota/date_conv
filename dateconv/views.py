from django.shortcuts import render,get_object_or_404,redirect
from dcapp import dateconv,models


def return_latest_pk():
    last_instance=models.datecapp.objects.latest('id')
    return last_instance.pk

def home(request):
   return render(request,'index.html')

# def post_data(request):
#      html_date=request.POST['date1']
#      html_fields=request.POST['ad2bs']
#      print(f'this is from above 1 {html_fields}')
     

#    #   if (html_field == "222"):
#    #      print(html_field)
#      models.datecapp.objects.create(date=html_date)
#      ltpk=return_latest_pk()
#      full_date=models.datecapp.objects.get(pk=ltpk)
#      dyear=full_date.date.year
#      dmonth=full_date.date.month
#      dday=full_date.date.day
#      nepali_bs_data=dateconv.ad_to_bs(dyear,dmonth,dday)
     
#      context={'nepali_bs_data':nepali_bs_data,'dyear':dyear,'dmonth':dmonth,'dday':dday}
#      full_date.delete()
#      return render(request,'result.html',context) 







def post_data(request):
     html_date=request.POST['date1']
   #   html_field=request.POST['bs2ad']
     if 'bs2ad' in request.POST:
         html_field=request.POST['bs2ad']
     else:
         html_field=False
       
     if (html_field =="bstoad"):
        models.datecapp.objects.create(date=html_date)
        ltpk=return_latest_pk()
        full_date=models.datecapp.objects.get(pk=ltpk)
        dyear=full_date.date.year
        dmonth=full_date.date.month
        dday=full_date.date.day
        conv_data=dateconv.bs_to_ad(dyear,dmonth,dday)
        d_from ="BS"
        d_to='AD'
        context={'conv_data':conv_data,'dyear':dyear,'dmonth':dmonth,'dday':dday,'d_from':d_from,'d_to':d_to}
        full_date.delete()
        return render(request,'result.html',context)
     else:
        models.datecapp.objects.create(date=html_date)
        ltpk=return_latest_pk()
        full_date=models.datecapp.objects.get(pk=ltpk)
        dyear=full_date.date.year
        dmonth=full_date.date.month
        dday=full_date.date.day
        conv_data=dateconv.ad_to_bs(dyear,dmonth,dday)
        d_from ="AD"
        d_to='BS'
        context={'conv_data':conv_data,'dyear':dyear,'dmonth':dmonth,'dday':dday,'d_from':d_from,'d_to':d_to}
        full_date.delete()
        return render(request,'result.html',context) 