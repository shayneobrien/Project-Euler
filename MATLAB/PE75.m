%Shayne O'Brien - Project Euler P75 Soln
%INTD 288 - Dr. Nicodemi
tic
triangle = zeros(1,1500001); %initialization vector
runningtab = 0; %count

for i = 2:sqrt((1.5e6)/2) %since one side is m^2 + n^2
    for j = 1:i
        if mod((i+j),2) == 1 && gcd(i,j) == 1 % if it's a right integer tri
            a = i^2 + j^2;
            b = j^2 - i^2;
            c = 2 * i * j;
            p = a + b + c;
            while p <= 1.5e6
                triangle(p) = triangle(p) + 1;
                if triangle(p) == 1
                    runningtab = runningtab + 1;
                end
                if triangle(p) == 2
                    runningtab = runningtab - 1;
                end
                p = p + (a + b + c);
            end
        end
    end
end
fprintf('Answer: %.0d\n', runningtab)
toc
