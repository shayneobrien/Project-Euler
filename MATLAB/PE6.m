%Shayne O'Brien - Project Euler P6 Soln
%INTD 288 - Dr. Nicodemi
tic
n = 1:100; %range to consider
sumsquare = sum((n.^2)); %sum of squares
squaresum = (sum(n))^2; %square of sums
result = abs(sumsquare-squaresum); %use absolute value because we?re looking for the difference
fprintf('The difference is %.0d\n', result)
toc
