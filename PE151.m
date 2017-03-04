%Shayne O'Brien - Project Euler P151 Soln
%INTD 288 - Dr. Nicodemi

tic
% increase 1e4 to higher for greater precision
% here we use markov chains to solve the problem, i am sure there is
% another way to do this probabilistically to get a more precise answer
matrix = zeros(1,1e4);

for i = 1:length(matrix)
cut = [ 1 1 1 1 ];
proba5 = 0;
while sum(cut) ~= 0
    guess = randi(4); 
    while cut(guess) == 0
         guess = randi(4);
    end

if guess == 1
        cut  = [ cut(1)-1, cut(2)+1, cut(3)+1, cut(4)+1 ];
        proba5 = proba5 + cut(4)/sum(cut)*1/16;
elseif guess == 2
        cut = [ cut(1), cut(2)-1, cut(3)+1, cut(4)+1 ];
        proba5 = proba5 + cut(4)/sum(cut)*1/16;
elseif guess == 3
        cut = [ cut(1), cut(2), cut(3)-1, cut(4)+1 ];
        proba5 = proba5 + cut(4)/sum(cut)*1/16;
elseif guess == 4
    if sum(cut) == 1
        % proba5 = proba5 + 1/15;
        cut = [ cut(1), cut(2), cut(3), cut(4)-1 ];
    else
        cut = [ cut(1), cut(2), cut(3), cut(4)-1 ];
        proba5 = proba5 + cut(4)/sum(cut)*1/16;
    end
end
end
matrix(i) = proba5;
new = sum(matrix)/length(matrix);
end
% will be close, but not exact..
answer = 1 - sum(matrix)/length(matrix); % we calculated the probability of not having 1 piece
fprintf('Answer: %.7d\n', answer)
toc