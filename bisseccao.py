"""
Implementação do Método da Bissecção
Autor: Bruno Ribeiro
Universidade Federal da Fronteira Sul - UFFS
Curso de Ciência da Computação
CCR: Cálculo Numérico
Professor: Paulo Boesing
Março/2018
"""
from math import *

# limite de iteracoes quando o algoritmo não especifica
N_MAX = 1000

def erro_relativo(x_atual, x_anterior):
    """
    Calcula o erro relativo entre as iterações da bissecção

    Args:
        x_atual (float): valor de x na iteração atual
        x_anterior (float): valor de x na iteração anterior

    Returns:
        float: Valor do erro relativo calculado
    """
    return abs(x_atual - x_anterior)/abs(x_atual)


def funcao(x, funcao_str):
    """
    Função a qual a bisseção será aplicada.

    Args:
        x (float): literal 'x' a qual a função é aplicada
        funcao_str (str): a string que representa a funcao, deve seguir a sintaxe do Python 3
    """
    try:
        resultado = eval(funcao_str)
    except:
        raise ValueError("A sintaxe da função informada não está correta!")
    
    return resultado


def iteracoes(a, b, precisao):
    """
    Define o número de iterações necessárias para encontrar a raiz ou aproximação

    Args:
        a (float): limite inferior do intervalo
        b (float): limite superior do intervalo
        precisao (float): precisão estabelecida

    Returns:
        int: Teto sob o número de iterações calculado
    """
    num_iter = (log10(b-a) - log10(precisao)) / log10(2)
    return ceil(num_iter)


def sinal(x):
    """
    Retorna o número 1 com o sinal de x
    """
    return copysign(1, x)


def bisseccao(funcao_str, a, b, precisao):
    """
    Realiza a bissecção tentando encontrar a raiz aproximada de uma função

    Args:
        funcao_str (string): string da função na sintaxe python 3
        a (float): limite inferior do intervalo
        b (float): limite superior do intervalo
        precisao (float): precisão estabelecida
    """
    i, x_anterior, erro_rel = 1, 0, precisao
    num_iteracoes = iteracoes(a, b, precisao)
    print("A precisão {} exige {} iterações da bissecção.".format(precisao, num_iteracoes))

    # condições de parada: n. de iterações e erro relativo < precisão
    while i < num_iteracoes+1 and erro_rel >= precisao:
        x = a + ((b - a)/2)
        erro_rel = erro_relativo(x, x_anterior)
        x_anterior = x
        print("a%d ="%i, a, "b%d ="%i, b, "x%d ="%i, x, "Erro rel.: {}".format(erro_rel))
        f_a, f_b, f_x = funcao(a, funcao_str), funcao(b, funcao_str), funcao(x, funcao_str)
            
        if sinal(f_a)*sinal(f_b) < 0:
            # talvez um dos termos aplicados à função já seja uma raiz
            if f_a == 0:
                print("a%d ="%i, a, "f(a%d) ="%i, f_a)
                return
            elif f_b == 0:
                print("b%d ="%i, b, "f(b%d) ="%i, f_b)
                return
            elif f_x == 0:
                print("x%d ="%i, x, "f(x%d) ="%i, f_x)
                return

            # redistribui os limites
            if sinal(f_a)*sinal(f_x) < 0:
                b = x
            else:
                a = x

            # incrementa iterações
            i += 1
        else:
            print("A execução terminou sem encontrar quaisquer raízes.")
            return

    print("Execução da bissecção concluída!")
    print("Uma das raízes possíveis da função '{}' está no intervalo [a,b] = [{}, {}].".format(funcao_str, a, b))


def newton(funcao_str, derivada_str, p0, precisao, N=N_MAX):
    """
    Busca uma raiz aproximada de uma função através do método de Newton

    Args:
        funcao_str (string): string da função na sintaxe python 3
        derivada_str (string): string da derivada da função anterior na sintaxe python 3
        p0 (float): chute inicial
        precisao (float): precisão estabelecida
    """
    i, p_anterior, erro_rel = 1, p0, precisao

    # condições de parada: n. de iterações e erro relativo < precisão
    while erro_rel >= precisao:
        if i < N+1:
            p = p_anterior - (funcao(p_anterior, funcao_str)/funcao(p_anterior, derivada_str))
            erro_rel = erro_relativo(p, p_anterior)

            print("p{} =".format(i-1), p_anterior, "p{} =".format(i), p, "Erro rel.: {}".format(erro_rel))
            p_anterior = p
            
            # incrementa iterações
            i += 1
        else:
            print("A execução terminou sem encontrar quaisquer raízes.")
            return

    print("Execução de Newton concluída!")
    print("Uma das raízes possíveis da função '{}' é {}.".format(funcao_str, p))


def ponto_fixo(funcao_str, p0, precisao, N=N_MAX):
    """
    Busca uma raiz aproximada de uma função através do método do ponto fixo

    Args:
        funcao_str (string): string da função de iteração na sintaxe python 3
        p0 (float): chute inicial
        precisao (float): precisão estabelecida
    """
    i, p_anterior, erro_rel = 1, p0, precisao

    # condições de parada: n. de iterações e erro relativo < precisão
    while erro_rel >= precisao:
        if i < N+1:
            p = funcao(p_anterior, funcao_str)
            erro_rel = erro_relativo(p, p_anterior)

            print("p{} =".format(i-1), p_anterior, "p{} =".format(i), p, "Erro rel.: {}".format(erro_rel))
            p_anterior = p
            
            # incrementa iterações
            i += 1
        else:
            print("A execução terminou sem encontrar quaisquer raízes.")
            return

    print("Execução de ponto fixo concluída!")
    print("Uma das raízes possíveis da função '{}' é {}.".format(funcao_str, p))
        

if __name__ == "__main__":
    print("""==========
Implementação do Método da Bissecção
Autor: Bruno Ribeiro
Universidade Federal da Fronteira Sul - UFFS
Curso de Ciência da Computação
CCR: Cálculo Numérico
Professor: Paulo Boesing
Março/2018
==========""")
    menu = 5
    while menu not in range(4):
        menu = int(eval(input("Digite a opção desejada:\n1 - Bissecção\n2 - Ponto Fixo\n3 - Newton\n0 - Sair\nOpção: ")))
        
        if menu == 1:
            funcao_str = input("Digite a função a ser resolvida (sintaxe Python 3): ")
            a = float(eval(input("Digite o valor de 'a': ")))
            b = float(eval(input("Digite o valor de 'b': ")))
            precisao = float(eval(input("Digite a precisão do cálculo: ")))
            bisseccao(funcao_str, a, b, precisao)
            menu = 5 # restart
        elif menu == 2:
            funcao_str = input("Digite a função de iteração (sintaxe Python 3): ")
            p0 = float(eval(input("Digite o chute inicial 'p0': ")))
            precisao = float(eval(input("Digite a precisão do cálculo: ")))
            n = int(eval(input("Digite o número máximo de iterações: ")))
            ponto_fixo(funcao_str, p0, precisao, n)
            menu = 5 # restart
        elif menu == 3:
            funcao_str = input("Digite a função a ser resolvida (sintaxe Python 3): ")
            derivada_str = input("Digite a derivada da função (sintaxe Python 3): ")
            p0 = float(eval(input("Digite o chute inicial 'p0': ")))
            precisao = float(eval(input("Digite a precisão do cálculo: ")))
            n = int(eval(input("Digite o número máximo de iterações: ")))            
            newton(funcao_str, derivada_str, p0, precisao, n)
            menu = 5 # restart
        elif menu == 0:
            print("Saindo...")
        else:
            menu = 5 # restart
