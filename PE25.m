%Shayne O'Brien - Project Euler P25 Soln
%INTD 288 - Dr. Nicodemi

format long
%using Binet's formula this problem is trivial
phi = (1+sqrt(5))/2;
nodigit = 1000;
term = ceil((nodigit-1 + log10(5)/2) / log10(phi)); %ceil fnc rounds up towards inf
fprintf('The term to contain 1000 digits is %.0d\n',term)