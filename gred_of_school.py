score = input('Please enter your score : ')
score = int(score)
if score >= 80 and score <= 100 :
    print('score = ',score,' Grad is A')
elif score >= 70 and score <= 79 :
    print('score = ',score,' Grad is B')
elif score >= 60 and score <= 69 :
    print('score = ',score,' Grad is C')
elif score >= 50 and score <= 59 :
    print('score = ',score,' Grad is D')
elif score >= 00 and score <= 49 :
    print('score = ',score,' Grad is F')

else:
    print('score error')

