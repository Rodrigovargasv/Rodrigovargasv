#!/usr/bin/python
# -*- coding: utf-8 -*-


class Calculadora:

    def __init__(self, *args):
        pass

    def calcular(self, *args):
        while True:
            args = list(args)
            args.append(eval(input('Digite a operação:\n')))
            for x in args:
                print (f'RESULTADO: {x}')
            print ('--------------------------------')
            args.append(eval(input('Digite os valores a ser calculado:\n')))
            print (f'RESULTADO: {sum(args)}')
            contin = str(input('[0] SAIR [1]CONTINUAR : '))
            if contin == '=':
                print (f'RESULTADO: {sum(args)}')
            if contin == '0':
                print (f'RESULTADO: {sum(args)}')
                break

c = Calculadora()
c.calcular()
