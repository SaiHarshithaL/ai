def tower(n,fr,tr,ar):
    if(n==0):
        return
    tower(n-1,fr,ar,tr)
    print("move disk ",n,"from rod ",fr,"to rod ",tr)
    tower(n-1,ar,tr,fr)
k= 3
tower(k, 'A', 'C', 'B')