from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _move(self):
        pass

    @abstractmethod
    def observe(self):
        pass

    @abstractmethod
    def activity(self):
        '''Функция определяет активность сущности, исходя из результатов действия функции observe.'''
        pass
    
    @abstractmethod
    def _check_walls(self):
        pass

    def _change_condition(self):
        '''Функция реализует смену состояний сущности (Entity) при соответствующих условиях.'''
        pass
