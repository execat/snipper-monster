#!/usr/bin/env ruby

# From: http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
# Pass the number to be determined to be prime or not, and True or False gets returned.
# Uses regexp (explanation in the above blog post)

def is_prime(n)
    ("1" * n) !~ /^1?$|^(11+?)\1+$/
end
