def two_sum(lst, target):
  '''
  Функция принимает на вход список чисел и число и возвращает индексы тех двух чисел 
  списка, которые в сумме дают данное.
  Функция состоит из двух циклов, что дает сложность O(n^2).
  
  lst(list) - список чисел.
  target(int) - число, используемое в качестве сравнения для суммы элементов списка.
  '''
  for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
      if lst[i] + lst[j] == target:
        return ((i, j))


if __name__ == "__main__":
  lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  target = 8
  result = two_sum(lst, target)
  print(result)
