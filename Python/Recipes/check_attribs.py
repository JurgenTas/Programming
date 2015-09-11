__author__ = 'J Tas'

# =====================================================================
# Places checks or assertions on the settings of certain
# instance attributes. See: 'Python Cookbook' (8.13).


class Descriptor:
    """
    Uses a descriptor to set a value
    """

    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def check_attributes(**kwargs):
    """
    Class decorator to apply constraints.
    """

    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate()

# =====================================================================

