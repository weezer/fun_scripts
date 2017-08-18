def infomast(string):
    if string[0] == 'E':
        # email
        email = string[2:]
        e = "E:"
        e += email[0]
        e += "*****"
        last = email.index('@') - 1
        e += email[last:]
        return e
    
    if string[0] == 'P':
        # phone
        phone = string[2:]
        s = ""
        for i in phone:
            if i.isdigit():
                s += i
        if len(s) <= 4:
            s = '*' * len(s)
        else:
            s = '*' * (len(s)-4) + s[-4:]
 
        zip = 0
        if len(s) > 10: # zip code
            zip = len(s) - 10
 
        # deal with space and parentheses
        count = -1
        i = 0
        while i < len(phone):
            if phone[i] == '+':
                i += 1
            elif phone[i] == ' ' or phone[i] == '(' or phone[i] == ')' or phone[i] == '-':
                while phone[i] == ' ' or phone[i] == '(' or phone[i] == ')' or phone[i] == '-':
                    i += 1
                if count != -1:
                    s = s[:count+1] + '-' + s[count+1:]
                else: # if symbol appears at beginning, do not add 1 to count
                    continue
                count += 1
            else:
                count += 1
                i += 1
 
        if zip != 0 and s[zip] != '-':
            s = s[:zip+1] + '-' + s[zip+1:]
 
        if phone[0] == '+':
            s = '+' + s
        return 'P:' + s

print infomast("E:a@gmai.com")
import sys
lst = sys.stdin.read().splitlines()
for i in lst:
    print infomast(i)