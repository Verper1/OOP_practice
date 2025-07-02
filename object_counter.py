class ObjectCounter:
    count = 0

    def __init__(self):
        ObjectCounter.count += 1

    @staticmethod
    def display_counter():
        print(f"Количество объектов класса: {ObjectCounter.count}")


o1 = ObjectCounter()
o1.display_counter()
o2 = ObjectCounter()
o2.display_counter()
