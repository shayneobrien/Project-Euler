function f = PE14(n)
current = 0;
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
end


