def gradeall(scores):
    jieguo={'优秀':0,'良好':0,'及格':0,'不及格':0}

    for i in scores:
        if i>=90:
            jieguo['优秀'] += 1
        elif i>=80:
            jieguo['良好'] += 1
        elif i>=60:
            jieguo['及格'] += 1
        else:
            jieguo['不及格'] += 1

    return jieguo
print(gradeall([1,1,22,44,77,88,55,99]))
