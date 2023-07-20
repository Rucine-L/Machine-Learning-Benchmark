class Factory:
    All_cla_elements={
        "id":1,
        "keys":[[],[0.2,0.3,3,5,10],[],[0.01,0.05,0.1],[],[]]
    }
    All_reg_elements={
        "id":1,
        "keys":[[],[0.2,0.3,3,5,10],[],[0.01,0.05,0.1],[],[]]
    }
    configuration=[]
    type=0

    def __init__(self) -> None:
        pass
       
    def c_register(self,index,value):
        self.All_cla_elements['keys'][index].append(value)
    def r_register(self,index,value):
        self.All_reg_elements['keys'][index].append(value)

    def c_inspect(self):
        return self.All_cla_elements
    def r_inspect(self):
        return self.All_reg_elements
    
    def set_configuration(self,message):
        self.configuration=message

    def set_type(self,type):
        self.type=type