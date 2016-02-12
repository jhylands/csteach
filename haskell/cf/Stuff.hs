module Stuff where
import LexIntExp
import ParIntExp
import ErrM
import AbsIntExp

pl = pIntExp . myLexer

handleResult:: Err a -> a
handleResult (Ok t) = t
handleResult (Bad s) = error s



simpIntExp :: IntExp -> IntExp
simpIntExp (EAdd a (Eint 0)) = simpIntExp a
simpIntExp (EAdd (Eint 0) b) = simpIntExp b
simpIntExp (EAdd a b) = EAdd (simpIntExp a) (simpIntExp b)
simpIntExp (EMul a (Eint 0)) = Eint 0
simpIntExp (EMul (Eint 0) b) = Eint 0
simpIntExp (EMul a (Eint 1)) = simpIntExp a
simpIntExp (EMul (Eint 1) b) = simpIntExp b
simpIntExp (EMul a b) = EMul (simpIntExp a) (simpIntExp b)
simpIntExp (EMin (EMin a)) = simpIntExp a
simpIntExp (EMin a) = EMin (simpIntExp a)
simpIntExp e = e -- catches all other cases (Const & Var)


ie2scheme::IntExp->String
ie2scheme (EMul a b) = "(* " ++ ie2scheme a ++ " " ++ ie2scheme b  ++ ")"
ie2scheme (EAdd a b) = "(+ " ++ ie2scheme a ++ " " ++ ie2scheme b ++ ")"
ie2scheme (EMin a) = "(- " ++ ie2scheme a ++ ")"
ie2scheme (Eint a) = show a
ie2scheme (Evar a) = show a

n2scheme::String->String
n2scheme = ie2scheme . simpIntExp . handleResult . pIntExp . myLexer

