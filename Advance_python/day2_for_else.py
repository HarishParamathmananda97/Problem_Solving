
def main():
    print("this is harish.")
    setting_name = 'harish'

if __name__ == '__main__':
    main()
    # using for_else statement
    
    # items = [2, 26, 35, 9]
    # divisor = 12

    # for item in items:
    #     if item % divisor == 0:
    #         found = item
    #         break
    # else: #nobreak
    #     items.append(divisor)
    #     found = divisor
    
    # # print(f"{items} contains {found} which is a mulitple of d{divisor}")
    # print("{items} contains {found} which is a multiple of the {divisor}".format(**locals()))

    # "overriding for...else code"
    def ensure_has_divisible(items, divisor):
        for item in items:
            if item % divisor == 0:
                return item
            items.append(divisor)
            return divisor
    items = [2, 25, 9]
    divisor = 12

    divident = ensure_has_divisible(items, divisor)
    print("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))