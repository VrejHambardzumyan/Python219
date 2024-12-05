import os
import time
import threading
from multiprocessing import Process, Manager
from collections import Counter


def generateTextFileile(filename, lines=100000, wordPerLine=10):
    import random
    import string
    with open(filename, "w") as file:
        for _ in range(lines):
            line = " ".join(
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))) 
                for _ in range(wordPerLine)
            )
            file.write(line + "\n")


def countWordsSequential(filename):
    wordCount = Counter()
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            wordCount.update(words)
    return wordCount


def threadWorker(lines, resDict, lock):
    wordCount = Counter()
    for line in lines:
        words = line.strip().split()
        wordCount.update(words)
    
    
    with lock:
        for word, count in wordCount.items():
            resDict[word] = resDict.get(word, 0) + count


def countWordsMultithreading(filename, numThreads=4):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    chunkSize = len(lines) // numThreads
    threads = []
    lock = threading.Lock()
    resDict = {}
    
    for i in range(numThreads):
        chunk = lines[i * chunkSize : (i + 1) * chunkSize]
        thread = threading.Thread(target=threadWorker, args=(chunk, resDict, lock))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return resDict


def processWorker(lines, resQueue):
    wordCount = Counter()
    for line in lines:
        words = line.strip().split()
        wordCount.update(words)
    resQueue.put(dict(wordCount))


def countWordsMultiprocessing(filename, numProcesses=4):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    chunkSize = len(lines) // numProcesses
    processes = []
    manager = Manager()
    resQueue = manager.Queue()
    
    for i in range(numProcesses):
        chunk = lines[i * chunkSize : (i + 1) * chunkSize]
        process = Process(target=processWorker, args=(chunk, resQueue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
   
    finalWordCount = Counter()
    while not resQueue.empty():
        finalWordCount.update(resQueue.get())
    
    return finalWordCount


def compareApproaches(filename):
    print(f"Processing file: {filename}")

  
    startTime = time.time()
    seqResult = countWordsSequential(filename)
    seqTime = time.time() - startTime
    print(f"Sequential time: {seqTime:.2f} seconds")

   
    startTime = time.time()
    threadResult = countWordsMultithreading(filename)
    threadTime = time.time() - startTime
    print(f"Multithreading time: {threadTime:.2f} seconds")

   
    startTime = time.time()
    processResult = countWordsMultiprocessing(filename)
    processTime = time.time() - startTime
    print(f"Multiprocessing time: {processTime:.2f} seconds")

    
    threadSpeedup = seqTime / threadTime if threadTime > 0 else float("inf")
    processSpeedup = seqTime / processTime if processTime > 0 else float("inf")
    
    print(f"\nSpeedup (Multithreading): {threadSpeedup:.2f}x")
    print(f"Speedup (Multiprocessing): {processSpeedup:.2f}x")

    
    assert seqResult == threadResult, "Mismatch in multithreading results"
    assert seqResult == processResult, "Mismatch in multiprocessing results "
    print("\n All approaches produced the same word counts")

if __name__ == "__main__":
    filename = "textFile.txt"
    if not os.path.exists(filename):
        print("Generating large text file")
        generateTextFileile(filename, lines=100000, wordPerLine=10)
    
    compareApproaches(filename)
