%Shayne O'Brien - Project Euler P72 Soln
%INTD 288 - Dr. Nicodemi
function PE72(n)
% count elements contained in set of reduced proper fractions for d <= n
    sum=0;
    for i=2:n
        sum = sum+totient(i);
    end
format rat;
sum
end