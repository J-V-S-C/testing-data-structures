def insertion_sort(lista):
    """
    Pega um elemento por vez e o insere
    na posição correta da parte já ordenada.
    """
    
    n = len(lista)
    

    # i representa o elemento que vamos inserir
    # na parte que já está ordenada.
    for i in range(1, n):
        # Guarda o valor que queremos posicionar.
        atual = lista[i]

        # j começa na posição de "atual"
        # e vai andando para a esquerda.
        j = i

        # Enquanto houver elementos à esquerda
        # maiores que "atual", deslocamos esses
        # elementos uma posição para a direita.
        while j > 0 and lista[j - 1] > atual:
            lista[j] = lista[j - 1]

            # Anda uma posição para a esquerda.
            j -= 1

        # Coloca "atual" na posição correta.
        lista[j] = atual

        print(f"i={i}: {lista}")

    return lista


numeros = [70, 90, 3, 0, 100, 2]

print("Original:", numeros)
print("Ordenada:", insertion_sort(numeros))
