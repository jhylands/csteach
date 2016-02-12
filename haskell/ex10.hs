middle :: String->Char
middle string = string!!(halfLength string)

halfLength :: [a]->Int
halfLength a = (length a) `div` 2
