def main() :
    #checkListaSimple()
    checkListaDoble()

# CHECK LISTA SIMPLE
def checkListaSimple() :
    from clases.listaSimple import ListaSimple

    LS = ListaSimple()

    # addFirst()
    print("addFirst()")
    for i in range(5) :
        LS.addFirst(i)
    LS.print()
    print("---------------------------------------")

    # addLast()
    print("addLast()")
    for c in 'abcde' :
        LS.addLast(c)
    LS.print()
    print("---------------------------------------")

    # removeFirst()
    print("removeFirst()")
    for i in range(3) :
        LS.removeFirst()
    LS.print()
    print("---------------------------------------")

    # removeLast()
    print("removeLast()")
    for i in range(3) :
        LS.removeLast()
    LS.print()
    print("---------------------------------------")

# CHECK LISTA DOBLE
def checkListaDoble() :
    from clases.listaDoble import ListaDoble
    from clases.nodoDoble import NodoDoble

    LD = ListaDoble()

    # addFirst()
    print("addFirst()")
    for i in range(5) :
        LD.addFirst(i)
    LD.print()
    print("---------------------------------------")

    # addLast()
    print("addLast()")
    for c in "abcde" :
        LD.addLast(c)
    LD.print()
    print("---------------------------------------")

    # removeFirst()
    print("removeFirst()")
    for i in range(3) :
        LD.removeFirst()
    LD.print()
    print("---------------------------------------")

    # removeFirst()
    print("removeLast()")
    for i in range(3) :
        LD.removeLast()
    LD.print()
    print("---------------------------------------")

    # remove()
    print("remove()")
    LD.remove("a")
    LD.print()
    print("---------------------------------------")

    # addBefore()
    print("addBefore()")
    LD.addBefore(0, "x")
    LD.print()
    print("---------------------------------------")

    # addAfter()
    print("addAfter()")
    LD.addAfter(0, "y")
    LD.print()
    print("---------------------------------------")

main()
