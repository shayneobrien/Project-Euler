%Shayne O'Brien - Project Euler P76 Soln
%INTD 288 - Dr. Nicodemi

function [] = PE76(number, min) % number >= min or else infinite loops
temp = 1;

while number > 1
    for i=1:floor(number/2)
        if i >= min
            k = number-i;
            temp = temp + PE76(k, i); % recursive fnc for all summations
        end
    end
end

fprintf('Answer: %.0d\n', temp)
end