def main():
    
    print("How many numbers you want to print: ")
    number = input()
    counter(0, int(number))
    
def counter(start, number):
        while start <= number:
                print(start)
                start += 1

if __name__ == "__main__":
        main()
