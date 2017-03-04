%Shayne O'Brien - Project Euler P53 Soln
%INTD 288 - Dr. Nicodemi
limit = 1e6;
current = 0;
for n = 1:100
    for r = 0:n
        b = nchoosek(n,r);
        if b > limit
            current = current + 1;
        end
    end
end
fprintf('The number of values for nCr above 1e6 is %.0d\n', current)
