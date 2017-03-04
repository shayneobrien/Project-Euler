tic

lim = 75; % for testing
n = zeros(1,lim); % pre allocate
k = zeros(1,lim);
k(1) = 1; % indexing
k(2) = 2; % indexing
x = zeros(1,lim-5); % lim - 5 bc of the for loop below index
for n = 3:lim  
    for j = 1:n-1
        % factor is a built in matlab fnc
        x(j) = sum(factor(j))*k(n-j); 
    end
    k(n) = 1/n*(sum(factor(n)) + sum(x));
    if k(n) > 50000 % if good
        break
    end
end

final = n-3; % for k(1) and k(2)
fprintf('Answer: %.0d\n', final)
toc
