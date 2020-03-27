class Calculadora:
    def __init__(self, *args):
        pass
        #args = list(args)
        #self.nomeclasse = self.__class__.__name__
        
class Cal (Calculadora):
    
    def calcular (self, *args):
        args = list(args)
        print('calculadora de expresão')
        while True:

            args.append(eval(input('Digite os valores a ser calculado:\n')))
            
           
            for x in args:
                print(f"resultado = {x}")
                print("-----------------------------------------------------")
                args.append(eval(input('Digite os valores a ser calculado: ')))
                print(sum(args))
                contin = str(input('Digite  [0] para sair : '))
                if contin == '=':
                    print(sum(args))
                if contin == '0':
                    print(f'RESULTADO DA OPERAÇAO: {sum(args)}')
                    break
                
            break     
            
a1 = Calculadora()
a1 = Cal()
a1.calcular()

