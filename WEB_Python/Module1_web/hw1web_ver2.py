from abc import abstractmethod,ABCMeta
import pickle
import json

class SerializationInterface(metaclass=ABCMeta):

    def __init__(self,data):
        self.data = data
        

    
    @abstractmethod
    def save_to_file(self):
        pass
  


class SerializationJson(SerializationInterface):
      


    def save_to_file(self):
        serialize_file = "json_file.json"
        with open(serialize_file,"w") as file:
            json.dump(self.data
                      ,file)


class SerializationBin(SerializationInterface):


    def save_to_file(self):
        serialize_file = "bin_file.bin"
        with open(serialize_file,"wb") as file:
            pickle.dump(self.data,file)

    def read_from_file(self):
        serialize_file = "bin_file.bin"
        with open(serialize_file,"rb") as file:
            data_from_file = pickle.load(file)
        return data_from_file  



class Meta(type):
    
    children_number = 0

    def __new__(*args,**kwargs):
        print(args,'\n')
        return type.__new__(*args)

    def __init__(*args,**kwargs):
        Meta.children_number +=1




class Cls1(metaclass=Meta):
    
    class_number = Meta.children_number

    def __init__(self,data):
        self.data = data



class Cls2(metaclass=Meta):
    
    class_number = Meta.children_number

    def __init__(self,data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)

a, b = Cls1(''), Cls2('')

assert (a.class_number, b.class_number) == (0, 1)  

