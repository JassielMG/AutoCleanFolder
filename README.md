# AutoCleanFolder
#### * This is a small project to keep clean periodicatly an specifict folder in my system
#### * I did use some librarys python natives so to execute this project in your system doens´t need install more dependeces


# Instrutions

``` bash
# Download Porject
git clone https://github.com/JassielMG/AutoCleanFolder.git
 ```

``` bash
# To execute the programa we need parser 2 arguments 
# 1.- dir_path: path of the folder that we keeping clean (str)
# 2.- period: the number of days old (int) that the files can be in that folder. 

# Example:

python3 main.py --dir_path="path/to_folder" --period=5

# this command executes the script and will delete all the files and directories in the path older than 5 days
```

``` bash
# We can use this script to run periodically as a job, for this we use contrab

# use
contrab -e

# and add this line
00 15 * * 5 cd /Users/rjmontes/Projects/AutoCleanFolder && python3 main.py --dir_path="yourPath/Downloads" --period=15 

# This scripting will do is delete all the files in the downloads folder older than 15 days


```
