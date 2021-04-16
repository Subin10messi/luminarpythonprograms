class Pycharm():
    def open(self):
        print("open method in pycharm")
    def debug(self):
        print("debug funclty in pycharm")
    def run(self):
        print("run functly in pycharm")

class JupyterNb():
    def open(self):
        print("open method in Jupyternb")
    def debug(self):
        print("debug funclty in Jupyternb")
    def run(self):
        print("run functly in Jupyternb")


class Programmer :
    def coding(self,ide):
        ide.open()
        ide.debug()
        ide.run()

py=Pycharm()
jp=JupyterNb()
p=Programmer()
p.coding(py)

#Duck typing is a concept related to dynamic typing, where the type or the class of an object is
# less important than the methods it defines. When you use duck typing, you do not check types at all.
# Instead, you check for the presence of a given method or attribute.


