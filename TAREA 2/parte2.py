def main() :
    #checkStack()
    checkQueue()

def checkStack() :
    from clases.stack import Stack

    print("STACK")
    S = Stack()

    # push()
    print("push()")
    for i in range(5) :
        S.push(i)
    S.print()
    print("---------------------------------------")

    # top()
    print("top()")
    print(S.top())
    print("---------------------------------------")
    
    # pop()
    print("pop()")
    for i in range(3) :
        S.pop()
    S.print()
    print("---------------------------------------")

    # top()
    print("top()")
    print(S.top())
    print("---------------------------------------")

def checkQueue() :
    from clases.queue import Queue

    print("QUEUE")
    Q = Queue()

    # enqueue()
    print("enqueue()")
    for i in range(5) :
        Q.enqueue(i)
    Q.print()
    print("---------------------------------------")

    # first()
    print("first()")
    print(Q.first())
    print("---------------------------------------")

    # dequeue()
    print("dequeue()")
    for i in range(3) :
        Q.dequeue()
    Q.print()
    print("---------------------------------------")

    # first()
    print("first()")
    print(Q.first())
    print("---------------------------------------")

main()