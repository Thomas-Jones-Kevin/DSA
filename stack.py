#Stack exp evaluation

#infix to prefix
def infix_to_postfix(s):
    stack = []
    ans = ""
    prior = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    for i in s:
        if i.isalpha():  # operand
            ans += i

        elif i == '(':
            stack.append(i)

        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()  # remove '('

        else:  # operator
            while stack and prior.get(i, 0) <= prior.get(stack[-1], 0):
                ans += stack.pop()
            stack.append(i)

        # while stack:
        #     ans += stack.pop()

    return ans

i = infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i")
print("The exp :",i)

#infix to prefix
def infix_to_prefix(s):
    stack = []
    ans = ""
    prior = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    
    # Reverse and swap brackets
    rev_s = s[::-1]
    crt_rev = ""
    for i in rev_s:
        if i == '(':
            crt_rev += ')'
        elif i == ')':
            crt_rev += '('
        else:
            crt_rev += i

    # Convert to postfix of reversed
    for i in crt_rev:
        if i.isalpha():  # operand
            ans += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()  # remove '('
        else:  # operator
            while stack and prior.get(i, 0) < prior.get(stack[-1], 0):  # use < for right-associativity of ^
                ans += stack.pop()
            stack.append(i)

    while stack:
        ans += stack.pop()

    return ans[::-1]  # reverse to get final prefix

# Test
i2 = infix_to_prefix("a+b*(c^d-e)^(f+g*h)-i")
print(i2)  # Expected: -+a*b^-^cde+f*ghi

#postfix to infix
def postToInfix(postfix):
    stack = []
    for i in postfix:
        if i.isalpha():  
            stack.append(i)
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            exp = '(' + t2 + i + t1 + ')'  
            stack.append(exp)
    return stack[-1]

#prefix to infix
def preToInfix(pre_exp):
        # Code here
        s = pre_exp
        stack = []
        for i in range(len(pre_exp)-1,-1,-1):
            if s[i].isalpha():
                stack.append(s[i])
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                exp = '('+t1+s[i]+t2+')'
                stack.append(exp)
        return stack[-1]

#prefix to postfix
def preToPost(self, pre_exp):
        # Code here
        s = pre_exp
        stack = []
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                stack.append(s[i])
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                exp = t1+t2+s[i]
                stack.append(exp)
        return stack[-1]

#postfix to prefix
def postToPre(self, post_exp):
        # Code here
        s = post_exp
        stack = []
        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                exp = i+t2+t1
                stack.append(exp)
        return stack[-1]



