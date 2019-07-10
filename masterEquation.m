tip = 1;

x = 50;
y = 50;
conc_grad = gradient2d(matrix,radius,center);

Tmn = chemoattractant(conc_grad,x,y,tip);
Tu = chemoattractant(conc_grad,x-1,y,tip);
Td = chemoattractant(conc_grad,x+1,y,tip);
Tl = chemoattractant(conc_grad,x,y-1,tip);
Tr = chemoattractant(conc_grad,x,y+1,tip);
Tuu = chemoattractant(conc_grad,x-2,y,tip);
Tdd = chemoattractant(conc_grad,x+2,y,tip);
Tll = chemoattractant(conc_grad,x,y-2,tip);
Trr = chemoattractant(conc_grad,x,y+2,tip);
Tul = chemoattractant(conc_grad,x-1,y-1,tip);
Tur = chemoattractant(conc_grad,x-1,y+1,tip);
Tdl = chemoattractant(conc_grad,x+1,y-1,tip);
Tdr = chemoattractant(conc_grad,x+1,y+1,tip);

TmnUp = Tu/(Tl+Tr+Tu+Td);
TmnDown = Td/(Tl+Tr+Tu+Td);
TmnLeft = Tl/(Tl+Tr+Tu+Td);
TmnRight = Tr/(Tl+Tr+Tu+Td);
TmoveUp = Tmn/(Tmn+Tdr+Tdl+Tdd);
TmoveDown = Tmn/(Tmn+Tur+Tul+Tuu);
TmoveLeft = Tmn/(Tmn+Tur+Trr+Tdr);
TmoveRight = Tmn/(Tmn+Tul+Tll+Tdl);

Pmn = TmoveRight + TmoveLeft + TmoveUp + TmoveDown - (TmnRight + TmnLeft + TmnUp + TmnDown)
