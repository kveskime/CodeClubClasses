# What is an Interface?

"""
Interfaces make it possible to say:
    Hey, this thing has these methods, I don't know how it is implemented, but it is there!
"""


class IRunnable:
    """Interface for things that are Runnable - they have the run() method!"""

    def run(self):
        raise NotImplementedError  # The thing that implements IRunnable has to implement run itself.

"""
class IRunnable:                    ->  class MyClass(IRunnable):

    def run(self):                  ->      def run(self):
        raise NotImplementedError   ->          ... # Lots of implementation code here!
"""

# How to make an Interface


class ISomething:
    """
    In python one way to make an Interface is just a class with a bunch of methods that raise NotImplementedError.
    """

    def x(self):
        raise NotImplementedError

    def y(self):
        raise NotImplementedError


# How to implement an Interface


class Something(ISomething):
    def y(self):  # Same signature, will overwrite the previous def y(self) so raise NotImplementedError is not called
        return "Wut?"

    def x(self):
        return "Wat?"


# STATIC METHOD SIDE NOTE


class ClassWithStaticMethod:
    def method(self):
        """Just a regular method.."""
        pass

    @staticmethod  # This marks this method as "Does not use self!"
    def a_static_method():  # Look Ma! No self!
        """This method is static!

        Use static methods when you don't need self. (You don't refer to instance variables)

        A real example is a calculation method like:

        def add(self, x, y):
            return x + y  # Umm... I'm not using self, so why even pass it in...

        Do this:

        @staticmethod
        def add(x, y):
            return x + y

        Differences in using static vs. non static method:

        class A:

            def m1(self):
                return 1

            @staticmethod
            def m2():
                return 2

        You can do this:

        a = A()
        a.m1()
        a.m2()

        You can't do this:

        A.m1()  # Because m1 is tied to an instance (need to call a = A() first, so self would exist!)

        But you can do this:

        A.m2()  # Because it is static and not tied to an instance! (self does not need to exist!)

        """
        pass
