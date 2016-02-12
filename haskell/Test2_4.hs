module Test2_4 where 
import Test.QuickCheck
import Solution2_4
test_zerofy :: IO()
test_zerofy = quickCheck tz
 where tz xs = zerofy xs == map(const 0) xs

copies:: Char -> Int -> String
copies c 0 = []
copies c n = |n>0 c:(copies c (n-1))
             |otherwise "copies: negatie argument"

--Test_copies = length(copies c n) = n 
