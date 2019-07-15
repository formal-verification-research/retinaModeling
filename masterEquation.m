clear
clc

tip = 1;

workspace = 200;
matrix=zeros(workspace);          % whole working space. Empty matrix
[m,n] = size(matrix);       % size of working space
center=[150,200];           % source of VEGF. center of concentration gradient
radius=pdist([1 1;center]);
x = 5;
y = 5;
conc_grad = gradient2d(matrix,radius,center);

Tu=0;Td=0;Tl=0;Tr=0;Tuu=0;Tdd=0;Tll=0;Trr=0;Tur=0;Tul=0;Tdr=0;Tdl=0;

Tmn = chemoattractant(conc_grad,x,y,tip);

if x>1
    Tu = chemoattractant(conc_grad,x-1,y,tip);
    if y>1
        Tul = chemoattractant(conc_grad,x-1,y-1,tip);
    if y<n
        Tur = chemoattractant(conc_grad,x-1,y+1,tip);
    if x>2
        Tuu = chemoattractant(conc_grad,x-2,y,tip);
    end
    end
    end        
end

if x<m
    Td = chemoattractant(conc_grad,x+1,y,tip);
    if y>1
        Tdl = chemoattractant(conc_grad,x+1,y-1,tip);
    if y<n
        Tdr = chemoattractant(conc_grad,x+1,y+1,tip);
    if x<m-1
        Tdd = chemoattractant(conc_grad,x+2,y,tip);
    end
    end
    end
end

if y>1
    Tl = chemoattractant(conc_grad,x,y-1,tip);
    if y>2
        Tll = chemoattractant(conc_grad,x,y-2,tip);
    end
end

if y<n
    Tr = chemoattractant(conc_grad,x,y+1,tip);
    if y<n-1
        Trr = chemoattractant(conc_grad,x,y+2,tip);
    end
end

TmnUp = Tu/(Tl+Tr+Tu+Td);
TmnDown = Td/(Tl+Tr+Tu+Td);
TmnLeft = Tl/(Tl+Tr+Tu+Td);
TmnRight = Tr/(Tl+Tr+Tu+Td);
TmoveUp = Tmn/(Tmn+Tdr+Tdl+Tdd);
TmoveDown = Tmn/(Tmn+Tur+Tul+Tuu);
TmoveLeft = Tmn/(Tmn+Tur+Trr+Tdr);
TmoveRight = Tmn/(Tmn+Tul+Tll+Tdl);

Pmn = TmoveRight + TmoveLeft + TmoveUp + TmoveDown - (TmnRight + TmnLeft + TmnUp + TmnDown)



