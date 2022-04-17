from collections import UserDict
from datetime import datetime
import pickle
import re
from copy import copy



class Field:
    
    def __init__(self, value):
        self._value = None
        self.value = value

    def __str__(self) -> str:
        return self._value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,value):
        self._value = value

    
class Name(Field):
    
    pass


class Phone(Field):
    
    @Field.value.setter
    def value(self, value):
        
        matched_phone = re.findall(r'^\+?\d+$',value)

        if matched_phone and len(value) <= 15:
            self._value = value
        else:
            print("Phone has to be no more then 15 digits and include or not '+' in the beginning")


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        try:
            b_day = datetime.strptime(value, "%d/%m/%y").date()
            self._value = b_day

        except ValueError:
            print("Wrong birthday format, has to be dd/mm/yy ")



class Record:
    
    def __init__(self, name, *args):
        
        self.name = name
        self.phones = []
        self.birthday = ''       
        for item in args:
            if isinstance(item, Phone):
                self.phones.append(item)
            if isinstance(item, Birthday):
                self.birthday = item
                              
            
                
                
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
            
    def days_to_birthday(self):
        if not self.birthday:
            return 'No birthday in this record'
        
        
        today = datetime.today()
                
        if (today.month == self.birthday.value.month and today.day >= self.birthday.value.day or today.month > self.birthday.value.month):
            next_birthday_year = today.year +  1
        else:
            next_birthday_year = today.year
            
        next_birthday = datetime(next_birthday_year,self.birthday.value.month,self.birthday.value.day)
        difference = next_birthday - today
        return  difference.days        
                 
        #self.phones = [item if item.value != phone_arg else Phone(replace_phone_arg) for item in self.phones]
            
        
        

    def __str__(self):
        if isinstance(self.birthday,Birthday):
            birthday_str = self.birthday.value.strftime("%d/%m/%y")
            res = f"{self.name}  {', '.join([str(phone) for phone in self.phones])}, {birthday_str}"
        else:
            res = f"{self.name}  {', '.join([str(phone) for phone in self.phones])}"
            
        return res
    


class AddressBook(UserDict):

    printed_records = 0
    records_to_print = 0
    
    def add_record(self, obj):

        if isinstance(obj, Record):
            self.data[obj.name.value] = obj
            return self.data
        
    def delete_record(self,obj):
        if isinstance(obj, Record):
            del self.data[obj.name.value]
            return self.data
        
    def __next__(self):

        if len(self.data.items()) > self.printed_records:
            
            printed_chunk = list(self.data.items())[self.printed_records:self.printed_records + self.rows_to_print]
            printed_chunk_str  = "\n".join([str(value) for key,value in printed_chunk])
            self.printed_records = self.printed_records + self.rows_to_print

            return printed_chunk_str
        else:
            print("No more records to show")
            raise StopIteration
        
    def __iter__(self):
         return self

    def iterator_2(self, quantity):
        self.rows_to_print = quantity

        for record in self:
            print(record)
            return record   
        
    def iterator(self, rows_number=2):
        end = len(self.data)
        i = 0
        limit = rows_number
        while True:
            yield "\n".join([f"{str(item)}" for key,item in list(self.data.items())[i:limit]])
            print("next page")
            i, limit = i + rows_number, limit + rows_number
            if i >= end:
                break  

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value

    def save_to_file(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self, file_name):
        with open(file_name, "rb") as file:
            return pickle.load(file)

    def search(self, text):
        #result = []
        for field in self.data.values():
            if text in field.name.value or [ph for ph in field.phones if text in ph.value]:
                print(f'{field}----serch result from----{text}')
                
        return '-----End of search------'

    def __str__(self):
        return "\n".join([f"{str(v)}" for k, v in self.data.items()])


if __name__ == "__main__":
    adress_book = AddressBook()
    record_1 = Record(Name("Vasya"), Phone("2346678"), Phone("1235468762"))   
    adress_book.add_record(record_1)  
                                    
    record_2 = Record(Name("Kolia"), Birthday('15/04/88'), Phone("23456777"), Phone("1235468762"))    
    adress_book.add_record(record_2)

    record_3 = Record(Name("Liolia"), Phone("23456780967"), Phone("12368762"),Birthday('17/08/89'))
    adress_book.add_record(record_3)

    record_4 = Record(Name("Tolia"), Phone("23876880967"), Phone("12368762"),Birthday('17/04/89'))
    adress_book.add_record(record_4)

    record_5 = Record(Name("Petia"), Phone("+5860880967"), Phone("12368762"))
    adress_book.add_record(record_5)

    

    print('-----All records in adressbook-----')
    
    print(adress_book)
    
    print('-----Adressbook after deleting record_1----')
    
    adress_book.delete_record(record_1)
    print(adress_book)
    
    print('------Adressbook after deleting phone in record_2----')
    
    record_2.delete_phone("23456777")
    print(adress_book)
    
    print('------Adressbook after adding phone in record_2----')

    record_2.add_phone('12345456')
    print(adress_book)
    
    print('------Adressbook after changing phone number in record_2----')

    record_2.change_phone('1234545','11111111')
    print(adress_book)
    
    print('------Days to birthday method test-------')

    print(record_1.days_to_birthday())
    print(record_2.days_to_birthday())
    print(record_3.days_to_birthday())
    print(record_5.days_to_birthday())
    
     

    print('\n------Iteration test 2------')

    adress_book.iterator_2(2)
    print('------')
    adress_book.iterator_2(1)
    print('------')
    adress_book.iterator_2(2)
  
  

    '''print('\n------Repr of adress_book------')

    print(repr(adress_book))'''

    print('\n------Iteration test------')

    for record in adress_book.iterator(1):
        print(record)

    print('\n-------Save/Open test-------------------')

    adress_book.save_to_file("test.bin")
    adress_book = adress_book.read_from_file("test.bin")
    print(adress_book)

    print('\n-----------Search test---------------')    

    print(adress_book.search("Liolia"))
    print(adress_book.search("lia"))
    print(adress_book.search("88"))
    print(adress_book.search("586"))
      


      

   
 
        

   
    
    
    
    

    

    

    
    
    
  
    
