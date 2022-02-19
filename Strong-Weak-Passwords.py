def check_pass(st):
    l = len(st)
    c = 0
    for i in range(l-2):
        if(st[i].isalpha() and st[i+1].isalpha() and st[i+2].isalpha()):
            c=1
        if(st[i].isdigit() and st[i+1].isdigit() and st[i+2].isdigit()):
            c=1
    return True if c==0 else False

def solution(input_from_question):
    l = []
    for i in range(input_from_question):
        l.append(check_pass(input()))
    if False in l:
        return 'Weak'
    return 'Strong'
  
