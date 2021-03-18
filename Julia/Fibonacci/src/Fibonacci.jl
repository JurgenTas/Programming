module Fibonacci

export itfib, mfib

function itfib(n::Int64)
    x, y = BigInt(0), BigInt(1)
    for i = 1:n
        x, y = y, x + y
    end
    return x
end

const b = [BigInt(1) 1; 1 0]

function mfib(n::Int64)
    if n == 0
        return 0
    elseif n == 1
        return 1
    else
        return (b^(n+1))[2, 2]
    end
end

end # module

