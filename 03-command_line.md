# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd: prints working directory  
hostname: my computer's network name  
cd: change directory  
mkdir: make directory  
ls: list directory  
rmdir: remove directory  
pushd: push directory - save current directory and go to whatever follows  
popd: pop directory - return to most recent pushed directory  
cp: copy a file or directory  
mv: move a file or directory  
less: page through a file  
more: shows contents of file  
cat: print the whole file  
xargs: execute arguments  
find: find files  
grep: find things inside files

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

'ls' lists the directory  
'ls -a' displays all files  
'ls -l' displays the long format listing
'ls -lh' displays the long format listing in a human-readable format  
'ls -lah' displays all files in the long format listing in a human-readable format  
'ls -t' displays the newest files first
'ls -Glp' displays long format listing files without group names and displays directories with /  


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

5 of my favorites include:  
'ls -f' which interprets each name as a directory, not a file  
'ls -m' which displays the names as a comma-seperated list  
'ls -r' which displays subdirectories as well  
'ls -1' which displays each entry on a line  
'ls -d' which displays only directories

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs executes arguments. The default command it uses is echo.  

An example of how to use xargs would be if you are attempting to find all .txt files in a specific folder (in this case, temp)  
  
    find ./temp -name "*.txt" | xargs ls  
  
This finds all files with .txt in their filename in the folder temp, and then uses xargs to list them.

 

