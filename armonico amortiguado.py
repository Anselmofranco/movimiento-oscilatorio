import matplotlib.pyplot as plt

dt = 0.01
v=0
k=1000
ma=10
x=4
b=500
t=0
a=-(b/ma)*v-(k/ma)*x
t=0
Ec=0.5*ma*v**2
Epk=0.5*k*x**2    
Em=Ec+Epk
while t<7: 
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
    a=-(b/ma)*v-(k/ma)*x
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
