from main import *
import math


def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(10, 3, 2, lambda n: n) == 70
  assert work_calc(22, 3, 2, lambda n: 2 * n) == 389
  assert work_calc(30, 3, 5, lambda n: n) == 57
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(10, 2, 2, lambda n: n) == 36
  assert work_calc(10, 2, 2, lambda n: int(math.log(n, 2))) == 19


def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work

  # create work_fn1
  # create work_fn2
  def work_fn1(n):
    return work_calc(n, 16, 2, lambda n: n**3)

  def work_fn2(n):
    return work_calc(n, 1, 2, lambda n: n**3)
                     
  res = compare_work(work_fn1, work_fn2)
  print(res)


def test_compare_span():
  def span_fn1(n):
    return span_calc(n,2,2,lambda n: 1)
  def span_fn2(n):
    return span_calc(n,2,2,lambda n: n)
  def span_fn3(n):
    return span_calc(n,2,2,lambda n: int(math.log(n, 2)))
  
  res = compare_span(span_fn1, span_fn2, span_fn3)
  print(res)

def test_time_compare_span():
  def span_fn1(n):
    return time_span_calc(n,2,2,lambda n: 1)
  def span_fn2(n):
    return time_span_calc(n,2,2,lambda n: n)
  def span_fn3(n):
    return time_span_calc(n,2,2,lambda n: int(math.log(n, 2)))

  res = compare_span(span_fn1, span_fn2, span_fn3)
  print(res)

