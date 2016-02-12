data Period = AM | PM
starthour :: Period -> Int
starthour AM = 9
starthour PM = 14
data TimeOfDay = TimeOfDay Int Int 

validTimeOfDay :: TimeOfDay -> Bool
validTimeOfDay (TimeOfDay hours minuets) = and [hours<24, hours>=0,minuets>=0,minuets<60]

tod2period :: TimeOfDay -> Period
tod2period (TimeOfDay hours minuets) 
     | validTimeOfDay (TimeOfDay hours minuets) = undefined
     | hours>12 = PM
     | otherwise = AM

data IntExp = Const Int | Var String
     |Plus IntExp IntExp |Times IntExp IntExp
     | Minus IntExp
 deriving Eq

instance Show IntExp where
     show (Const n) = show n 
     show (Var s) = show s
     show (Plus a b) = show [show a ,"Plus" ,show b]
     show (Times a b) = show [show a, "Times", show b]
     show (Minus a) = show ["Minus", show a]

