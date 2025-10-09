import csv

def search_ai_in_names(csv_file1):
    result = []
    file1 = open(csv_file1, 'r', newline='')
    reader = csv.reader(file1)
    # for row_idx, row in enumerate(reader, start=1):
    #     for col_idx, cell in enumerate(row, start=1):
    #         if 'ai' in cell.lower():
    #             result.append((row_idx, col_idx))
    for row_idx, row in enumerate(reader, start=1):
        cell = row[0]  
        if 'ai' in cell.lower():
            result.append((row_idx, 1))  

    file1.close()
    return result


if __name__ == "__main__":
    # file1name = 'students.csv'
    matches = search_ai_in_names('students.csv')
    print("Cells containing 'ai':", matches)
