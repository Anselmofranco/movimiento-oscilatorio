import matplotlib.pyplot as plt
import math as m

dt = 0.01
v=0
k=100
ma=1
x=2
b=1
w_f=8
t=0
f=20
a=-(b/ma)*v-(k/ma)*x+(f/ma)*m.sin(w_f*t)
t=0
Ec=0.5*ma*v**2
Epk=0.5*k*x**2    
Em=Ec+Epk
while t<10: 
    plt.figure(1)
    plt.plot(x,v,"r.")
 
    plt.figure(2)
    plt.plot(t,x,"b.")
   
    plt.figure(3)
    plt.plot(t,Epk,"b.")
    plt.plot(t,Ec,"g.")
    plt.plot(t,Em,"r.")
    
    v=v+a*dt
    x=x+v*dt         
    a=-(b/ma)*v-(k/ma)*x+(f/ma)*m.sin(w_f*t)
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