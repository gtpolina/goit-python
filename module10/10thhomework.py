from collections import UserDict


class Field:
    
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return self.value


class Name(Field):
    
    pass


class Phone(Field):
    
    pass


class Record:
    
    def __init__(self, name, *args):
        
        self.name = name
        self.phones = []
        for item in args:
            if isinstance(item, Phone):
                self.phones.append(item)             

    def delete_phone(self, phone_arg):
        
        for item in self.phones:
            if phone_arg == item.value:
                a = self.phones.remove(item)                
                return a
            
        print(f'No such phone number {phone_arg} in record {self.name}')
                
    def add_phone(self, phone_arg):
        self.phones.append(Phone(phone_arg))
        
    def change_phone(self,phone_arg, replace_phone_arg):
        count = 0
        for i in range(len(self.phones)):
            if phone_arg == self.phones[i].value:
                self.phones[i] = Phone(replace_phone_arg)
                count += 1
        if count == 0:
            print(f'No such phone {phone_arg} in a record')
            
                
                 
        #self.phones = [item if item.value != phone_arg else Phone(replace_phone_arg) for item in self.phones]
            
        
        

    def __str__(self):
        res = f"{self.name}  {', '.join([str(phone) for phone in self.phones])}"
        return res
    


class AddressBook(UserDict):
    
    def add_record(self, obj):

        if isinstance(obj, Record):
            self.data[obj.name.value] = obj
            return self.data
        
    def delete_record(self,obj):
        if isinstance(obj, Record):
            del self.data[obj.name.value]
            return self.data
    

    def __str__(self):
        return "\n".join([f"{str(v)}" for k, v in self.data.items()])


if __name__ == "__main__":
    adress_book = AddressBook()
    record_1 = Record(Name("Vasya"), Phone("23456777"), Phone("1235468762"))   
    adress_book.add_record(record_1)  
                                    
    record_2 = Record(Name("Kolia"), Phone("23456777"), Phone("1235468762"))    
    adress_book.add_record(record_2)
    
    print(adress_book)
    print('------')
    
    adress_book.delete_record(record_1)
    print(adress_book)
    print('------')
    
    record_2.delete_phone("23456777")
    print(adress_book)
    print('------')

    record_2.add_phone('12345456')
    print(adress_book)
    print('------')

    record_2.change_phone('1234545','11111111')
    print(adress_book)
    print('------')
    
    
    

    

    

    
    
    
  
    
