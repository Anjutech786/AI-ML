from abc import ABC, abstractmethod

class MathBase(ABC):
    def __init__(self,num1,num2):#define properties
        self._num1=num1
        self._num2=num2
    @abstractmethod
    def add(self):
        pass

class MyMaths(MathBase):
    pass
    @property
    def num2(self):
        return self._num2
    @property
    def num1(self):
        return self._num1    
    # setter method for num1 and num2 to validate the values before assigning them to the properties
    @num1.setter   
    def num1(self,value):
        if value<0:
            raise ValueError("num1 should be non-negative")
        self._num1=value
    #@num2.setter  
    @num2.setter
    def num2(self,value):
        if value<0:
            raise ValueError("num2 should be non-negative")
        self._num2=value
  
    def add(self):
        return self._num1 + self._num2
class AdvancedMaths(MyMaths):
    def log(self):
        print(str(self._num1)+"this is log method")