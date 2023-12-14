'''

INTRODUCTION:

Properties in Python are attributes that are controlled by methods. We've already seen how to use the property() 
function to define getter and setter methods that control how object attributes are accessed and modified.

A decorator is a function that takes another function as an argument and returns a new function, often attaching 
pre- or post-processing functionality. The decorator syntax was not available when the property() function was 
originally introduced. However, the decorator syntax was added in Python 2.4, and using property() as a decorator 
has become a popular practice.

Reviewing property()
Before we see how to use a decorator to define a property, let's review the original property() function.

We'll start with a Dog class with attributes for name and breed.

name must be a string of 1 to 25 characters in length
breed must be a string in the list of approved breeds
We define getter and setter methods for the attributes, then use the property function to enforce that the 
methods are used to access and mutate the attributes:


Function Decorators
We decorate a function by placing the name of the decorator with a leading @ symbol before the definition of the 
function you want to decorate:

@decorator
def func(a):
    return a
This syntax is equivalent to the following:

def func(a):
    return a



Using property() as a Decorator:
We use the @property decorator to define a property's getter method. The method should use the public name for the underlying managed attribute, for example name.

Delete the get_name method:

def get_name(self):
        return self._name
 

Add the name getter method decorated with @property as shown:

@property
def name(self):
    """The name property"""
    return self._name

Delete the set_name method:
def set_name(self, name):
    if isinstance(name, str) and 1 <= len(name) <= 25:
        self._name = name.title()
    else:
        raise ValueError(
            "Name must be string between 1 and 25 characters.")

Add the name setter method decorated with @name.setter as shown:

@name.setter
def name(self, name):
    """Name must be a string between 1 and 25 characters in length"""
    if isinstance(name, str) and 1 <= len(name) <= 25:
        self._name = name
    else:
        raise ValueError("Name must be string between 1 and 25 characters." )
Finally, you can delete the call to the property function as the decorators have defined the getter and setter methods:

name = property(get_name, set_name)

'''