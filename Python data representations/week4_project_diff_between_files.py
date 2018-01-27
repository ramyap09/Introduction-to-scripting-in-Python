"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) == len(line2):
        if line1 == line2:
            return IDENTICAL
        else:
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    return i
    else:
        shortline = min(line1, line2, key=len)
        if line1[ :len(shortline)] != line2[ :len(shortline)]:
            for i in range(len(shortline)):
                if line1[i] != line2[i]:
                    return i
        else:
            return len(shortline)





def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if "\n" in line1 or "\n" in line2 or "\r" in line1 or "\r" in line2 :
        return ""
    elif idx < 0 or idx > len(min(line1,line2, key=len)):
        return ""
    else:
        x = "="*idx + "^"
        return line1 +"\n"+ x + "\n" +line2 +"\n"




def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if len(lines1) == len(lines2):
        if lines1 == lines2 :
            return (IDENTICAL, IDENTICAL)
        else:
            for i in range(len(lines1)):
                idx = singleline_diff(lines1[i], lines2[i])
                if idx != IDENTICAL:
                    return (i, idx)
    else:
        shortlist = min(lines1, lines2, key = len)
        if lines1[ :len(shortlist)] != lines2[ : len(shortlist)]:
            for i in range(len(shortlist)):
                idx = singleline_diff(lines1[i], lines2[i])
                if idx != IDENTICAL :
                    return (i, idx)
        else:
            return (len(shortlist), 0)




def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    filehandle = open(filename, "rt")
    filelist = filehandle.readlines()
    lst = [item.rstrip() for item in filelist]
    #print(lst)
    filehandle.close()
    return lst




def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lst1 = get_file_lines(filename1)
    lst2 = get_file_lines(filename2)
    if lst1 == lst2:
        return "No differences\n"
    else:
        diff_tuple = multiline_diff(lst1, lst2)
        diff_format = singleline_diff_format(lst1[diff_tuple[0]] if diff_tuple[0] < len(lst1) else "", lst2[diff_tuple[0]] if diff_tuple[0]<len(lst2) else "", diff_tuple[1])
        return "Line " + str(diff_tuple[0]) + ":\n"+ diff_format



print(file_diff_format("a.txt", "b.txt"))
