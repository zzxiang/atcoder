n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

def score_can_be(min_cut_len):
  cut_cnt = 0
  last_cut_point = 0
  for a_i in a:
    if a_i - last_cut_point >= min_cut_len:
      last_cut_point = a_i
      cut_cnt += 1
    if cut_cnt >= k:
      return l - a_i >= min_cut_len
  return False

low = 0
high = l
max_score = 0

while low <= high:
  mid = low + (high - low) // 2
  #print(low, mid, high)
  if score_can_be(mid):
    low = mid + 1
    max_score = mid
  else:
    high = mid - 1

print(max_score)