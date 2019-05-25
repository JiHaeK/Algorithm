def solution(n, s="", count=0):
    if n == 0: 
        if count == 0: 
            return [s]
        return solution(n, s+")", count-1) 

    if count == 0:
        return solution(n-1, s+"(", count+1)

    return solution(n-1, s+"(", count+1) + solution(n, s+")", count-1)