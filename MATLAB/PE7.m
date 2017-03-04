%Shayne O'Brien - Project Euler P7 Soln
%INTD 288 - Dr. Nicodemi
function findprime = PE7(y)
i=1;
n=2; %first prime number
    while(i<y)
    n=n+1;   % incremental counter, n is what we want to be prime
    x=2;     % x will divide n. 1 divides everything, so start with x=2
        while x<=sqrt(n)  % because if there's no divisor by sqrt(n), there's no divisor ever
            if mod(n,x)==0
                break         % stop while loop if x divides n
            end
            x=x+1;          % otherwise keep incrementing x
        end
        if x>sqrt(n)  % if true, this means we got a prime
            i=i+1;    % so increment i by 1 (checking next number in sequence)
        end
    end
fprintf('Answer: %.0d\n', n)
end
