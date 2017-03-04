%Shayne O'Brien - Project Euler P30 Soln
%INTD 288 - Dr. Nicodemi
tic
k = 0;
runtotal = 0;
for i = 10:295277 
    % 10 since 2:9 cannot be written as sums of themselves^5,
    % 295277 since 299,999 --> 2^5 + 5*9^5 = 295277 < 299,999
    b = num2str(i);
    for j=1:size(b,2)
        k = k + str2double(b(j))^5;
    end
        if k == str2double(b)
            runtotal = runtotal + k;
        end
    k = 0;
end
toc