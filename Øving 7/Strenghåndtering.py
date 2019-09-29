#a
def check_equal(str1, str2):
    lst1 = list(str1)
    lst2 = list(str2)
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if str1[i] != str2[i]:
            return False
    return True

#b
def reversed_word(str1):
    lst = list(str1)
    print(lst)
    reversed_lst = []
    for i in range(0, len(lst)):
        reversed_lst.append(lst[(len(lst)-1)-i])
    ut = ''.join(reversed_lst)
    return ut

#c
def check_palindrome(str1):
    return check_equal(str1, reversed_word(str1))

#d
def contains_string(str1, str2):
    if str2 in str1:
        lst = list(str1)
        lst2 = list(str2)
        word = []
        for i in range(0, len(lst)-(len(lst2)-1)):
            if lst[i] != str2[0]:
                continue
            for j in range(i, len(str2)+i):
                word.append(lst[j])
                print(word)
            word = ''.join(word)
            if word == str2:
                return i
            word = []
    return -1

str1 = "agnes i senga"
str2 = "hallo"
str3 = "hallo"

print(check_equal(str1, str2))
print(check_equal(str3, str2))

print(reversed_word(str1))

print(check_palindrome(str1))

print(contains_string("pepperkake", "per"))