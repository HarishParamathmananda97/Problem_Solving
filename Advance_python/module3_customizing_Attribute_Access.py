"""
FallBack -> __getattr__()
Invoked after requested attribute/ property not found by normal lookup

Preemptive -> __getattribute__()
Invoked instead of normal lookup

"""

import day3_customizing_attribute_storage as vector

class LoggingProxy:
    def __init__(self, target):
        super().__setattr__('target', target)

    def __getattribute__(self, name):
        target = super().__getattribute__('target')
    
        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name, target))from e
        print("Retrieved attribute {!r} = {!r} from {!r}".format(name, value, target))
        return value
    def __setattr__(self, name, value):
        target = super().__getattribute__('target')
        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,name, target)) from e
        print("Set attribute {!r} = {!r} on {!r}".format(name, value, target))
    
    def __repr__(self):
        target = super().__getattribute__('target')
        repr_callable = getattr(target, '__repr__')
        return repr_callable()

# cv = vector.ColoredVector(red = 23, green = 44, blue = 238, p=9, q = 14)
"""
Attribute Lookup for Special Methods Example
"""
cv = vector.ColoredVector(red = 39, green = 22, blue = 89, s = 45, t = 12)
cw = LoggingProxy(cv)
print(cw.s)

