class cifrado_cesar:
    def __init__(self, password):
        self.__password = password
 
    def getPassword(self):
        return self.__password
    
    def cifrado(self):
        
        abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        pass_cifrada = ""
        list_p = list()
        p = str(self.__password)
        var_temp = 0
        for i in p:
            list_p.append(i.lower())
        
        print(abecedario)
        print(list_p)
        
        for letra in range(len(list_p)):
            for letra_abecedario in range(len(abecedario)):
             if list_p[letra] == abecedario[letra_abecedario]:
                  var_temp = (letra_abecedario + 2) % 27
                  pass_cifrada = pass_cifrada + abecedario[var_temp]
        print(pass_cifrada)
        
           
p = cifrado_cesar('myPassword')    
p.cifrado()        
p2 = cifrado_cesar('otracontraseña')
p2.cifrado()