%Shayne O'Brien - Project Euler P3 Soln
%INTD 288 - Dr. Nicodemi
function primefactor = PE3(n) % n is your input
i = 2; % start at the smallest prime
while n~=1 
    while mod(n,i) ~= 0 %keep trying to find a divisor...
        i = i+1;  %increase i by 1 until we find a divisor..
    end
    prime = i; % keeps track of current divisor
    n = n/prime;
    i = i+1;
end
fprintf('The biggest prime factor of n is: %.0d\n', prime)
end
