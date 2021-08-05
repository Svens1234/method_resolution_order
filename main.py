#class A:
    #def some_method(self):
        #print('Method of class A')


#class B(A):
    #def some_method(self):
        #print('Method of class B')


#class C(A):
    #def some_method(self):
        #print('Method of class C')


#class D(B,C):
    #def some_method(self):
        #print('Method of class D')


#some_object = D()
#some_object.some_method()


#class A:
    #def some_method(self):
        #print('Method of class A')


#class B(A):
    #def some_method(self):
        #print('Method of class B')


#class C(A):
    #def some_method(self):
        #print('Method of class C')


#class D(B,C):
    #pass


#print(D.__mro__)

#some_object = D()
#some_object.some_method()




#class A:
    #def some_method(self):
        #print('Method of class A')


#class B(A):
    #pass


#class C(A):
    #def some_method(self):
        #print('Method of class C')


#class D(B,C):
    #pass


#print(D.__mro__)

#some_object = D()
#some_object.some_method()


#class A:
    #def some_method(self):
        #print('Method of class A')


#class B(A):
    #pass


#class C(A):
    #pass


#class D(B,C):
    #pass


#print(D.__mro__)

#some_object = D()
#some_object.some_method()




#class A:
    #pass


#class B(A):
    #pass


#class C(A):
    #pass


#class D(B,C):
    #pass


#print(D.__mro__)

#some_object = D()
#some_object.some_method()



class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B,C):
    pass


print(D.__mro__)
print(D.mro())
help(D)
#some_object = D()
#some_object.some_method()

