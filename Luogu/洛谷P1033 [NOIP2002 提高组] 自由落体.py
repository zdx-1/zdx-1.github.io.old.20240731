from math import *
h,s,v,l,k,n=map(float,input().split())
t_max=sqrt(h/5)
t_min=sqrt((h-k)/5)
i_b=int(s-t_min*v+1)
i_e=int(s-t_max*v)
i_b=min(i_b,n)
i_e=max(i_e,0)
print(int(i_b-i_e))
