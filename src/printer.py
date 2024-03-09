#!/usr/bin/env python3




def print_table(header,content,bottom=[],sort=-1,margin=3):
    '''
    @param header
    header is a list of header names
    @param content
    is a list of the content in the same order as the headings
    '''
    widths = [len(item)+margin for item in header]
    # loop thogh the data in the header
    for cont in content:
        for col in range(len(header)):
            cl = len(str(cont[col]))
            widths[col] = cl if cl > widths[col] else widths[col]
    ## print the header
    for i in range(len(header)):
        print(header[i],end="")

        for j in range(widths[i]-len(str(header[i]))):
            print(" ",end="")
    print("")
    ## sort content
    if sort >= 0:
        content = sorted(content, key=lambda x: x[sort],reverse=True)
    # print contetn
    for cont in content:
        for i in range(len(header)):
            print(cont[i],end=" ")

            for j in range(widths[i]-len(str(cont[i]))):
                print(" ",end="")
        print("")

    #print bottom
    for i in range(len(header)):
        print(bottom[i],end="")

        for j in range(widths[i]-len(str(bottom[i]))+1):
            print(" ",end="")
    print("")
