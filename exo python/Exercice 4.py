#Exercice4:

N=int(input("saisissez nombre: "))  #On demande à l'utilisateur de saisir un nombre
Nbas=0
Nhaut=N
while(Nhaut-Nbas>0.001):
    L=(Nhaut+Nbas)/2       
    if(L*L>N):       #on compare L puissance 2 au nombre qui a été saisi pas l'utilisateur. 
        Nhaut=L
    else:
        Nbas=L
print('La racine de' ,N, 'est',L)     #On affiche la racine de N qui est égle à L.
    
