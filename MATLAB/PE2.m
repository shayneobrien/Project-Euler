%projecteuler.net
%Shayne O'Brien
%Problem 3 Soln
%INTD 288 - Dr. Nicodemi
tic
n = 600851475143; % given number to find largest prime factor of
i = 2; % start at the smallest prime
while n~=1 
    while mod(n,i) ~= 0 %keep trying to find a divisor...
        i = i+1;  %increase i by 1 until we find a divisor..
    end
    prime = i; % keeps track of current divisor
    n = n/prime;
    i = i+1;
% it's like factor trees, but the smaller divisor does not have to be 2
end
fprintf('The biggest prime factor of n is: %.0d\n', prime)
toc
