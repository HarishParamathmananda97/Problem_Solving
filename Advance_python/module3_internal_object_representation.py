"""
Internal Object Representation

The __dict__ dictionary
Manipulating __dict__
Faking attributes with
> __getattr__()
> __getattribute__()
> __setattr__()
> __delattr__()
> Save space with __slots__

"""
#example 1:
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self.x, self.y)
    

obj_v = Vector(5, 3)

print(dir(obj_v))

print(obj_v.__dict__) # dictionary
print(obj_v.__dict__['x'], obj_v.__dict__['y'])

obj_v.__dict__['x'] = 17
print(obj_v.x)

del obj_v.__dict__['x']

obj_v.__dict__['z'] = 23
print('x' in obj_v.__dict__)
print('y' in obj_v.__dict__)
print('z' in obj_v.__dict__)

getattr(obj_v, 'y')

hasattr(obj_v, 'x')

delattr(obj_v, 'z')

setattr(obj_v, 'x', 11)

print(obj_v.__dict__)

#example 2

class Vector:
    def __init__(self, **coords):
        private_coords = {'_'+k : v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __repr__(self):
        return "{} ({})".format(
            self.__class__.__name__, 
            ', '.join("{k} = {v}".format(
                k = k[1:], 
                v = self.__dict__[k])
                for k in sorted(self.__dict__.keys())))
    
v = Vector(p = 3, q = 7)
print(v)
print(dir(v))

# overriding using __getattr__()

"""
Fallback __getattr__()
Invoked after requested attribute/ property not found by normal lookup


Preemptive __getattribute__()
Invoked instead of normal lookup
"""
#example 3
class Vector:
    def __init__(self, **coords):
        private_coords = {'_' + k:v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    # recursion error if name is not exists to avoid this we use __hasattr__()

    # def __getattr__(self, name):
    #     # print("name =", name)
    #     private_name = '_' + name
    #     if private_name not in self.__dict__:
    #         raise AttributeError('{!r} object has no attribute {!r}'.format(self.__class__, name))
    #     return getattr(self, private_name)    
    def __getattr__(self, name):
        private_name = '_' + name
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError('{!r}object has no attribute {!r}'.format(self.__class__, name))
    
    # to avoid creation of new variable into the class, we override this use __setattr__()
    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

    #to override the deletion of assigned property
    def __delattr__(self, name: str) -> None:
        raise AttributeError("Can't delete attribute {!r}".format(name))

    def __repr__(self):
        return "{} ({})".format(
            self.__class__.__name__, ', '.join("{k} = {v}".format(
                k = k[1:],
                v = self.__dict__[k])
                for k in sorted(self.__dict__.keys())))
    
v = Vector(p=5, q=8)
print(v)


# Overriding __delattr__()

# 28th will be continued.

