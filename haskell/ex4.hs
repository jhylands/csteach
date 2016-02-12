allzero, somezero :: [Int] -> Bool
allzero [] = False
allzero xs = and [if xs!!i==0 then True else False | i <- [0..((length xs) -1)]]
somezero xs = or [if xs!!i==0 then True else False | i <- [0..((length xs) -1)]]
