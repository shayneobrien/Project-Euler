%Shayne O'Brien - Project Euler P100 Soln
%INTD 288 - Dr. Nicodemi
tic
% some algebra...
% b/n * ((b-1)/(n-1)) = 0.50
% (b^2 - b)/(n^2 - n) = 0.50
% (b^2 - b) = 0.50*(n^2 - n)
% (2b^2 - 2b) = (n^2 - n)
% 2b^2 - 2b - n^2 + n = 0
% --> diophantine equation, plug into online calculator
% b(k+1) = 3bk + 2nk -2
% n(k+1) = 4bk + 3nk -3

b = 15; % base value for b
n = 21; % base value for n
stop = 1e12;

while n < stop
    temporaryb = 3*b + 2*n - 2; % b(k+1)
    temporaryn = 4*b + 3*n - 3; % n(k+1)
    b = temporaryb;
    n = temporaryn;
end
fprintf('Number of blues: %.0f\n', b) %disp ans
toc