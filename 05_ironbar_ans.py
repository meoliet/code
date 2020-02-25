def solution(arrangement):
    answer=0
    stack=[]
    arrangement = list(arrangement.replace('()','L'))

    for num in range(len(arrangement)):
        if arrangement[num]=='(':
            stack.append('(')
            answer+=1
        elif arrangement[num]==')':
            stack.pop()
        else:
            answer+=len(stack)

    return answer

arrangement='()(((()())(())()))(())'
print(solution(arrangement))