clc
clear all


A=[0 1;0 0];
B=[0;1];
C=[1 0];

L1=[2 -1 ;-1 3];
beta=0.5;

setlmis([]);
P1=lmivar(1,[2 1]);
Z1=lmivar(2,[2 1]);

lmiterm([1,1,1,P1],1,A,'s');  
lmiterm([1,1,1,Z1],1,C,'s'); 
lmiterm([1,1,1,0],beta); 
lmiterm([2,1,1,P1],-1,1);

lmis=getlmis;
[tmin,xfeas]=feasp(lmis,[0,0,100,0,0],0);
P1=dec2mat(lmis,xfeas,P1);
Z1=dec2mat(lmis,xfeas,Z1);
tmin
L2=inv(P1)*Z1;

setlmis([]);
P2=lmivar(1,[2 1]);
Z2=lmivar(2,[1 2]);

lmiterm([1,1,1,P2],A,1,'s');  
lmiterm([1,1,1,P2],L2*C,1,'s'); 
lmiterm([1,1,1,Z2],B,1,'s'); 
lmiterm([1,1,1,0],beta); 
lmiterm([2,1,1,P2],-1,1);

lmis=getlmis;
[tmin,xfeas]=feasp(lmis,[0,0,100,0,0],0);
P2=dec2mat(lmis,xfeas,P2);
Z2=dec2mat(lmis,xfeas,Z2);

tmin

