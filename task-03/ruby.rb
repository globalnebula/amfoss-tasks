def is_prime(num)
    return false if num <= 1
    return true if num <= 3
    return false if (num % 2 == 0) || (num % 3 == 0)
    i = 5
    while i * i <= num
      return false if (num % i == 0) || (num % (i + 2) == 0)
      i += 6
    end
    true
  end

  print "Enter a number: "
  n = gets.chomp.to_i
  puts "Prime numbers up to #{n} are:"
  (2..n).each do |i|
    puts i if is_prime(i)
  end
