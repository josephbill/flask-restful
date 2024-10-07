class A:
    def __init__(self,name) -> None:
        self.name = name
        
    # methods 
    @classmethod
    def greetuser(cls):
        return f"Hello {cls.name}"