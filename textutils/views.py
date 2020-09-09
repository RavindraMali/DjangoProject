from django.http import  HttpResponse
from django.shortcuts import render
def index(request):
        #param={'name':'ravindra mali','age':22}
        #return HttpResponse("hello ravindra bhai")
        #return  render(request,'index.html',param)
        return render(request,'index.html')
def about(request):
        return render(request,'about.html')
def check(request):
        djtext=request.GET.get('text','default')
        rp_check=request.GET.get('rp_checkbox','off')
        cpt_checkbox=request.GET.get('cpt_checkbox','off')
        nl_checkbox = request.GET.get('nl_checkbox', 'off')
        extra_space=request.GET.get('extra_space','off')
        print(djtext)
        print(rp_check)
        print(cpt_checkbox)
        if rp_check=="on":
                analyzed = ""
                punc = ''',.\/'";:[]{}()!@#$%^&*~`-_=+|<>?"'''
                for char in djtext:
                        if char not in punc:
                                analyzed = analyzed + char
                param={ 'purpose':'Remove Punchuations','analyzed_test': analyzed }
                return render(request,'check.html',param)
        elif (cpt_checkbox=="on"):
                analyzed = ""
                for char in djtext:
                        analyzed = analyzed + char.upper()
                param = {'purpose': 'Capitalize', 'analyzed_test': analyzed}
                return render(request, 'check.html', param)
        elif (nl_checkbox == "on"):
                analyzed = ""
                for char in djtext:
                        if char!='\n':
                                analyzed = analyzed + char
                param = {'purpose': 'Remove NewLine', 'analyzed_test': analyzed}
                return render(request, 'check.html', param)
        elif (extra_space == "on"):
                analyzed = ""
                for index,char in enumerate(djtext):
                        if not(djtext[index]==" " and djtext[index+1]== " ") :
                                analyzed = analyzed + char
                param = {'purpose': 'Remove NewLine', 'analyzed_test': analyzed}
                return render(request, 'check.html', param)
        else:
                param = {'purpose': 'Remove Punchuations', 'analyzed_test': djtext}
                return render(request, 'check.html', param)
def nevigation(request):
        return render(request,'nevigation.html')