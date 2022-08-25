# end = int(input())
# depth = '----'
#
# def recursive_function(start, end):
#
#     if start == end:
#
#         print(f'{depth * start}재귀함수가 뭔가요?')
#         print(f'{depth * start}"재귀함수는 자기 자신을 호출하는 함수라네."')
#     else:
#         print(f'{depth * start}재귀함수가 뭔가요?')
#         print(f'{depth * start}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print(f'{depth * start}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print(f'{depth * start}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         start += 1
#         recursive_function(start, end)
#         print(f'{depth * start}라고 답변하였지.')
#
#
#
#
#
# print('''어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.''')
# recursive_function(0, end)
# print('라고 답변하였지.')

n = 0
def function(k):
    global n
    print(n*"____" + f'\"재귀함수가 뭔가요?\"\n' +
          n*"____" + f'\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n' +
          n*"____" + f'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n' +
          n*"____" + f'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"')
    n += 1
    function(k-n)
    print(n * "____" + "라고 답변하였지.")
    if A != n:
        function(A-n)
        # print(n * "____" + "라고 답변하였지.")



A = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
function(A)
