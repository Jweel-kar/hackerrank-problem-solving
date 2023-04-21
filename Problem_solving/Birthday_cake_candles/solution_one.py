def birthdayCakeCandles(candles):
    # Write your code here
    count = 0
    max_candle = max(candles)
    for i in candles:
        if max_candle == i:
            count += 1
            
    return count
