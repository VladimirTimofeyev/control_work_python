def process_array(arr: list):
    result = []
    for elem in arr:
        if len(elem) <= 3:
            result.append(elem)
            
    return result


def main():
    arr = input().split(" ")
    
    print(process_array(arr))
    
    
if __name__ == "__main__":
    main()
