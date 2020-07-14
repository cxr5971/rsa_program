from random import *
import binascii



'''
Function Name: randomPrime
Parameters: None
Description: Retrieves a random prime number between 10 and 30
Returns: Returns the prime if it is prime
'''
def randomPrime():
    x = randint(10, 30)
    if checkPrime(x):
        return x
    else:
        randomPrime()


def checkPrime(a):
    if a == 2:
        return False

    elif (a % 2) == 1:
        return True

    else:
        return False


def totient(a,b):
    return (a-1)*(b-1)


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


def isCoPrime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False


def getPublicExponentRand(phi):
    x = randint(1, phi-1)

    if isCoPrime(x, phi):
        return x
    else:
        return getPublicExponentRand(phi)


def getPublicExponentIter(phi):
    for x in range(2,phi):
        if isCoPrime(phi, x):
            return x


def getD(phi, tempPhi, e, rightTop, otherX):

#if our b == 0
#if our a == 1


    if e == 0:
        if tempPhi ==1:
            return otherX

    else:
        #temp will store our remainder for the first iteration, we do phi mod e essentially
        # a / b   what's the quotient? Store in temp
        r = tempPhi // e
        x = r * e
        newX = tempPhi - x
        #remember that our new a is just our old b, and our new b is our remainder
        newE = newX
        newPhi = e


        #This stuff here, is the reverse Euclid part
        rightSideX = rightTop - (r * otherX)
        if rightSideX < 0:
            newOtherX = rightSideX % phi
        else:
            newOtherX = rightSideX
        if newE == 1:
            return newOtherX
        else:
            return getD(phi, newPhi, newE, otherX, newOtherX)


def getDStart(phi, e):
    return getD(phi, phi, e, phi, 1)


def encrypt(message, e, n):
    #cipher = [(ord(char) ** e) % n for char in message]
    cipher = []
    for char in message:
        unicodeValue = ord(char)
        finalValue = ((unicodeValue ** e) % n)
        cipher.append(finalValue)
    return cipher


def decrypt(cipherText, d, n):

    #for char in cipherText:
    #    tempChar = chr((char**d)%n)
    plaintext = [chr((char ** d) % n) for char in cipherText]
    return plaintext



if __name__ == '__main__':
    p = 17
    q = 19
    n = p * q
    print("First prime (p) = ", p)
    print("Second prime (q) = ", q)
    print("N = p*q = ", n)
    euler = totient(p, q)
    print("Here's the euler's totient phi(n) = (p-1)*(q-1) = ", euler)
    exponent = getPublicExponentRand(euler)
    print("We select a random exponent")
    d = getDStart(euler, exponent)
    print("here is the d: ", d)
    print("Public Key: (" + str(exponent) + "," + str(n) + ")")
    print("Private Key: (" + str(d) + "," + str(n) + ")")
    message = input("Please enter a message to encrypt: ")
    print("Encrypting message...")
    encrypted = encrypt(message,exponent,n)
    print(encrypted)
    print("decrypting...")
    decrypted = decrypt(encrypted,d,n)
    print(str(decrypted))

    """
    print("Enter a")
    a = input()
    print("Enter b")
    b = input()
    print(gcd(int(a), int(b)))
    """





