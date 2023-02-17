def main():
    file1=input('filename (correct answers):')
    correct_answer=write_file_correct(file1)
    print('The correct answers are:', correct_answer)
    file2=input('filename (student answers):')
    student_answer=write_file_student(file2)
    print('Your answers are:', student_answer)
    correct, wrong=comparison(correct_answer, student_answer)
    print('You got', correct, 'correct answers')
    print('You got', wrong, 'wrong answers')
    pass_fail(correct)


def write_file_correct(name):
    correct_list=[]
    infile=open(name,'r')
    for letter in infile:
        correct_list+=[letter.strip()]
    return correct_list

def write_file_student(name):
    answer_list=[]
    infile=open(name,'r')
    for letter in infile:
        answer_list+=[letter.strip()]
    return answer_list

def comparison(list1, list2):
    i=0
    j=0
    total=0
    incorrect=0
    while i< len(list1) and j< len(list2):
        if list1[i]==list2[j]:
            total+=1
        else:
            incorrect+=1
        i+=1
        j+=1
    return total, incorrect

def pass_fail(total):
    if total>=15:
        print('You passed the test. CONGRATULATION!!')
    else:
        print('You failed the test. Best of luck next time!')

main()
