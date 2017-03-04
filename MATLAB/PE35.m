%Shayne O'Brien - Project Euler P35 Soln
%INTD 288 - Dr. Nicodemi
function f = PE35(x)
% find number of circular primes below input x
primelist = primes(x);
count = 0;
v = [];
    for i = 1:size(primelist,2) % for all primes under x
        b = num2str(primelist(i)); % convert to string
        for j = 1:size(b,2) % for all characters in string
            b = strcat(b,b(1)); %add first digit to end
            b(1) = []; %remove first digit
            if isprime(str2double(b)) ~= 1 || b(1) == 0 %not prime or not same #
                break % quit the for loop
            else 
                v = [v str2double(b)]; % otherwise add to vector
            end
        end
        if size(v,2) == size(b,2) && all(isprime(v)) == 1 % isprime([]) yields 1
            count = count + size(v,2);
           for k = 1:size(v,2)
               primelist(primelist==v(k)) = 1; %remove duplicates by setting to non-prime
           end
        end
        v = []; % reset vector
    end
    fprintf('The number of primes under %0.d is %0.d.\n', x, count-1) % subtract 1 due to 11
end
