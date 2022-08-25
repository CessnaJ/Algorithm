T = int(input())

for case in range(1, T+1):
    target, storage = input().split()
    trimmed_target = target.replace(storage, '@')
    print(f'#{case} {len(trimmed_target)}')