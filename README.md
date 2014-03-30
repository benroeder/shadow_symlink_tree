shadow_symlink_tree
===================
##Create shadow symlink tree and replacing characters in the filenames.
##e.g. foo.bar.txt -> foo_bar.txt


##Usage

Create a shadow tree

`shadow_symlink_tree.py /Users/foo/src/ /Users/foo/dest --force`  

and force creation of the root of the shadow tree if it does not exist

`shadow_symlink_tree.py /Users/foo/src/ /Users/foo/dest --force`  

and replace . in the filename with _
userful for making graphite read rrd files that have . in them 

**e.g. switch.port.model.rrd -> switch_port_model.rrd**
 
`shadow_symlink_tree.py /Users/foo/src/ /Users/foo/dest --rmstr=. --rpstr=_ --force --replace` 

and print lots of stuff going on

`shadow_symlink_tree.py/Users/foo/src/ /Users/foo/dest --rmstr=. --rpstr=_ --force --replace --verbose`

