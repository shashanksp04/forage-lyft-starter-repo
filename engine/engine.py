from abc import ABC

class Engine(ABC):
    
    def __init__(self):
        pass 

    def need_service(self) -> bool:
        pass