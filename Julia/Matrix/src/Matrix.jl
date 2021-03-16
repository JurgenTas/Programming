module Matrix
using LinearAlgebra

export lu_solve!, lu_ijk!

"""
Solve Ax = b using LU factorization of A
"""
function lu_solve!(a::LinearAlgebra.Matrix, b::Vector)
    n, m = size(a)
    @assert n == m "only square matrix!"
    lu_ijk!(a, n) #LU factorization
    y = solve_forward(a, b, n)
    return solve_backward(a, y, n)
end # function

"""
LU factorization of a Matrix (in the ijk version)
"""
function lu_ijk!(a::LinearAlgebra.Matrix, n::Int64)
    for i = 1:n
        for j = 2:i
            @assert a[j-1, j-1] != 0 "non-zero diagonal element!"
            a[i, j-1] = a[i, j-1] / a[j-1, j-1]
            for k = 1:j-1
                a[i, j] = a[i, j] - a[i, k] * a[k, j]
            end
        end
        for k = 1:i-1
            for j = i+1:n
                a[i, j] = a[i, j] - a[i, k] * a[k, j]
            end
        end
    end
    return a
end # function

"""
Forward solve: solve Ly = b
"""
function solve_forward(a::LinearAlgebra.Matrix, b::Vector, n::Int64)
    y = zeros(n)
    for i = 1:n #solve Ly = b
        y[i] = b[i]
        for j = 1:(i-1)
            y[i] -= a[i, j] * y[j]
        end
    end
    return y
end # function

"""
Backward solve: Ux = y
"""
function solve_backward(a::LinearAlgebra.Matrix, y::Vector, n::Int64)
    x = zeros(n)
    for i = n:-1:1 #solve Ux = y
        x[i] = y[i]
        for j = i+1:n
            x[i] -= a[i, j] * x[j]
        end
        x[i] /= a[i, i]
    end
    return x
end # function

end # module
