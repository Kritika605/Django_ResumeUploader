from django.shortcuts import redirect,render
from .forms import ResumeForm
from .models import Resume
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self,request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        context = {
            'form':form,
            'candidates':candidates
        }
        return render(request ,'index.html',context)

    def post(self,request):
        form = ResumeForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print("eroor...........................")
            context = {
            'form':form
            }
            return render(request ,'index.html',context)
        
    
class CandidateView(View):
    def get(self,request,pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request , 'candidate.html',{'candidate':candidate})
