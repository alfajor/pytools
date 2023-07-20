# py-dojo: katas - assorted challenges & algorithms
import math
from urllib.parse import urlparse

# return remaining passenger count at last bus stop
def passenger_count(bus_stops):
    start = []
    end = []
    for s in bus_stops:
        boarding = s[0]
        departing = s[1]
        start.append(boarding)
        end.append(departing)
    
    total_boarding = sum(start)
    total_departing = sum(end)
    diff = (total_boarding - total_departing)

    print(diff)
    return diff
    
#passenger_count([[10,0], [3,5], [5,8]])

# return len of shortest word in sentence
def shortest_word(words):
   word_size = [len(w) for w in words.split()]
   shorty = min(word_size)

   print(shorty)
   return shorty

#shortest_word('This is a sentence with lots and lots and lots of words')

# find unique number in list
def find_unique(numbers):  
    for n in numbers:
        if numbers.count(n) == 1:
            print(n)
            return n
        
#find_unique([3, 10, 3, 3, 3])

# return prime-ness of number - bool - handle 0 or negative numbers
def is_prime(num):
    # > 1 and no positive divisors besides itself & 1
    if num <= 1:
        print(f'{num} is not prime')
        return False
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            print(f'{num} is not prime')
            return False
        
    print(f'{num} is prime')
    return True

#is_prime(409)

# remove uppercase chars and add break
def break_camel_case(word):
    camel_break = ''.join(' ' + w if w.isupper() else w.strip() for w in word).strip()
    print(camel_break)   
    return camel_break 

#break_camel_case('helloWorldYea')

# multiplicative persistence - return count of times to multiply digit to get to a single digit
def persistance(num):
    base = 10 
    while num < base:
        return 0 

    int_str = str(num)
    product = 1
    for n in int_str:
        product *= int(n)

    print(persistance(product) + 1)
    return persistance(product) + 1

#persistance(999)

# return domain name from any complete URL - google.com
def domain_name(url):
    parsed = urlparse(url)
    full_domain = parsed.netloc

    def splitter(str, tld):
        return str.split(f'.{tld}')[0]
    
    if parsed.scheme == '':
        if 'www' in parsed.path:
            domain = url.split('.')[1]
            print(domain)
            return domain
        else: 
            domain = url.split('.')[0]
            print(domain)
            return domain

    elif 'http' not in url:
        part = parsed.path.split('/')[0]
        
        tld = part.split('.')[2]
        final = part.split('www.')[1]

        domain = splitter(final, tld)
        print(domain)
        return domain

    elif 'http' and 'www' in url:
         domain = full_domain.split('.')[1]
         print(domain)
         return domain

    else:
        tld = full_domain.split('.')[1]
        domain = splitter(full_domain, tld)
        print(domain)
        return domain

# domain_name('www.icann.org/something/something')

# return array of nums in phone# format, i.e (123) 456-7890
def phone_number(nums):
    first_digits = [n for n in nums[:3]]
    remaining_digits = [n for n in nums[3:]]

    area_code = f"({''.join(str(s) for s in first_digits)})"

    first = ''.join(str(d) for d in remaining_digits[:3])
    last = ''.join(str(d) for d in remaining_digits[3:])

    full_number = f'{area_code} {first}-{last}'

    print(full_number)
    return full_number

#phone_number([1,2,3,4,5,6,7,8,9,0])

# return hashtag of str  
def hashtag_maker(words):
    if len(words) > 140 or words == '':
        return False
    
    tag = f"#{''.join(w[0].upper() + w[1:].lower() for w in words.split())}"

    print(tag)
    return tag

hashtag_maker('hAshtags arE so lamE')