import mpmath
import os
from scipy import constants as constant 
from scipy.constants import physical_constants as physical_constant
import quantiphy

def main():
    os.system('clear')
    Exercicio_1()
    Exercicio_2()

def Exercicio_1():
    print("1) a) " + probability(0.1, 300))
    print("1) b) " + probability(0.1, 600))


def Exercicio_2():
    Resposta_E2a = E2a(T=300)
    Resposta_E2b = E2b(T=600)
    print("2) a) \n\tGe: " + Resposta_E2a[0] + "\n\tGaAs: " + Resposta_E2a[1] )
    print("2) b) \n\tGe: " + Resposta_E2b[0] + "\n\tGaAs: " + Resposta_E2b[1] )
    
def E2a(T):
    
    #Ge
    Nc = 1.03e19
    Nv = 5.35e18
    Eg = 0.66
    E = Eg/2 + 0.1
    Ei = intrinsic_energy_level(Eg, T, Nc, Nv)
    Ef = Ei #For intrinsic Semiconductors 
    P = probability(E - Ef, T) 
    Ge = P

    #GeAs
    Nc = 4.21e17
    Nv = 9.52e18
    Eg = 1.42
    E = Eg/2 + 0.1
    Ei = intrinsic_energy_level(Eg, T, Nc, Nv)  
    Ef = Ei #For intrinsic Semiconductors 
    P = probability(E - Ef, T)
    GaAs = P
    return [Ge, GaAs]


def E2b(T):
    return E2a(T)

def E2c():
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
