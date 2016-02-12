w= [ [1:1:127] [128:-1:1] ] ;
% logHDR = ones(650,450,3);
for row = 1:650
    row
for col = 1:450
for chan = 1:3
% 1. Extract the vector of intensity values (see part 1)
toBeGd = squeeze(images(row,col,chan,:));
% 2. Transform the intensities to log intensities using g (see part 3)
logH = g(toBeGd+1);
% 3. Compute the weights for the intensities using w (see part 2)
squeezedValues = w(toBeGd+1);
% 4. Compute the vector difference between the log intensities and the log of the exposure times in t
diff = logH - log(t);
% 5. Scale the differences by the weights and take the sum
scaledDiff = sum(squeezedValues'.*diff);
% 6. Compute the sum of the weights
sumOfWeighd = sum(toBeWeighd);
% 7. Compute the final log HDR values by dividing the result of step 5 by the result of step 6:
result=scaledDiff./sumOfWeighd;
% logHDR(row,col,chan) = ...
logHDR(row,col,chan)=result;
end
end
end