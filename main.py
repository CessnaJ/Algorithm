def solution(participant, completion):
    deleted = []
    for i in participant:
        if i in completion:
            participant.remove(i)

    return participant[0]


a = ["leo", "kiki", "eden"]
b = ["eden", "kiki"]
# "leo"
c = ["marina", "josipa", "nikola", "vinko", "filipa"]
d = ["josipa", "filipa", "marina", "nikola"]
#"vinko"
x = ["mislav", "stanko", "mislav", "ana"]
y = ["stanko", "ana", "mislav"]
# "mislav"
print(solution(x,y))