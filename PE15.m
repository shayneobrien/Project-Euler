%Shayne O'Brien - Project Euler P15 Soln
%INTD 288 - Dr. Nicodemi
function latticepaths = PE15(n)
mat = ones(n); % matrix of ones since each point takes 1 movement to get to
    for i = 2:n % i=2:n, use 2 because otherwise index messes up
        for j =2:n
            mat(j,i) = mat(j,i-1) + mat(j-1,i); % mat(j,i) increases based on
        end % number of times it is used in each pathway 
    end 
fprintf('Answer: %.0d\n', 2*sum(mat(n,:))) % add them all up, *2
end % we multiply by 2 because we didn?t include the initial point of matrix