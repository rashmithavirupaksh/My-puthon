#inheritance
class parent:
  def function(self):
    print("good")
class child(parent):
  def function(self):
    print("bad")
obj=child()
obj.function()
