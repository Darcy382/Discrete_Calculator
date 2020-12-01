def convertBases(orgBase, toBase, num):
    idx = len(num) - 1
    sum = 0
    for digit in num:
        sum += int(digit) * (orgBase ** idx)
        idx -= 1

    new_num = []
    while sum:
        new_num.append(str(sum % toBase))
        sum //= toBase

    return "".join(new_num[::-1])

def gcd(num1, num2):
    return eucleanAlgorithum(num1,num2)[1]

def eucleanAlgorithum(num1, num2, printOutput=False):
    c = 0
    d = num1
    r = num2
    table = []
    counter = 0
    while r != 0:
        c = d
        d = r
        r = c % d
        if counter == 0:
            s = 1
            t = 0
        elif counter == 1:
            s = 0
            t = 1
        else:
            s = table[-2][5] - table[-2][3] * table[-1][5]
            t = table[-2][6] - table[-2][3] * table[-1][6]
        table.append([counter, c, d, c//d, r, s, t])
        counter += 1
    gcd = table[-1][2]
    if counter == 1:
        s = 0
        t = 1
    else:
        s = table[-2][5] - table[-2][3] * table[-1][5]
        t = table[-2][6] - table[-2][3] * table[-1][6]
    table.append([counter, 0, 0, 0, 0, s, t])
    if printOutput:
        for count, c, d, q, r, s, t in table[:-1]:
            print("{}: {} = {}({}) + {}".format(count, c, d, q, r, s, t))
        print("\nGCD = {}\ns = {}\nt = {}".format(gcd, s, t))
    return table, gcd, s, t

def findInverse(num, m):
    table, gcd, s, t = eucleanAlgorithum(num, m)
    if gcd == 1: # Using the extended euclean algorithum
        return s
    else: # Brute force
        count = 1
        sum = num
        while count < m:
            if sum % m == 1:
                return count
            count += 1
            sum += num
        return "No solution less than m"

def solveCongruence(num1, num2, m):
    '''
    Equation of the form:
    num1 * x = num2 (mod m)

    >>> solveCongruence(34, 77, 89)
    52
    >>> solveCongruence(144, 4, 233)
    123
    >>> solveCongruence(200, 13, 1001)
    936
    '''
    table, gcd, s, t = eucleanAlgorithum(num1, m)
    sol = 0
    if gcd == 1: # Using the extended euclean algorithum
        return (s * num2) % m
    elif num2 % gcd == 0:
        num1a = num1 // gcd
        num2a = num2 // gcd
        m1 = m // gcd
        table, gcd, s, t = eucleanAlgorithum(num1a, m1)
        sol = (s * num2a) % m1
    else:

        target = num2 % m
        counter = 1
        sum = num1
        while sum % m != target:
            if counter >= m:
                return "No solution less than m"
            sum += num1
            counter += 1
        sol = counter
    if num1 * sol % m == num2 % m:
        return sol
    else:
        return "Algorithum Error"

def bayesTheorem(pEifF, pF, pEifnF):
    '''
    >>> bayesTheorem(0.80,0.01,0.1)
    0.07476635514018691
    '''
    pnF = 1 - pF
    return (pEifF * pF) / ((pEifF * pF) + (pEifnF * pnF))

def chineseRemainder(verbose, args):
    '''
    chineseRemainder(False, [(a1, m1), (a2, m2)...])
    >>> chineseRemainder(False, [(1, 3), (1, 4), (1, 5), (0, 7)])
    301
    >>> chineseRemainder(True, [(3, 5), (1, 7), (6, 8)])
    'm0 = 5 | z0 = 56 | y0 = 1\\nm1 = 7 | z1 = 40 | y1 = 3\\nm2 = 8 | z2 = 35 | y2 = 3\\n\\nM = 280 | X = 78'
    '''
    output = []
    N = len(args)
    A = []
    M = []
    Y = []
    Z = []
    M_prod = 1
    for a, m in args:
        A.append(a)
        M.append(m)
        M_prod *= m

    for i in range(N):
        Z.append(M_prod // M[i])
    for i in range(N):
        Y.append(findInverse(Z[i], M[i]))
    for i in range(N):
        output.append("m{} = {} | z{} = {} | y{} = {}\n".format(i, M[i], i, Z[i], i, Y[i]))
    X = sum([A[i] * Z[i] * Y[i] for i in range(N)]) % M_prod
    output.append("\nM = {} | X = {}".format(M_prod, X))
    output = "".join(output)
    return output if verbose else X

if __name__ == "__main__":
    test = False
    if test:
        import doctest
        doctest.testmod(verbose=True)
    else:
        selection = int(input("Select on the following functions to run:\n" +
                          "1) Base converter\n" +
                          "2) Euclean Algorithum\n" +
                          "3) Find Inverse\n" +
                          "4) Solve Congruence\n" +
                          "5) Bayes Theorem\n" +
                          "6) Chinese Remainder\n" +
                          "Enter number: "
                          ))
        print()
        if selection == 1:
            print("*** Convert Bases ***")
            num = input("Enter number: ")
            orgBase = int(input("Enter the number's base: "))
            nextBase = int(input("Enter base to convert to: "))
            print(convertBases(orgBase, nextBase, num))
        elif selection == 2:
            print("*** Euclean Algorithum ***")
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            eucleanAlgorithum(num1, num2, printOutput=True)
        elif selection == 3:
            print("*** Find Inverse ***\nEnter input in the form 'x mod m'")
            num = int(input("x = "))
            m = int(input("m =  "))
            print("x^-1 = {}".format(findInverse(num, m)))
        elif selection == 4:
            print("*** Solve Congruence ***\nEnter input in the form 'num1 * x = num2 (mod m)'")
            num1 = int(input("Enter num1: "))
            num2 = int(input("Enter num2: "))
            m = int(input("Enter m: "))
            print("x = {}".format(solveCongruence(num1, num2, m)))
        elif selection == 5:
            print("*** Bayes Theorem ***")
            f = input("F = ")
            e = input("E = ")
            print("The probalility that {} if {} has occured".format(f, e))
            pEifF = float(input("p({} if {}) = ".format(e, f)))
            pF = float(input("p({})".format(f)))
            pEifnF = float(input("p({} if not {})".format(e, f)))
            print(bayesTheorem(pEifF, pF, pEifnF))
        elif selection == 6:
            args = []
            print("*** Chinese Remainder Thoerm ***")
            N = int(input("Enter the amount of lines: "))
            print("Enter lines in the form 'x mod m'")
            for i in range(N):
                args.append((int(input("x{} = ".format(i))), int(input("m{} = ".format(i)))))
            print(chineseRemainder(True, args))
        else:
            print("invalid selection")
