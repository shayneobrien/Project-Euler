%Shayne O'Brien - Project Euler P39 Soln
%INTD 288 - Dr. Nicodemi
function f = PE39(x)
% find maximum value of p <= x, where p is our number of solutions
final = zeros(1,x);
for a = 1:(x/3)
    p = 1;
    b = a;
    while p < x
        b = b + 1;
        c = sqrt((a^2)+ (b^2));
        p = a + b + c;
        if mod(p,1)==0 % if it's an integer and therefore has a soln,
           final(1,p) = final(1,p) + 1; % set the index value to true and the value
        end 
    end
end
[y,z] = max(final); % output where answer is saved to...
fprintf('Answer: %.0d\n', z)
fprintf('No. Solutions: %0.d\n', y)
end
