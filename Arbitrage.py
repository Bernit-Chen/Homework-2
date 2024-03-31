liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def getReserves(tokenIn,tokenOut) :
    if ((tokenIn,tokenOut) in liquidity) :
        percentage=liquidity[(tokenIn,tokenOut)]
        return percentage
    else :
        (pright,pleft)=liquidity[(tokenOut,tokenIn)]
        return (pleft,pright)

def getAmountOut(amountIn,reserveIn,reserveOut):
        if (amountIn<=0 and reserveIn<=0 and reserveOut<=0): return
        amountInWithFee = amountIn*997
        numerator = amountInWithFee*reserveOut
        denominator = (reserveIn*1000)+amountInWithFee
        amountOut = numerator / denominator
        return amountOut

def getAmountsOut(amountIn,path):
    if (len(path)<2): return
    amounts = []
    amounts.append(amountIn)
    out_string="path: "+path[0]
    for i in range(0,len(path)-1) :
        out_string=out_string+"->"+path[i+1]
        (reserveIn,reserveOut)=getReserves(path[i], path[i + 1])
        amounts.append(getAmountOut(amounts[i],reserveIn, reserveOut))
    out_string=out_string+", tokenB balance="+str(amounts[len(path)-1])
    return (out_string,amounts)

(out_string,ammount) = getAmountsOut(5,['tokenB','tokenA','tokenD','tokenC','tokenB'])
print(out_string)


