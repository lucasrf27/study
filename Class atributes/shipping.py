class ShippingContainer:
    
    serial_number = 1337

    @classmethod
    def get_serial_number(cls):
        result = cls.serial_number
        cls.serial_number += 1
        return result


    def __init__(self, owner_code, content):
        self.owner_code= owner_code
        self.content = content
        self.serial = self.get_serial_number()


