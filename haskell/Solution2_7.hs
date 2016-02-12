module Solution2_7 where
import Data.Maybe
maxl ::[Int] -> Maybe Int
--maxl [] = Nothing
maxl [] = error "Empty List"
maxl (x:ys) = mxl x ys
	where 
        mxl x [] =Just x
        mxl x (y:ys) = mxl (if y>x then y else x) ys
rpt:: (Maybe Int) -> String
rpt (Just x) = show x
rpt Nothing = "No max"

mx::Int->Maybe Int->Maybe Int
mx x (Just y) = if x > y then Just x else Just y
mx x Nothing = Just x

reportmax:: [Int] -> String
reportmax [] = "There is no maximum of an empty list"
reportmax x = "The maximum is " ++ rpt (maxl x)

--Exersise finished
