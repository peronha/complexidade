# encoding utf-8
def verificaPartition(C,A,B):
    """
    :param C: [(int)] conjunto que deve conter os conjuntos A e B
    :param A: [(int)] primeiro conjunto da solução
    :param B: [(int)] segundo conjunto da solução
    :return: boolean: true se os subconjuntos pertencem a C, são disjuntos e suas somas são iguais
    """
    if somaIgual(A,B) and juncaoIgual(A,B,C):
        return True
    else:
        return False


def somaIgual(A,B):
    soma_a = somatorio(A)
    soma_b = somatorio(B)

    if soma_b - soma_a == 0:
        return True
    else:
        return False

def juncaoIgual(A,B,C):
    """
    Copia C para um vetor auxiliar e verifica se as juncoes de A e B sao iguais ao vetor C
    :return:  A U B == C ?
    """
    C_aux = list(C)
    juncao = list(A + B)
    return estaContidoRemove(juncao ,C_aux) and len(C_aux) == 0

def encontraElemento(elemento, V):
    for item in V:
        if elemento == item:
            return True

    return False


def estaContidoRemove(A,C):
    """
    Subtrai o conjunto A do C e retorna se está contido em C
    """
    for elemento in list(A):
        if encontraElemento(elemento,C):
            C.remove(elemento)
            A.remove(elemento)

    if len(A) == 0:
        return True

"""Complexidade N"""
def somatorio(C):
    soma = 0
    for i in C:
        soma += i
    return soma
