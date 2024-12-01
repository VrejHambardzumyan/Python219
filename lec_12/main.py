import time

def TimeDecorator(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(f"Working time: {endTime - startTime} ")
        return result
    return wrapper

def fileGenerator(filePath):
    with open(filePath, 'r') as file:
        for line in file:
            yield line.strip()

@TimeDecorator
def processFile(filePath):
    with open(filePath, 'r') as f:
        lines = f.readlines()
        processedLines = []
        
        for line in lines:
            numbers = list(map(int, line.split()))
            filteredNumbers = list(filter(lambda x: x > 40, numbers))
            processedLines.append(' '.join(map(str, filteredNumbers)))
        
        with open(filePath, 'w') as f:
            for line in processedLines:
                f.write(line + '\n')

def readWithGenerator(filePath):
    for line in fileGenerator(filePath):
        print(line)

if __name__ == "__main__":
    filePath = 'numbers.txt' 
    
    processFile(filePath)
    print("\nReading file using generator:")
    readWithGenerator(filePath)
