from clases.listaSimple import ListaSimple
from clases.listaDoble import listaDoble
from clases.ArrayStack import Stack

l = ListaSimple()

l.addFirst(0)
l.addLast(5)
l.addFirst(3)
l.addLast(15)

l.print()
print("####")
l.removeFirst()
l.removeLast()

l.print()
print("#########")
li=listaDoble()
li.addFirst(10)
li.addLast(2)
li.addLast(5)
c=li.head.next
li.addBefore(c,20)
li.removeFirst()
li.removeLast()
li.remove(li.head.next)
li.print()
print("############### desde aca:")
l1=ListaSimple()
l1.addFirst(3)
st=Stack(l1)
st.push(5)
st.push(8)
st.pop()
st.print()