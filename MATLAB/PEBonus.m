%Shayne O'Brien - Marcus' Problem
%INTD 288 - Dr. Nicodemi
i = 1;
n = 1;
truth = 0;
A = PE14;
B = P2E14;
while truth ~=1
    k = n+2;
    n = n+1;
        for i = 1:n
        current = n;
        iterations = 1;
        n = i;
        while n~=1
            if mod(n,2) == 0
                n = n/2;
                iterations = iterations + 1;
                else
                n = 3*n+1;
                iterations = iterations + 1;
            end
            if current < iterations
                current = iterations;
                answer = n;
            end
        end
        end
            for i = 1:k
                current2 = k;
                iterations2 = 1;
                k = i;
                    while k~=1
                        if mod(k,2) == 0
                            k = k/2;
                            iterations2 = iterations2 + 1;
                        else
                            k = 3*k+1;
                            iterations2 = iterations2 + 1;
                        end
                    end
            end
            if current2 < iterations2
                current2 = iterations2;
                answer2 = k;
            end
    if (iterations == iterations2) && ~(mod(itn-3,8)==4 && A(itn-3)==(A(itn-3)+1))
        smallest = n;
        truth = 1;
        break
    elseif (iterations == iterations2) && ~(mod(itn-3,4)==8 && A(itn-3)==(A(itn-3)+1))
        smallest = n;
        truth = 1;
        break
    end
end
fprintf('The smallest x is %.0d\n', smallest)
        
