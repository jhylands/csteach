module Solution2_4 where
-- Ex 12
zerofy :: [Int] -> [Int]
zerofy [] = []
zerofy xs = 0 : zerofy ( tail xs)

