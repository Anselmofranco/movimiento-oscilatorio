import matplotlib.pyplot as plt
import math as m


dt = 0.001
v=0
k=100
ma=3
x=0.04
w=(k/ma)**0.5
x_t=x
t=0

a=-(k/ma)*x
t=0
Ec=0.5*ma*v**2
Epk=0.5*k*x**2    
Em=Ec+Epk

while t<2: 
    
    plt.figure(1)
    plt.plot(x,v,"ro")
 
    plt.figure(2)
    plt.plot(t,x,"bx")
    plt.plot(t,x_t,"g.")
   
    plt.figure(3)
    plt.plot(t,Epk,"bo")
    plt.plot(t,Ec,"go")
    plt.plot(t,Em,"ro")
   
    v=v+a*dt
    x=x+v*dt         
    a=-(k/ma)*x
    x_t=0.04*m.cos(w*t)
    
    Ec=0.5*ma*v**2
    Epk=0.5*k*x**2    
    Em=Ec+Epk
   
    t = t+dt
   

plt.figure(1)
plt.show()
plt.figure(2)
plt.show()
plt.figure(3)
plt.show()



