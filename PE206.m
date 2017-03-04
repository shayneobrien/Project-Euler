% Shayne O'Brien - Project Euler P206 Soln
% INTD 288 - Dr. Nicodemi

% 1_2_3_4_5_6_7_8_9_0
% smallest is  1020304050607080900
% --> sqrt(smallest) = 1010101010.10101008
% largest is   1929394959697989990
% --> sqrt(largest) = 1389026623.10626364
% our bounds are then 1010101010 to 1389026623
% 378,925,613 possible answers to check

% script needs to be optimized because we use vpa(i^2) in line 21, which
% eats up a lot of computational power (Matlab precision problem)
tic
digits(18)
true = 0;
i = 1010101010; % start at smallest
z = 0;

for i = 1010101010:1389026623
    z = z + 1;
    k = char(vpa(i^2)); % this is what kills 
    count = 0;
    for j = 1:2:19
        if str2double(k(j)) == j;
            count = count + 1;
        else
            break % no need to keep going
        end
    end
    if count == 10
        fprintf('Answer: \n', i)
        break
    else
        i = i+1;
    end
end
toc