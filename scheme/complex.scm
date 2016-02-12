;;
;; This package uses typed values ...
;;

(load "typed-values")

;
; Selectors (real, imag, mag, angle) have to decide WHICH
;   representation is being used,and then use ITS selector...
;
(define (real c)
  (cond ((rectangular? c) (real-rect c))
        ((polar? c)       (real-polar c))
	(else (error "real: unknown complex representation -" (type-of c)))
  )
)

(define (imag c)
  (cond ((rectangular? c) (imag-rect c))
	((polar? c)	  (imag-polar c))
	(else (error "imag: unknown complex representation -" (type-of c)))
  )
)

(define (mag c)
  (cond ((polar? c)	  (mag-polar c))
	((rectangular? c) (mag-rect c))
	(else (error "mag: unknown complex representation -" (type-of c)))
  )
)

(define (angle c)
  (cond ((polar? c)	  (angle-polar c))
	((rectangular? c) (angle-rect c))
	(else (error "angle: unknown complex representation -" (type-of c)))
  )
)



;;
;; Constructors etc.
;;

(define (a-complex-from-rectangular re im)
  (a-typed-value 'rectangular (list re im)))

(define (real-rect c) (car (value-of c)))

(define (imag-rect c) (cadr (value-of c)))

(define (mag-rect c)
  (define (square x) (* x x))  		;as it's not built-in!
  (sqrt (+ (square (real-rect c))
	   (square (imag-rect c)))))

(define (angle-rect c) (atan (imag-rect c) (real-rect c)))

(define (rectangular? c) (eq? (type-of c) 'rectangular))

(define (a-complex-from-polar magnitude angle)
  (a-typed-value 'polar (list magnitude angle)))

(define (polar? c) (eq? (type-of c) 'polar))

(define (mag-polar c) (car (value-of c)))

(define (angle-polar c) (cadr (value-of c)))

(define (real-polar c) (* (mag-polar c) (cos (angle-polar c))))

(define (imag-polar c) (* (mag-polar c) (sin (angle-polar c))))

