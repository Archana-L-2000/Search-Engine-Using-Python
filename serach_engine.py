import os
import sys
import string


def create_index(filenames, index, file_titles):
    
    for i in filenames:
        file= open(i,'r')
         
        for line in file:
            
            line.strip()
            
            new=[k.strip(string.punctuation) for k in line.split()]
            
            for j in new:
                if(j!= ''):
                    k=j.lower()
                    if k not in index:
                        
                            index[k]= [i]
                    else:
                        if(i not in index[k]):
                            index[k].append(i)
    
    for i in filenames:
        file= open(i,'r')
    
        for line in file:
        
                l=line.strip()
            
                file_titles[i]  = l
                break
    

def search(index, query):
    
    c=0
    if(len(query.split())>1):
            l3=[]
            l1=[]
            l2=[]
            for j in index:
                if(query.split()[0] == j):
                   for k in index[j]:
                       l1.append(k)
            
            for j in index:
                for l in range(1,len(query.split())):
                        if(j==query.split()[l]):
                           for k in index[j]:
                               l2.append(k)
                               for u in l1:
                                    for y in l2:
                                                # if(len(list1)==len(list2)):
                                        if(u==y):
                                           c+=1
                                        if(u not in l3 and c==len(query.split())):
                                               l3.append(u)
            return l3     


    l3=[]
    
    for j in index:
         for l in query.split():

            if(j==l):
                for k in index[j]:
                            if(k not in l3):
                                l3.append(k)

                            
    return l3                              

def do_searches(index, file_titles):
    
    while True:
        query = input("Query (empty query to stop): ")
        query = query.lower()                   # convert query to lowercase
        if query == '':
            break
        results = search(index, query)

        # display query results
        print("Results for query '" + query + "':")
        if results:                             # check for non-empty results list
            for i in range(len(results)):
                title = file_titles[results[i]]
                print(str(i + 1) + ".  Title: " + title + ",  File: " + results[i])
        else:
            print("No results match that query.")


def textfiles_in_dir(directory):
    
    filenames = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))

    return filenames


def main():

    # Get command line arguments
    args = sys.argv[1:]

    num_args = len(args)
    if num_args < 1 or num_args > 2:
        print('Please specify directory of files to index as first argument.')
        print('Add -s to also search (otherwise, index and file titles will just be printed).')
    else:
        # args[0] should be the folder containing all the files to index/search.
        directory = args[0]
        if os.path.exists(directory):
            # Build index from files in the given directory
            files = textfiles_in_dir(directory)
            index = {}          # index is empty to start
            file_titles = {}    # mapping of file names to article titles is empty to start
            create_index(files, index, file_titles)

            # Either allow the user to search using the index, or just print the index
            if num_args == 2 and args[1] == '-s':
                do_searches(index, file_titles)
            else:
                print('Index:')
                print(index)
                print('File names -> document titles:')
                print(file_titles)
        else:
            print('Directory "' + directory + '" does not exist.')


if __name__ == '__main__':
    main()
