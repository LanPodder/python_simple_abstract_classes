# python_simple_abstract_classes
showcasing abstract classes (interface like classes in this case) in python

----------
# How this works

IMotor (probably not python namingconvention comform) here represents a Motor interface.
It uses pythons "abc" (short for "Abstract Base Class") module which allows us to do a couple of things.

By inheriting from the abc.ABC class we are able to define methods as abc.abstractmethods by using the @abc.abstractmethod annotation.
This way, if another class inherits from IMotor, 
an error will be thrown if it does not implement all abstract methods (similar to how a interface behaves in java)

Within Car we can now pass a IMotor (well, any object really because we dont declare the type of anything)
into the __init__ constructor and call motors methods within the drive method.

What happens here is while running the code, python will try to run the code no matter what
and as soon as we call the "drive" method from our main, it will try to run the motor methods. 
If we happen to pass a "non-motor" what ends up happening is, we recieve a runtime error inside the drive method.

Because we dont compile anything in python before we run the code, we cant really force Car to only take IMotor objects in its constructor.
However, with IMotor we can at the very least force ourselfs to implement those motor methods by using the above method.

