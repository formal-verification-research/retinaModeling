function d= gradient2d(mat,radius,center)
d=mat;
[m,n]=size(d);
for i=1:m
    k = 1;
    for j=1:n
        D = pdist([i j;center]);
        x= radius-D;
        d(i,j)=d(i,j)+x;
        k = k + 1;
    end
end
