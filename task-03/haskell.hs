isPrime :: Integer -> Bool
isPrime 2 = True
isPrime n | n <= 1 = False
          | otherwise = all (\x -> n `mod` x /= 0) [2..isqrt n]
          where isqrt = floor . sqrt . fromIntegral

findPrimesUpToN :: Integer -> [Integer]
findPrimesUpToN n
  | n < 2 = []
  | otherwise = filter isPrime [2..n]

main :: IO ()
main = do
  putStr "Enter a number (n): "
  input <- getLine
  let n = read input :: Integer
  let primeNumbers = findPrimesUpToN n
  putStrLn $ "Prime numbers up to " ++ show n ++ ": " ++ show primeNumbers
