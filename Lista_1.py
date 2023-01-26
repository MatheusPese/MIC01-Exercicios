import mpmath
import os
from scipy import constants as constant 
from scipy.constants import physical_constants as physical_constant
import quantiphy

class element:
    def __init__(self, name, T, Eg, Nc, Nv):
        self.name = name
        self.T = T
        self.Eg = Eg
        self.Nc = Nc
        self.Nv = Nv

    def probability(self, foo, unit='eV'):
        #foo: E - Ef
        k = physical_constant["Boltzmann constant in eV/K"][0]
        result = 1/(mpmath.exp(foo/(k*self.T))+1)
        result = quantiphy.Quantity(result,'eV',scale=unit)
        return result.render(form='fixed', prec=6)

Ge300K = element("Ge", 300, 0.66, 1.03e19, 5.35e18)
GaAs300K = element("GeAs", T=300, Eg=1.42, Nc=4.21e17, Nv=9.52e18)        

def main():
    os.system('clear')
    print(Ge300K.probability(0.1))
    Exercicio_1()
    Exercicio_2()

def Exercicio_1():
    print("1) a) " + Ge300K.probability(0.1))
    print("1) b) " + probability(0.1, 600))


def Exercicio_2():
    Resposta_E2a = E2a(T=300)
    Resposta_E2b = E2b(T=600)
    print("2) a) \n\tGe: " + Resposta_E2a[0] + "\n\tGaAs: " + Resposta_E2a[1] )
    print("2) b) \n\tGe: " + Resposta_E2b[0] + "\n\tGaAs: " + Resposta_E2b[1] )
    
def E2a(T):
    
    #Ge at 300K
    Nc = Ge300K.Nc 
    Nv = Ge300K.Nv
    Eg = Ge300K.Eg
    E = Eg/2 + 0.1
    Ei = intrinsic_energy_level(Eg, T, Nc, Nv)
    Ef = Ei #For intrinsic Semiconductors 
    P = probability(E - Ef, T) 
    Ge = P

    #GeAs at 300K
    Nc = GaAs300K.Nc 
    Nv = GaAs300K.Nv 
    Eg = GaAs300K.Eg
    E = Eg/2 + 0.1
    Ei = intrinsic_energy_level(Eg, T, Nc, Nv)  
    Ef = Ei #For intrinsic Semiconductors 
    P = probability(E - Ef, T)
    GaAs = P
    return [Ge, GaAs]


def E2b(T):
    return ["#TODO: CALCULATE Eg, Nc, and Nv at 600K",""]

def E2c():
    #Ge
    
    intrinsic_concentration(Nc, Nv, Eg, T)
    pass

def probability(Eg,T=0, unit='eV'):
    k = physical_constant["Boltzmann constant in eV/K"][0]
    result = 1/(mpmath.exp(Eg/(k*T))+1)
    result = quantiphy.Quantity(result,'eV',scale=unit)
    return result.render(form='fixed', prec=6)

def intrinsic_energy_level(Eg, T, Nc, Nv):
    k = physical_constant["Boltzmann constant"][0]
    Ei = (Eg/2) - ((k*T)/2) * mpmath.ln(Nc/Nv)
    return Ei

def intrinsic_concentration(Nc, Nv, Eg, T):
    k = physical_constant["Boltzmann constant"][0]
    ni = 2*(Nc*Nv)^(1/2)*exp(-Eg/(2*k*T))
    return ni

main()
