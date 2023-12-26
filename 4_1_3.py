def two_sum_hashed_all(lst, target):
  seen = {}
  result = []
  for i in range(len(lst)):
    complement = target - lst[i]
    if complement in seen:
      result.append((seen[complement], i))
    seen[lst[i]] = i
  return result


if __name__ == "__main__":
  lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  target = 6
  result = two_sum_hashed_all(lst, target)
  print(result)
