alli, somei :: Eq t=> t -> [t] -> Bool
alli x [] = False
alli x v = and map (==x) v
somei x v = or map (==x) v
