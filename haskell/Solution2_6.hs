slz :: [Int] -> [Int]
slz [] = []
slz  (x:xs) | x==0 = slz xs
            | otherwise = x:xs
--section complete but not saved
