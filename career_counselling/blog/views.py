import gensim as gn
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from .forms import ExamForm1
def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def test(request):
    if request.method=='POST':
        form = ExamForm1(request.POST)
        if form.is_valid():
            arr=[]
            field=[]
            field.append(form.data['agriculture'])
            field.append(form.data['photography'])
            field.append(form.data['hotel_management'])
            field.append(form.data['gaming'])
            field.append(form.data['commerce'])
            field.append(form.data['business_management'])
            field.append(form.data['biology'])
            field.append(form.data['animation'])
            field.append(form.data['computer_engineering'])
            field.append(form.data['journalism'])
            courses={}
            courses[0]="agriculture"
            courses[1]="photography"
            courses[2]="hotel_management"
            courses[3]="gaming"
            courses[4]="commerce"
            courses[5]="business_management"
            courses[6]="biology"
            courses[7]="animation"
            courses[8]="computer_engineering"
            courses[9]="journalism"

            degrees={0:{"Diploma in Agriculture","Diploma in Agriculture Engineering","Diploma in Organic Agriculture"}}
            degrees[1]={"Diploma in Photography"}
            degrees[2]={"Diploma in Hotel Management","Diploma in Food & Beverage Production","Diploma in Front Office Operations"}
            degrees[3]={"Diploma in Game designing","Diploma in Graphic designing"}
            degrees[4]={"Commerce(CEC)","Commerce(MEC)","eCommerce","Diploma in Accounting "}
            degrees[5]={"Diploma in Business Adminstration"}
            degrees[6]={"Biology(BPC)","Diploma in Pharmacy","Diploma in Dental Mechanics"}
            degrees[7]={"Diploma in Animation","Diploma in 3D animation","Diploma in animation,art and design"}
            degrees[8]={"Science(MPC)","Diploma in Computer Programming","Diploma in Information Technology"}
            degrees[9]={"Diploma in Journalism and Mass Communication","Diploma in Development Journalism","Diploma in Mass Media Communication"}
            # lis=open("C:/Users/Magesh/Desktop/career_counselling/blog/static/inference/agriculture.txt", encoding="UTF-8",errors="ignore").replace(",","").split()
            with open("C:/Users/Magesh/Desktop/career_counselling/blog/static/inference/agriculture.txt", "r", encoding="UTF-8") as f:
                stri=f.read()
            lis=stri.replace(",","").split('\n')
            li=[i.split() for i in lis]
            maxScore=0
            course=0
            for i in range(10):
                p=summarize(field[i], ratio=0.9)
                lis2=set(list(set(p.split())))
                result=len(set(li[i]).intersection(lis2))
                if( maxScore < result):
                    maxScore=result
                    course=i
                src="/media/output/"+"img"+str(course)+".jpg"
            return render(request,'blog/output.html',{'arr':courses[course],'src':src,'degrees':degrees[course]})
    else:
        form = ExamForm1()
    return render(request,'blog/test.html',{'form':form})
