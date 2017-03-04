%Shayne O'Brien - Project Euler P48 Soln
%INTD 288 - Dr. Nicodemi
function f = PE48(x)
% find the last ten digits of x
a = 0;
for i = 1:x
        a = a + i^i;
        a = mod(a,10^i);
end
y = num2str(a);
%answer = y(length(y)-9:length(y));
fprintf('Answer: %.0\n', y(length(y)-9:length(y)))
end