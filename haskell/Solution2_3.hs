module Solution2_3 where

sum3 :: Int -> Int->Int->Int
sum3 x y z = x + y + z

middle :: String -> Char
middle string = string!!n 
     where len = length string
	   n = len `div` 2

