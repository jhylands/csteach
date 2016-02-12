median :: (Fractional a, Ord a) => [a] -> a
median [x,y] = (x+y)/2
median [x] = x
median y = median (tail (init y))
