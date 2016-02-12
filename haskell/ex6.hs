alli, somei :: Int -> [Int] -> Bool
alli x [] = False
alli x v = and [not (v!!i==x) | i<-[0..((length v)-1)]]
somei x v = or [not (v!!i==x) | i<-[0..((length v)-1)]]
