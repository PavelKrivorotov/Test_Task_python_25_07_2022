Вопрос 1. Реализация алгоритма определения чётности числа:

  def is_even(value):
      return not int(bin(value)[-1])
      
  is_iven(-12) -> True
  is_iven(119) -> False
    
  Функция преобразует число (предполагается что оно изначально в десятичной системе) в двоичную,
  а дальше мы преобразуем последний символ числа, приведённого к двоичной форме в целое чило. То
  есть либо 0 либо 1. При этом если там 0, то чисо чётное, а если 1, то нечётное.

Вопрос 2. Реализовать очередь FIFO.

  class MyElem():
    def __init__(self, val):
        self.next = None
        self.val = val

  class MyQueue():
    def __init__(self, val):
        elem = MyElem(val)
        self.root = elem
        self.end = elem

    def add_elem(self, val):
        elem = MyElem(val)
        self.end.next = elem
        self.end = elem

    def get_elem(self):
        try:
            val = self.root.val
            self.root = self.root.next
        except AttributeError:
            return None
        return val


  a = MyQueue(10)
  a.add_elem(9)
  
  print(a.get_elem()) -> 10
  print(a.get_elem()) -> 9
  print(a.get_elem()) -> None
  
  Для решения задачи были прописаны два класса MyElem как абстракция элемента в очереди и MyQueue
  как абстракция очереди. При этом MyQueue имеет два метода add_elem для добавления элемента в
  очередь и get_elem для извлечения элемента из очереди.

Вопрос 3. Реализовать самую быструю сортировку.

  def my_sort(array):
    return sorted(array)
    
  my_sort([234, -98, 74, 1]) -> [-98, 1, 74, 234]
  
  Нужно признать что вопрос обсурдный и самой быстрой сортировки не сущствует. У каждой есть лучшее,
  худшее и среднее время выполения. Но если набор данных относитально рандомный (случайный), то 
  встроенная сортировка в python -> TimeSort справится с задачей сортировкуи куда лучше любого велосипеда.
  
