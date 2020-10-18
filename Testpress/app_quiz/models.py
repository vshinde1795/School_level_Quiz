from django.db import models

class Quiz(models.Model):
    # quiz_id = models.IntegerField(primary_key=True,auto_created=True)
    quiz_name = models.CharField(max_length=100)


class Question(models.Model):
    question = models.TextField(max_length=200)
    quiz_id = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    # question_id = models.IntegerField(primary_key=True,auto_created=True)

    option_a = models.TextField(max_length=50)
    option_b = models.TextField(max_length=50)
    option_c = models.TextField(max_length=50)
    option_d = models.TextField(max_length=50)

    correct_ans = models.CharField(max_length=4)



