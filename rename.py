##This script is used to rename the 
import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),'constants.ini'))
path = str(config['path']['indian_stock_data'])


# Function to rename multiple files
def main():
    i = 0
    global path
    for filename in os.listdir(path):
        print(path)
        filename_new = filename.split("_")[0]
        source = path+'/'+filename
        dest = path+'/'+filename_new+'.csv'
        ##Rename the files
        os.rename(source, dest)
# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()