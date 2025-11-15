#multiple inheritance
class A:
  def fun1(self):
    print("day1")
class B:
  def fun2(self):
    print("day2")
class C(A,B):
  pass
obj=A()
obj2=B()
obj.fun1()
obj2.fun2()
