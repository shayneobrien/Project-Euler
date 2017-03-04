%Shayne O'Brien - Project Euler P40 Soln
%INTD 288 - Dr. Nicodemi
n = zeros(1,1e6);
for i = 1e6:-1:1
    n(i) = ((i) / 10^(i));
end
x = strrep(num2str(n));
a=1;
for i = 0:5
    a = a * str2num(x(10^i));
end