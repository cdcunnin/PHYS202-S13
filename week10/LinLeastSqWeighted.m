function [m, b, uncm, uncb] = LinLeastSqWeighted(x,y,w)
%This takes in x and y values and their weighting and returns the equation
%of a linear approximation of the data.
sumw=sum(w)
S = sum(sum(w));
WX = sum(sum(w.*x));
WY = sum(sum(w.*y));
WX2 = sum(sum(w.*(x.^2)));
WXY = sum(sum(w.*x.*y));
m = (S*WXY - WX*WY)/(S*WX2 - WX^2);
b = (WX2*WY - WX*WXY)/(S*WX2 - WX^2);
if sumw/len(w)=1:
    xavg = mean(x);
    x2 = mean(x.^2);
    s2 = mean( (y-(m*x+b)).^2 );
    uncm = abs( (1.0/length(x(:))-2) * (s2/((x2-xavg^2))) )^(0.5);
    uncb = abs( (1.0/length(x(:))-2) * ((s2*x2)/((x2-xavg^2))) )^(0.5);
else:
    uncm = ( S/(S*WX2-WX^2) )^0.5;
    uncb = ( WX2/(S*WX2-WX^2) )^0.5;
end

