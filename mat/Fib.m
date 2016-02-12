function [ numbers ] = Fib( number )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    numbers = ones(1,number);
    n2=0;
    n1=1;
    numbers(1)=1;
    for i = 2:number
        n=n1+n2;
        n2=n1;
        n1=n;
        numbers(i) = n;
    end
    

end

