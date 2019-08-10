class NumberType:
    def __init__(self):
        self.set_target_name(self.__class__.__name__, id(self))

    def set_target_name(self, cls_name, key):
        self.target_name = f'{cls_name}__{key}'

    def __get__(self, instance, owner):
        return getattr(instance, self.target_name)

    def __set__(self, instance, value):
        if value > 0.0:
            setattr(instance, self.target_name, value)
        else:
            raise ValueError('Value should be bigger than 0')

    def __str__(self):
        return self.__class__.__name__


class MetaModel(type):
    def __init__(cls, name, bases, dictionary):
        super(MetaModel, cls).__init__(name, bases, dictionary)
        for key, attr in dictionary.items():
            if hasattr(attr, 'set_target_name'):
                attr.set_target_name(attr, key)


class Model(metaclass=MetaModel):
    pass
