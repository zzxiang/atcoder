n = int(input())
a = list(map(int, input().split()))

m = max(a)

cnt = [0] * (m + 1)
for a_i in a:
	cnt[a_i] += 1

total_cnt = 0

for a_j in range(1, m + 1):
	for a_k in range(m // a_j + 1):
		a_i = a_j * a_k
		total_cnt += cnt[a_i] * cnt[a_j] * cnt[a_k]

print(total_cnt)