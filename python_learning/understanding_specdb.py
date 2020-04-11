# also need to understand spine_toolbox.py!

# purpose of specdb v8: save source id, seq, exp_type, 
# both images, fid and ser files

# noticed 6 rows in exp_type column which contain file paths
# instead of type

# noticed that the "timedomain_blob" contains BOTH fid and ser

# try different string formatting for table creation?

import sqlite3
import argparse
import sys
import re
import os
import glob
import spine_toolbox as st
import hashlib

# skipped the argparse part and defining variables

# this "maintains" the SQL look i guess, depends on preference
# uses python3's latest string formatting technique
c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (,
	{id_column} INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	{column1} {text_type},
	{column2} {text_type},
	{column3} {text_type},
	{column4} {text_type},
	{column5} {blob_type}""")

# now insert statement call
# assigns sql insert statement to "sql"
sql = f"""INSERT OR IGNORE INTO {table_name}
({column1}, {column2}, {column3}, {column4}, {column5})
VALUES(?, ?, ?, ?, ?)"""

# now make an index called index_name on the checksum
c.execute(f"""CREATE UNIQUE INDEX IF NOT EXISTS {index_name}
	ON {table_name} ({column1})""")

# so far so good, now THE LOOP
# key terms: enumerate(), split(), open() 
# enumerate(); adds a counter to an iterable, starting from 0
# split(): splits a string into a list, can specify separator in ()
# open(): used to open files in our system
# takes two arguments, name of file AND the MODE for which we want
# to open the file

# this line was way above but needed to understand what "r" does 
data = open("data.tsv", "r")

for i, x in enumerate(data):
	# splits by space, by default
	splitted = x.split()
	# if the first element of the first list (read from top to bottom, line by line) is "pst_id", continue
	# do this to skip the field names basically!
	# field names already specified above so yeah
	if splitted[0] == "pst_id":
		continue

	# to print counters with their corresponding first element of the list i.e. the pst_id
	# the two are separated by a tab space
	print(i, '', splitted[0])


	# time to grab the fid/ser blobbbb	
	# to get the tar.gz paths (archive paths)
	path = splitted[3]
	#print(path)	

	# to split archive paths by "/"
	parts = path.split('/')
	#print(parts)

	# to join the first four elements of the resulting list from archive column
	# not including the tar file itself
	upper_path = '/'.join(parts[0:5])
	#print(upper_path)

# use of glob module!
	# function: finds all pathnames matching a specified pattern according to the rules
	# used by the Unix shell, but results are returned in ARBITRARY order
	# glob treats filenames beginning with a dot as special cases
	# glob.iglob(pathname): return an iterator which yields the same values as glob()
	# without actually storing them all simultaneously

	# if recursive is true, the pattern "**" will match ANY files and zero or
	# more directories, subdirectories and symbolic links to directories
	# SUGGESTION for improvement: documentation says,
	# Using the “**” pattern in large directory trees may consume an inordinate amount of time
	files = list((glob.iglob(f'{path}**/fid', recursive=True)))
	#print(files)
	files.extend(list(glob.iglob(f'{path}**/ser', recursive=True)))
	#print(files)
	for f in files:
		#print(f)
		# b argument specifies BINARY 
		with open(f,"rb") as fh:
			fbytes = fh.read() # reads file as bytes, you can specify how many bytes (int)!
			# we want to use the md5 algorithm
			# can ask hashlib anytime to digest the concatenation of data 
			# fed to it so far using the digest() or hexdigest() methods
			readable_hash = hashlib.md5(fbytes).hexdigest()

			# need to understand spine_toolbox.py!!
			m = st.meta_data(f.replace(arg.b+'data/',''))
			if len(m) != 4:
				continue
			else:
				inserter=[readable_hash, splitted[0], splitted[-1], m[1], fbytes]
				c.execute(sql, inserter)

conn.commit()
conn.close()


# now look through spine_toolbox.py!






