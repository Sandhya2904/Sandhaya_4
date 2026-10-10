class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine_obj = Engine() 
    def driving(self):
        self.engine_obj.start()
        print("Car is driving")
obj = Car()
obj.driving()
