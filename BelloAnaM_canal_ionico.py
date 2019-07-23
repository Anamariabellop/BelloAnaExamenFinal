import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


datos= np.genfromtxt("Canal_ionico.txt")
xobs= datos[:,0]
yobs= datos[:,1]


def modelo(x,y):
    return np.sqrt(x**2 + y**2) 

def verosimilitud(obs,model):
    suma= np.sum((obs-model)**2)
    return np.exp(0.5*suma)

plt.figure()
plt.scatter(xobs,yobs)
plt.savefig("datos.png")

xini=-4.5
yini=7.05 #guiado del txt

radio=[]

for i in range(len(xobs)):
    radio.append(np.sqrt(xobs[i]**2 + yobs[i]**2)) 
    

def MCMC(xini,yini,xobser,yobser,iteraciones,sigma):
    x=[]
    y=[]
    racep=[]
    L=[]
    
    x.append(xini)
    y.append(yini)
    
    rini= np.sqrt(xini**2 + yini**2) 
    racep.append(rini)   
    
    for i in range(iteraciones):
        xnuevo= np.random.normal(x[i],sigma)
        ynuevo= np.random.normal(y[i],sigma)
        rnuevo=np.random.normal(Racep[i],sigma)
        Lnuevo= np.random.normal(L[i],sigma)
      
        alpha= verosimilitud(radio,rnuevo)/verosimilitud(radio,racep[i])
    
        #obs= modelo(xini,yini)
        #inicio= verosimilitud()
        
        if( alpha > 1):
            x.append(xnuevo)
            y.append(ynuevo)
            racep.append(rnuevo)
            L.append(Lnuevo)
        else:
            beta= np.random.uniform(0,1)
            
            if( beta > alpha):
                x.append(xnuevo)
                y.append(ynuevo)
                racep.append(rnuevo)
                L.append(Lnuevo)
            else:
                x.append(x[i])
                y.append(y[i])
                racep.append(racep[i])
                L.append(L[i])              
    return x,y,racep,L
                


#fig, ax = plt.subplots()
#plt.axis('equal')
#circle1 = plt.Circle((best_x, best_y), np.max(r_walk), color='r',fill=False)
#ax.add_artist(circle1)
#plt.savefig("Canal.png")
#plt.close()
