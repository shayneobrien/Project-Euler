%Shayne O'Brien - Project Euler P79 Soln
%INTD 288 - Dr. Nicodemi

passcodes = '319680180690129620762689762318368710720710629168160689716731736729316729729710769290719680318389162289162718729319790680890362319760316729380319728716';
firstdigit = zeros(1,(size(passcodes,2)/3));
seconddigit = zeros(1,(size(passcodes,2)/3));
thirddigit = zeros(1,(size(passcodes,2)/3));
a = 1;
b = 1;
c = 1;

% first digit
for i = 1:3:size(passcodes,2)
    firstdigit(a) = str2double(passcodes(i));
    a = a + 1;
end
% second digit
for i = 2:3:size(passcodes,2)
    seconddigit(b) = str2double(passcodes(i));
    b = b + 1;
end
% third digit
for i = 3:3:size(passcodes,2)
    thirddigit(c) = str2double(passcodes(i));
    c = c + 1;
end

a = firstdigit(:);
a(:,2) = seconddigit(:);
a(:,3) = thirddigit(:);


comesafter = [0;1; 2; 3; 4;5;6;7;8;9];
comesafter(:,2:12) = -1*ones(10,11);
comesbefore = comesafter;


for i = 1:size(a,1)
    b = a(i,1);
    c = a(i,2);
    d = a(i,3);
    comesafter(b+1,c+2) = c; % second col comes after first
    comesafter(b+1,d+2) = d; % third col comes after first
    comesafter(c+1,d+2) = d; % third col comes after second
    comesbefore(d+1,b+2) = b; % first col comes before third
    comesbefore(d+1,c+2) = c; % second col comes before third
    comesbefore(c+1,b+2) = b; % first col comes before second
end

for i = 1:10
    for j = 1:12
        if comesafter(i,j) == -1
            comesafter(i,j) = NaN;
        end
        if comesbefore(i,j) == -1
            comesbefore(i,j) = NaN;
        end
    end
end

% and then we do pattern analysis to figure out answer

% sumsafter = [0; 1; 2; 3; 4;5;6;7;8;9];
% sumsafter(:,2) = zeros(10,1);
% sumsbefore = sumsafter;
% 
% comesbefore = comesbefore(:,2:11);
% comesafter = comesafter(:,2:11);
% 
% for i = 1:10
%     sumsafter(i,2) = sum(comesafter(i,:));
%     sumsbefore(i,2) = sum(comesbefore(i,:));
% end
