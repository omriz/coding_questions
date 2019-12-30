def knows(a,b):
    pass
def IdentifyCelebrity(people):
    celeb = 0
    if len(people) == 0:
        return None
    if len(people) == 1:
        return 1
    for i in range(1,len(people)):
        if knows(people[i],people[celeb]):
            celeb = i
    print(people[celeb])
        
