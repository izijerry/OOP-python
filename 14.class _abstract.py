from abc import ABC,abstractmethod
class button(ABC):
    @abstractmethod
    def click(self):
       pass

class push_button(button):
    def click(self):
        print("hello world")

class button_name(button):
    def click(self):
        print("nama saya udin")

tombol1 = push_button()
tombol2 = button_name()

tombol2.click()
tombol1.click()