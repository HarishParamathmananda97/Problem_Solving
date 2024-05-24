"""
In short, Descriptors are the mechanism behind Properties.
Lets see, > Properties without decorators.
          > Custom descriptors.
          |-> Data Descriptors.
          |-> Non-Data Descriptors. 
          > Attribute lookups.
"""

class Planet:
    def __init__(self, name, raidus_metres, mass_kilograms, orbital_period_seconds, surface_temperature_kelvin):
        self.name = name
        self.raidus_meters = raidus_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin


pluto = Planet(name = 'Pluto', raidus_metres=1184e3, mass_kilograms=1.305e22, orbital_period_seconds=7816012992, surface_temperature_kelvin=55)

# using decorators, we set value and also validate the data before assigning it into the class attribute.
class Planet:
    def __init__(self, name, raidus_metres, mass_kilograms, orbital_period_seconds, surface_temperature_kelvin):
        self.name = name
        self.raidus_meters = raidus_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty planet name")
        self._name = value

    @property
    def radius_metres(self):
        return self._radius_metres
    @radius_metres.setter
    def radius_metres(self, value):
        if value <= 0:
            raise ValueError("radius_metres value {} is not positive".format(value))
        self._radius_metres = value
    
    @property
    def mass_kilograms(self):
        return self._mass_kilograms
    @mass_kilograms.setter
    def mass_kilograms(self, value):
        if value <= 0:
            raise ValueError("mass_kilograms value {} is not positive".format(value))
        self._mass_kilograms = value

    @property
    def orbital_period_seconds(self):
        return self._orbital_period_seconds
    @orbital_period_seconds.setter
    def orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError("orbital_period_seconds value {} is not positive".format(value))
        self._orbital_period_seconds = value

    @property
    def surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin
    @surface_temperature_kelvin.setter
    def surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError("Surface_Temperature_Kelvin value {} is not positive".format(value))
        self._surface_temperature_kelvin = value
    

pluto = Planet(name = 'Pluto', raidus_metres=1184e3, mass_kilograms=1.305e22, orbital_period_seconds=7816012992, surface_temperature_kelvin=55)

# instead of using decorators, we use property() which do the same trick.

class Planet:
    def __init__(self, name, raidus_metres, mass_kilograms, orbital_period_seconds, surface_temperature_kelvin):
        self.name = name
        self.raidus_meters = raidus_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin
    
    def _get_name(self):
        return self._name
    def _set_name(self, value):
        if not value:
            raise ValueError("Cannot set empty planet name")
        self._name = value
    name = property(fget=_get_name, fset=_set_name)

    def _get_radius_metres(self):
        return self._radius_metres
    def _set_radius_metres(self, value):
        if value <= 0:
            raise ValueError("radius_metres value {} is not positive".format(value))
        self._radius_metres = value
    radius_meters = property(fget=_get_radius_metres, fset=_set_radius_metres)

    def _get_mass_kilograms(self):
        return self._mass_kilograms
    def _set_mass_kilograms(self, value):
        if value <= 0:
            raise ValueError("mass_kilograms value {} is not positive".format(value))
        self._mass_kilograms = value
    mass_kilograms = property(fget=_get_mass_kilograms, fset=_set_mass_kilograms)
    
    def _get_orbital_period_seconds(self):
        return self._orbital_period_seconds
    def _set_orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError("orbital_period_seconds value {} is not positive".format(value))
        self._orbital_period_seconds = value
    orbital_period_seconds = property(fget=_get_orbital_period_seconds, fset=_set_orbital_period_seconds)
    
    def _get_surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin
    def _set_surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError("Surface_Temperature_Kelvin value {} is not positive".format(value))
        self._surface_temperature_kelvin = value
    surface_temperature_kelvin = property(fget=_get_surface_temperature_kelvin, fset=_set_surface_temperature_kelvin)
    

pluto = Planet(name = 'Pluto', raidus_metres=1184e3, mass_kilograms=1.305e22, orbital_period_seconds=7816012992, surface_temperature_kelvin=55)

print(pluto.mass_kilograms)



"""
After the validation is set, we can now cant assign negative value to the class attribute directly, 
pluto.surface_temperature_kelvin = -143 
will trigger Value Error 
but, if you use the private variable for assigning it will over ride the real variable's value as well.
eg: pluto._surface_temperature_kelvin = -143
print(pluto.surface_temperature_kelvin)# -143

#to solve this if we delte this _variables then it wont assign neg value to the class attributes.
"""
