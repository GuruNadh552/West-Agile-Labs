def solution(input_from_question):
    noh,btc = map(int,input_from_question.split())
    if(noh%2!=0):
        return ((noh//2)+1)*btc
    return (noh//2)*btc
  
 print(solution(input_from_question)) 
