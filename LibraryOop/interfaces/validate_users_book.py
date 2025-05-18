from abc import ABC, abstractmethod

class ValidateUsersBook(ABC):
    @abstractmethod
    def _validate_to_remove(self):...
    
    @abstractmethod
    def _validate_to_add(self):...
    
    @abstractmethod
    def _validate_to_show(self):...
    
