def birthdayCakeCandles(candles):
    # Write your code here
    tallest_candle = candles[0]
    candles_count = 0
    
    for i in candles:
        if i > tallest_candle:
            tallest_candle = i
            
    for i in candles:
        if i == tallest_candle:
            candles_count += 1
            
    return candles_count
