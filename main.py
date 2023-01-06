import os
import datetime
import argparse
import sys
import shutil
def run():
    parser = argparse.ArgumentParser(description="Delete files each period of time")
    parser.add_argument("--dir_path", type=str, help="Path to the folder")
    parser.add_argument("--period", type=int, help="Period of time in days")
    args = parser.parse_args()
    print(sys.stdout.write(str(delete_old_files(args))))


def delete_old_files(args):
    # get the current time
    print("Files to delete:")
    now = datetime.datetime.now()
    try:
        files = os.listdir(args.dir_path)
    except FileNotFoundError:
        print("The directory does not exist or is empty")
        return

    # loop through all the files in the directory
    for file_name in os.listdir(args.dir_path):
        # get the full path of the file
        file_path = os.path.join(args.dir_path, file_name)
        # get the modification time of the file
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

        # calculate the difference between the modification time and the current time
        diff = now - mtime
        
        # if the difference is greater than the period of time, delete the file
        if diff.seconds > args.period:
            # delete the file
            # give permission of root to delete the file
            os.chmod(file_path, 0o777)

            try:
                shutil.rmtree(file_path)
            except NotADirectoryError:
                os.remove(file_path)

            print("- ",file_name)

    if args.period > 1:
        print("The function to deleted files each {} days has been executed successfully!".format(args.period))
    else:
        print("Files has been deleted successfully!")

if __name__ == "__main__":
    run()
