% Shayne O'Brien - Project Euler P80 Soln
% INTD 288 - Dr. Nicodemi

digits(110)
total = 0; % type does not matter here, matlab does automatic

for i = 1:100 % first 100 natural numbers
    if length(char(vpa(sqrt(i)))) > 4 % under 10, square root won't have length > 3
        a = char(vpa(sqrt(i))); 
        a(2) = '0'; % set the '.' to 0 so total won't be affected
        for j = 1:101 % skip first 2 digits
            total = total + str2double(a(j)); % running count
        end
    end
end

fprintf('Answer: %.0d\n', total)
