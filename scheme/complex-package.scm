;;
;;  The package requires the complex number ADT:

(load "complex.scm")	;; this will load *other* 'packages'

;;

(define (+c a b)
  (a-complex-from-rectangular (+ (real a) (real b))
                              (+ (imag a) (imag b))
  )
)

(define (-c a b)
  (a-complex-from-rectangular (- (real a) (real b))
			      (- (imag a) (imag b))
  )
)

(define (*c a b)
  (a-complex-from-polar (* (mag a) (mag b))
                        (+ (angle a) (angle b))
  )
)

(define (/c a b)
  (a-complex-from-polar (/ (mag a) (mag b))
		        (- (angle a) (angle b))
  )
)

