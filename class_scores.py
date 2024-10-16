import random

students = ['Serena','Jake','Joe','Jeremy','Kyle','Sarah','Sadie','Emily',
            'Nora','Claire','Lily','Ella','Ben','Michael','Gabby','Lauren',
            'Sam','Natalie','Edward','Amy','Rachel','Jasmine','Clarissa',
            'Addison','Izzy','Cecelia','Payton','Noah','Nyomi','Regan','Sean',
            'Charlie','Megan','Evelyn','Brooke','Sophia','Callie','Hadley']
scores = random.sample([i for i in range(50,101)], len(students))
random.shuffle(students)
random.shuffle(scores)
test_scores = {}
for i in range(0, len(students)):
    test_scores[students[i]] = {'score':scores[i]}

def a(score):
    global grade
    grade = 'A'
    return score >= 90
def b(score):
    global grade
    grade = 'B'
    return 90 > score >= 80
def c(score):
    global grade
    grade = 'C'
    return 80 > score >= 70
def d(score):
    global grade
    grade = 'D'
    return 70 > score >= 60
def f(score):
    global grade
    grade = 'F'
    return 60 > score >= 50 or score < 50

filters = lambda function: list(filter(function, scores))
alist = filters(a)
blist = filters(b)
clist = filters(c)
dlist = filters(d)
flist = filters(f)

def grad(a_list, a_grade):
    for i in test_scores:
    	if test_scores[i]['score'] in a_list:
    		test_scores[i]['grade'] = a_grade
    return test_scores

l = [alist,blist,clist,dlist,flist]
list(map(grad, l, ('A','B','C','D','F')))

a_students = [i for i in test_scores if test_scores[i]['grade'] == 'A']
b_students = [i for i in test_scores if test_scores[i]['grade'] == 'B']
c_students = [i for i in test_scores if test_scores[i]['grade'] == 'C']
d_students = [i for i in test_scores if test_scores[i]['grade'] == 'D']
f_students = [i for i in test_scores if test_scores[i]['grade'] == 'F']

scores.sort()
scores.reverse()
score_ranks = []
for i in scores:
    for el in students:
        if test_scores[el]['score'] == i:
    	    score_ranks.append(el)

best_score = max(scores)
worst_score = min(scores)
l = []
for i in score_ranks:
    k = i + ': ' + str(test_scores[i]['score']) + ', ' + str(test_scores[i]['grade'])
    l.append(k)
for i in test_scores:
    if test_scores[i]['score'] == best_score:
        best_person = i
        best_grade = test_scores[i]['grade']
    if test_scores[i]['score'] == worst_score:
        worst_person = i
        worst_grade = test_scores[i]['grade']
apercent = round((len(a_students)/len(test_scores)) * 100, 2)
bpercent = round(len(b_students)/len(test_scores) * 100, 2)
cpercent = round(len(c_students)/len(test_scores) * 100, 2)
dpercent = round(len(d_students)/len(test_scores) * 100, 2)
fpercent = round(len(f_students)/len(test_scores) * 100, 2)
average_score = round(sum(scores)/len(scores), 2)
for i in a,b,c,d,f:
	if i(average_score) is True:
		average_grade = grade

for i, el in enumerate(l, 1):
    print(' %d. %s' % (i, el))
print('\nThe best grade in the class is', best_person + ', with a score of',best_score,'and a grade of', best_grade)
print('The worst grade in the class is', worst_person + ', with a score of',worst_score,'and a grade of',worst_grade)
print('Serena had a score of',test_scores['Serena']['score'],'and a grade of', test_scores['Serena']['grade'],'\n')
print(apercent,'% of students, or',len(a_students),'students, had a grade of A')
print(bpercent,'% of students, or',len(b_students),'students, had a grade of B')
print(cpercent,'% of students, or',len(c_students),'students, had a grade of C')
print(dpercent,'% of students, or',len(d_students),'students, had a grade of D')
print(fpercent,'% of students, or',len(f_students),'students, had a grade of F')
print("\nThe average score of the class is", str(average_score) + ', '+ "or a grade of",average_grade)
