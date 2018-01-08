#given input word, determine if it's a palindrome

def ifPalindrome(word):
    if len(word) == 0: return True
    if len(word) == 1: return True
    else: return word[0] == word[-1] and ifPalindrome(word[1:-1])

def main():
    #print(ifPalindrome("racecar"))
    #print(ifPalindrome("tacocat"))
    #print(ifPalindrome("taccccat"))
    possible = ""
    while possible != "exit":
        possible = input("Put a word in to see if it's a Palindrome!\n")
        print(ifPalindrome(possible))


if __name__ == "__main__":
    main()
