def result_append(result:int, results:list[int]):
    if len(results) <= 0:
        results.append(result)
    else:
        for i in results:
            if i == result:
                break
            elif results.index(i) == (len(results) - 1):
                results.append(result)
                break



def main():
    a, results = [int(input()) for _ in range(10)], []
    for i in a:
        result =  i%42
        result_append(result, results)


    print(len(results))

main()