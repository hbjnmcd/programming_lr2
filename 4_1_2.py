def two_sum_hashed(lst, target):
  seen = {}
  for i, num in enumerate(lst):
    complement = target - num
    if complement in seen:
      return (seen[complement], i)
    seen[num] = i
  return None


if __name__ == "__main__":
  lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  target = 6
  result = two_sum_hashed(lst, target)
  print(result)
