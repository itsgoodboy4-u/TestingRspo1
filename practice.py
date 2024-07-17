# Given a number reverse it and return
num = -1020

def reverseNum(num:int) -> int:
    assert -2**31 < num < 2**31, "Invalid range"

    is_neg = True if num < 0 else False 
    if is_neg:
        num = -1 * num

    new_num = int(str(num).rstrip("0"))
    value = 0
    while (new_num > 0):
        value = value*10 + new_num%10
        new_num = new_num//10

    if is_neg:
        return -value
    return value


# print(reverseNum(10900))

# for x in [12, -12, 120, 1200, 12001]:
#     print(reverseNum(x))

def first_unique_char(s:str)-> int:
    s = s.lower()

    for i in range(len(s)):
        i_unique = True
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                i_unique = False
                break

        if i_unique:
            return i 

    return -1     

# for s in ['Appsilon', 'Appsilon Poland', 'abcabc']:
#     print(f"Index: {first_unique_char(s=s)}")

def deFang_ip(ip:str) -> str:
    # result = ""
    # for i in ip:
    #     if i != ".":
    #         result += i 
    #     else:
    #         result += "[.]"
    # return result 

    # Alternative solution >>>
    spliteed_ip = ip.split(".")
    return "[.]".join(spliteed_ip)

# for ip in ['1.1.1.1', '127.0.0.1']:
#     print(f"{ip} defanged = {deFang_ip(ip=ip)}")


def is_Anagram(a:str, b:str) -> bool:
    if len(a) != len(b):
        return False
    a = a.lower()
    b = b.lower()
    checksum = 0
    for i in range(len(a)):
        checksum += ord(a[i]) - ord(b[i])
    return True if checksum == 0 else False

    # Alternate solution
    # return sorted(a) == sorted(b)

test_cases = [
    ('apple', 'pale'),        # Different lengths
    ('knee', 'keen'),         # Anagram
    ('listen', 'silent'),     # Anagram
    ('apple', 'app'),         # Different lengths
    ('banana', 'bananas'),    # Different lengths
    ('abcd', 'abcf'),         # Same length, different characters
    ('hello', 'world'),       # Same length, different characters
    ('test', 'test'),         # Identical words
    ('anagram', 'nagaramm'),  # Different lengths
    ('rat', 'car'),           # Same length, different characters
    ('abcd', 'dcbaa'),        # Different lengths
]

# for words in test_cases:
#     print(f"Words {words[0]} and {words[1]} are anagrams? {is_Anagram(a=words[0], b=words[1])}")
import re 

def is_palindrome(s:str) -> bool:
    # s = s.lower()
    # s = re.sub(r'[^A-Za-z0-9]', '', s)
    # for i in range(len(s)//2):
    #     if s[i] != s[len(s)-1-i]:
    #         return False
    # return True

    # Alternative solution

    clean_s = ''
    for i in s:
        if i.isalnum():
            clean_s += i
    s = clean_s.lower()
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True


# for word in ['Bob', '**Bob****', 'Appsilon', 'A man, a plan, a canal: Panama']:
#     print(f"Is {word} a palindrome? {is_palindrome(s=word)}")

def factorial(x:int) -> int:
    """Using recursion"""
    if x < 0:
        return -1
    if x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)
    
# for x in [5, 7, 10, 12, 0, -3]:
#     print(f"{x}! = {factorial(x=x)}")

