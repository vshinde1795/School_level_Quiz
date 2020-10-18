from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import pyautogui as pu
import time
from .models import Quiz, Question
from datetime import date


def home(request):
    return render(request, 'home.html')



def student_login(request):
    all_quiz = Quiz.objects.all()
    return render(request, 'all_quiz.html', {'all_quiz': all_quiz})

def signup_page(request):
    return render(request,'signup.html')

def login_page(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            pu.alert("Username already exist")
        else:
            x = User.objects.create_user(username=username,first_name=first_name, last_name=last_name, email=email,
                                         password=password)
            x.save()
            pu.confirm("user created")
            return redirect('/')
    return render(request, 'signup.html')


all_question = []
visited = 0
score = 0
options = []
initial_time = 0

def start(request, quiz_id):
    global ques_id, visited, all_question, initial_time, score
    visited = 0
    score = 0
    initial_time = time.time()
    all_question = Question.objects.filter(quiz_id=quiz_id)
    question = all_question[visited]
    return render(request, 'quiz_start.html', {'question': question, 'enabled': True})



score11 = []
def next(request):
    global visited, all_question, score, options, score11, initial_time

    if request.method == 'POST':
        options = request.POST.getlist('options')
        options1 = ','.join(str(i) for i in score11)
        action = request.POST.get('action')
        if action == 'Next':
            previous = all_question[visited]
            correct_answer = getattr(previous, 'correct_ans')
            print("correct:", correct_answer)
            print("anss:", options1)
            if correct_answer == options1:
                score += 1
            visited += 1
            if len(all_question) > visited:
                question = all_question[visited]
                context = {
                    'question': question,
                    'enabled': True
                }
                return render(request, 'quiz_start.html', context)
            else:
                end_time = time.time()
                total_time = end_time - initial_time
                total_time = str(("%.3f" % total_time) + " " + "sec")
                temp = 1
                visited = 0
                return render(request, 'quiz_start.html', {'temp': temp, 'score': score, 'total_time': total_time})
        else:

            option_a = False
            option_b = False
            option_c = False
            option_d = False
            score11 = options
            for i in options:
                if i == 'a':
                    option_a = True
                elif i == 'b':
                    option_b = True
                elif i == 'c':
                    option_c = True
                elif i == 'd':
                    option_d = True
            question = all_question[visited]
            context = {
                'question': question,
                'enabled': False,
                'option_a': option_a,
                'option_b': option_b,
                'option_c': option_c,
                'option_d': option_d
            }
            return render(request, 'quiz_start.html', context)


def create(request):
    return render(request, 'create_quiz.html')


def save_quiz(request):
    if request.method == 'POST':
        quiz_name = request.POST['quiz_name']
        qz = Quiz(quiz_name=quiz_name)
        qz.save()
        for i in range(1, 11, 1):
            question = request.POST['ques_' + str(i)]
            option_a = request.POST['option_' + str(i) + '_a']
            option_b = request.POST['option_' + str(i) + '_b']
            option_c = request.POST['option_' + str(i) + '_c']
            option_d = request.POST['option_' + str(i) + '_d']
            correct_ans = request.POST['correct_ans_' + str(i)]
            q_obj=Question.objects.create(question=question,quiz_id=qz,option_a=option_a,option_b=option_b,option_c=option_c,option_d=option_d,correct_ans=correct_ans)
            q_obj.save()
        return render(request,'create_quiz.html')