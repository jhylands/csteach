;;
;;  Simple typed-value ADT
;;

(define (a-typed-value type value)
  (cons type value)
)

(define (type-of x) (car x))

(define (value-of x) (cdr x))
