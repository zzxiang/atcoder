# https://atcoder.jp/contests/typical90/tasks/typical90_b
# https://atcoder.jp/contests/typical90/submissions/31643695

n = int(input())

if n % 2 == 0:
	s = list('(' * (n // 2) + ')' * (n // 2))

	i = n // 2 - 1  # s[i]：チェックしている括弧
	right_cnt = n // 2  # i以降の位置に右括弧の数
	left_cnt = 1  # i以降の位置に左括弧の数

	# 左括弧を一つずつ一ポジションずつ右へ移動する
	while True:
		print(''.join(s))
		# s[i]は必ず'('
		if right_cnt > 1:
			s[i], s[i+1] = ')', '('
			i += 1
			right_cnt -= 1
		else:
			while i > 0 and (left_cnt >= right_cnt or s[i] == ')'):
				i -= 1
				if s[i] == '(':
					left_cnt += 1
				else:
					right_cnt += 1
			if i > 0:
				s[i] = ')'
				i += 1
				right_cnt -= 1
				for j in range(i, i + left_cnt):
					s[j] = '('
				i += left_cnt - 1
				left_cnt = 1
				for j in range(i + 1, n):
					s[j] = ')'
			else:
				break
