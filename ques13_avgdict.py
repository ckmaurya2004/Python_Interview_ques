student_data = {
    'kiran':{'details':{'roll':101,'marks':[20,60,30,50,50]}},
    'shikha':{'details':{'roll':101,'marks':[20,63,30,55,50]}}, 
    'ruchi':{'details':{'roll':101,'marks':[21,60,30,10,50]}},
    'priya':{'details':{'roll':101,'marks':[24,60,20,50,50]}},
    'kajal':{'details':{'roll':101,'marks':[20,60,34,50,50]}}
}

for key in student_data:
    print(sum(student_data[key]['details']['marks'])/len(student_data[key]['details']['marks']))