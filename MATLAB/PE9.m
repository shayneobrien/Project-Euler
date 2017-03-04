%Shayne O'Brien - Project Euler P9 Soln
%INTD 288 - Dr. Nicodemi
tic
done = 0;
while done ~= 1
for a=1:1000
    for b=1:1000
        c = a^2 + b^2;
        if sqrt(c)+a+b==1000
           answer = sqrt(c)*a*b;
           done = 1;
        end
    end
end
end
fprintf('Answer is %.0d\n', answer)
toc
