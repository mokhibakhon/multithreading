import multiprocessing
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"Data written to {file_path}")

def main():
    file_path1 = 'data/file1.txt'
    file_path2 = 'data/file2.txt'
    file_path3 = 'data/file3.txt'
    file_path4 = 'data/file4.txt'
    file_path5 = 'data/file5.txt'
    file_path6 = 'data/file6.txt'
    file_path7 = 'data/file7.txt'
    file_path8 = 'data/file8.txt'

    data1 = 'python!'
    data2 = 'Java!'
    data3 = 'c!'
    data4 = 'c ++ !'
    data5 = 'c#!'
    data6 = 'javaScript'
    data7 = 'php'
    data8 = 'delphi'

    # Create processes
    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_path3, data3))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_path4, data4))
    process5 = multiprocessing.Process(target=write_to_file, args=(file_path5, data5))
    process6 = multiprocessing.Process(target=write_to_file, args=(file_path6, data6))
    process7 = multiprocessing.Process(target=write_to_file, args=(file_path7, data7))
    process8 = multiprocessing.Process(target=write_to_file, args=(file_path8, data8))


    # Start processes
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    main()