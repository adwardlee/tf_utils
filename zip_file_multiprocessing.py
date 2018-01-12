# importing required modules
from zipfile import ZipFile
import os
from multiprocessing import Pool

split_num = 1000
 
def get_all_file_paths(directory):
 
    # initializing empty file paths list
    file_paths = []
 
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
 
    # returning all file paths
    return file_paths        
def zip_worker(names):
    with ZipFile(names[1],'w') as zip:
        for file in names[0]:
            zip.write(file)
 
def main():
    # path to folder which needs to be zipped
    directory = './python_files'
 
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
 
    # printing the list of all files to be zipped
    #print('Following files will be zipped:')
    #for file_name in file_paths:
        #print(file_name)
    file_name1 = [[] for x in xrange(int(len(file_name)/split_num))]
    zipnames = [ str(x) + 'zipfile.zip' for x in xrange(int(len(file_name)/split_num))]
    union = (file_name1,zipnames)
    function_input = ((a,b) for a,b in union)
    for i in xrange(len(file_name)):
        k = i / split_num
        file_name1[k].append(file_name[i])
    pool.map(zip_worker, function_input)
    # writing files to a zipfile
 
    print('All files zipped successfully!')        
 
if __name__ == "__main__":
    main()
