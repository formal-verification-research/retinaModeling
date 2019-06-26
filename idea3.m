% retinaModeling agiogenesis

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

no = 0.1101;
n1 = 0.2250;
n2 = 0.1837;
n3 = 0.8163;
n4 = 0.4494;
n5 = 1.2250;
n6 = 0.5506;
n7 = 2.2250;

kf1 = 1.69;
kf2 = kf1 * 100;
kr1 = 0.02;
kr2 = kr1 / 100;
kp = 0.6667;
Rf = 0.02;

xo = 0.05;                  
K = 2;                      
Dp = 1.44*10^-4;

gamma = (2*kr2+kp)/(n5*n7*kf2);
theta = Rf*tip;

movement = zeros(workspace);
movement(x,y) = 1000;

for i = 1:iterations         % will go from one to the last integer value in ierations i.e iteration = 5.9 only goes to 5
    if x ~= 1 
        alpha = (kr1*Rf)/(2*kr2*conc_grad(x-1,y)+kr1);
        beta = (n4*(kp-2*kr1))/(2*kf1*conc_grad(x-1,y)+kr1);
        delta = n4 + beta;

        A = (-2*alpha*delta-gamma+theta*beta+sqrt((2*alpha*delta+gamma-theta*beta)^2+4*alpha*beta*(n4+delta)*(theta-alpha)))/(2*beta*(n4+delta));

        TU = exp((xo*K/Dp)*(K-(K+A)*exp(-A/K)));
    else
        TU = 0;             % tip cell is at the top edge of work space. Can't go up. Probability of up = 0
    end
    
    if x ~= m
        alpha = (kr1*Rf)/(2*kr2*conc_grad(x+1,y)+kr1);
        beta = (n4*(kp-2*kr1))/(2*kf1*conc_grad(x+1,y)+kr1);
        delta = n4 + beta;

        A = (-2*alpha*delta-gamma+theta*beta+sqrt((2*alpha*delta+gamma-theta*beta)^2+4*alpha*beta*(n4+delta)*(theta-alpha)))/(2*beta*(n4+delta));

        TD = exp((xo*K/Dp)*(K-(K+A)*exp(-A/K)));      
    else
        TD = 0;             % tip cell at bottom edge. Can't go down. Probability of down = 0
    end
    
    if y ~= 1
        alpha = (kr1*Rf)/(2*kr2*conc_grad(x,y-1)+kr1);
        beta = (n4*(kp-2*kr1))/(2*kf1*conc_grad(x,y-1)+kr1);
        delta = n4 + beta;

        A = (-2*alpha*delta-gamma+theta*beta+sqrt((2*alpha*delta+gamma-theta*beta)^2+4*alpha*beta*(n4+delta)*(theta-alpha)))/(2*beta*(n4+delta));

        TL = exp((xo*K/Dp)*(K-(K+A)*exp(-A/K)));        
    else
        TL = 0;             % tip cell at starting line. Can't go left. Probability of left = 0
    end
    
    if y ~= n
        alpha = (kr1*Rf)/(2*kr2*conc_grad(x,y+1)+kr1);
        beta = (n4*(kp-2*kr1))/(2*kf1*conc_grad(x,y+1)+kr1);
        delta = n4 + beta;

        A = (-2*alpha*delta-gamma+theta*beta+sqrt((2*alpha*delta+gamma-theta*beta)^2+4*alpha*beta*(n4+delta)*(theta-alpha)))/(2*beta*(n4+delta));

        TR = exp((xo*K/Dp)*(K-(K+A)*exp(-A/K)));        
    else
        time = ['time expired: ',num2str((i-1)*k), ' hours'];       
        disp(time)          % display amount of time taken
        break               % Tip cell has reached the RPE cells. Simulation over
    end
    
    PU = (TU/(TU+TD+TL+TR));
    PD = (TD/(TU+TD+TL+TR));
    PL = (TL/(TU+TD+TL+TR));
    PR = (TR/(TU+TD+TL+TR));
    
    conc_grad(x,y) = 0;
    
    random_num = rand;
    
    if random_num <= PU
        if x ~= 1
            x = x - 1;
            movement(x,y)=1000;
        end
    elseif random_num <= PD + PU
        if x ~= m                   % if x = 1 nothing happens?
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
