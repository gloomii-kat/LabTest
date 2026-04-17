#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''

    #Read first line in file, remove whitspace and split into individual column headings
    headings = f.readline().strip().split(",")

    #loop through headings and assign index positions to the required columns
    for i, head in enumerate(headings):
        if head == "Student Number": 
            num_col=i
        elif head == "Mark" : 
            mark_col = i
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''

    best =  0
    best_idx = None

    #read through the remaining lines
    for line in f:
        data = line.strip().split(",")

        #extract mark data and convert into integer
        mark = int(data[mark_col])

        #Compare the current mark with the best mark so far and update both the mark and student number if higher
        if mark > best:
            best = mark
            best_idx = data[num_col]
    return best_idx, best

def main():
    f = open(sys.argv[1])
    num_col, mark_col = getCols(f)
    best_idx, best = findTop(f,num_col,mark_col)
    print("The top student was student %s with %d"%(best_idx,best))
    f.close()

if __name__ == "__main__":
    main()
