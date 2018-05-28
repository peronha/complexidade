from verificacao import verificaSubSetSum

def main():
    S = [3,1,1,2,2,1]
    S1 = [1,1,1,2]
    S2 =  [2,3]

    print(verificaSubSetSum(S,S1,S2))

    S1 = [3, 1, 1]
    S2 = [2, 2, 1]

    print(verificaSubSetSum(S,S1,S2))

    S1 = [5, 1, 1]
    S2 = [2, 2, 1]

    print(verificaSubSetSum(S,S1,S2))


    S1 = [1, 1, 1]
    S2 = [1, 1, 1]

    print(verificaSubSetSum(S,S1,S2))

    S1 = [2, 1, 1]
    S2 = [3, 2, 1]

    print(verificaSubSetSum(S,S1,S2))

    S1 = [2, 1, 1]
    S2 = [3, 1]

    print(verificaSubSetSum(S,S1,S2))


    return


if __name__ == "__main__":
    main()