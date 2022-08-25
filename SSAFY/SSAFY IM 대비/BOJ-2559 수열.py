N, K = map(int, input().split())

given_temperature_list = list(map(int, input().split())) # 계산 수를 줄이기 위해서 sliding 사용.
temp_result = sum(given_temperature_list[0:K]) # 첫 idx부터 K-1까지 K개의 개체를 더함.
max_result = temp_result + 0
for i in range(N-K):
    temp_result = temp_result - given_temperature_list[i] + given_temperature_list[i + K] # 한칸씩 컨베이어벨트처럼 밀려나니까 앞 계산치의 첫 idx 빼주고 뒤 idx 1개 더 더해준거 더함.
    if temp_result > max_result: #직전 sum 값이랑 비교. 내장함수대신 이런식으로 1번만 더하니까 계산 빠름.
        max_result = temp_result

print(max_result)