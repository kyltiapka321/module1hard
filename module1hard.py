grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
x = grades[0]
x1 = len(x)
x = sum(x)
x2 = x/x1
y = grades[1]
y1 = len(y)
y = sum(y)
y2 = y/y1
z = grades[2]
z1 = len(z)
z = sum(z)
z2 = z/z1
q = grades[3]
q1 = len(q)
q = sum(q)
q2 = q/q1
w = grades[4]
w1 = len(w)
w = sum(w)
w2 = w/w1
grades[0] = x2
grades[1] =y2
grades[2] =z2
grades[3] =q2
grades[4] =w2
print(grades)
itog = {students[0] : grades[0], students[1] : grades[1], students[2] : grades[2], students[3] : grades[3], students[4] : grades[4]}
print(itog)