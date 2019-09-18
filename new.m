clear
clc

format long g

workspace = 200;
matrix=zeros(workspace);          % whole working space. Empty matrix
[m,n] = size(matrix);       % size of working space
center=[150,200];           % source of VEGF. center of concentration gradient
radius=pdist([1 1;center]); % radius of concentration. bigger than matrix so that the concentration covers the whole matrix

conc_grad = gradient2d(matrix,radius,center);

x = 100;                    % starting location for the tip cell
y = 1;
[num,tip] = size(x);

total_time = 500;            % time the simulation will run for in hours
k = .07;                    % constant. Time before cell "decides" where to move
iterations = total_time/k;  % total number of "decisions"/ iterations 

movement = zeros(workspace);
movement(x,y) = 1000;

for i = 1:iterations         % will go from one to the last integer value in ierations i.e iteration = 5.9 only goes to 5
    
    conc_grad(x,y) = 0;
    
    random_num = rand;
    
    if random_num <= PU
        if x ~= 1
            x = x - 1;
            movement(x,y)=1000;
        end
    elseif random_num <= PD + PU
        if x ~= m                   
            x = x + 1;
            movement(x,y)=1000;
        end
    elseif random_num <= PL + PD + PU
        if y ~= 1
            y = y - 1;
            movement(x,y)=1000;
        end
    else 
        if y ~= n
            y = y + 1;
            movement(x,y)=1000;
        end
    end
    
end


imagesc(movement+conc_grad)
colormap('jet');
