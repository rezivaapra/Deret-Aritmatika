class Series(object):
    def arithmetic(self, N):
        output = [2]
        for i in range(1, N):
            value = output[i-1] + 3
            output.append(value)
        return output

def main():
    n = int(input('Input: '))
    print('Output:', ",".join(map(str, Series().arithmetic(n))))

if __name__ == '__main__':
    main()