%Shayne O'Brien Proj. Euler Problem 1 Solution 
%INTD 288 - Dr. Nicodemi
function [answer] = PE1(n) % input n as your sum limit
    answer = sum(unique([0:3:n, 0:5:n]));
end
