#assignment 3 :# sentance (string) is pangram or not.

def pangram(st):
    li = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in li:
        if i not in st:
            return False 
    return True
            
string = 'the quick brown, fox jumps over the lazy dog!'
print (pangram(string))