#lang racket

; Constants
;    are NUMBERS

(define (a-constant x)
  (if (number? x) x
		  (error x "is not a constant")
  )
)

(define (constant? x) ;lexer-type check to recognise token
         (number? x)  ;of type constant
)

; Variables
;    are SYMBOLS 

(define (a-variable x)
  (if (symbol? x) x
		  (error x "is not a symbol")
  )
)

(define (variable? x) ;lexer-type check to recognise token
         (symbol? x)  ;of type variable
)

(define (=var? x y) 
  (and	(symbol? x)
	(symbol? y)
	(eq? x y)		;; use eq? for symbols
  )
)


;; Sums 
;;   are fully parenthesised prefix notation expressions
;;   => just like scheme expressions!

(define (a-sum x y) 
  (list '+ x y)
)

(define (sum? expr)  ;recognising a sum expression as a list 
  (if (list? expr)   ;starting with '+': detecting '(' and ')' and '+'
	 (eq? (car expr) '+) ;would be the lexer's job, matching '(' and ')'
	 #f                  ;is the parser's.
  )
)

(define (addend expr)
  (if (sum? expr) (cadr expr)
		  (error expr "is not a sum")
  )
)

(define (augend expr)
  (if (sum? expr) (caddr expr)
		  (error expr "is not a sum")
  )
)

;; Products
;;   are just like sums!

(define (a-product x y) 
  (list '* x y)
)

(define (product? expr) ;recognising a product expression
  (if (list? expr)      ;again, a lexer-parser combo here.
	 (eq? (car expr) '*)
	 #f
  )
)

(define (multiplier expr)
  (if (product? expr) (cadr expr)
		  (error expr "is not a product")
  )
)

(define (multiplicand expr)
  (if (product? expr) (caddr expr)
		  (error expr "is not a product")
  )
)
; main procedure
(define (diff expr var)
      (cond ((constant? expr) ;syntactic rule for a primitive expression.. 
              (a-constant 0)  ;..and the value of its derivative (=semantics).
            )
            ((variable? expr) ;synt. rule for a primitive expr. (the name of a variable)...
               (if (=var? expr var) 
                   (a-constant 1)  ; ..and the value of its derivative (=semantics)
                   (a-constant 0)  ; ..for the two possible cases.
               )
            )
            ((sum? expr)      ;syntactic rule for a compound expression of type sum...
               (a-sum (diff (addend expr) var) ; ...and the value of
                      (diff (augend expr) var) ;    its derivative.
               )
            )
           ;;COMPLETE THIS DEFINITION
           ((product? expr)
            (a-product (diff (multiplier expr) var)
                       (diff (multiplicand expr) var)
            )
           )
            (else (error "diff: unrecognisable type: " expr))
       )
 )

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; TEST EXAMPLES
;;
;;  expr1 = x+3

(define expr1 (a-sum (a-variable 'x) (a-constant 3)))

;;
;;  expr2 = x*y

(define expr2 (a-product (a-variable 'x) (a-variable 'y)))

;;  expr3 = (x*y)*(x+3)
;;        = (x*y)*expr1

(define expr3 (a-product (a-product (a-variable 'x)
				    (a-variable 'y)
			 )
			 expr1
	      )
)

;; expr4 = 10x^2 + 3x -5
(define expr4 (a-sum (a-product (a-constant 10)
				(a-product (a-variable 'x)
					   (a-variable 'x)
				)
		     )
		     (a-sum (a-product (a-constant 3)
				       (a-variable 'x)
			    )
			    (a-constant -5)
		     )
	      )
)
