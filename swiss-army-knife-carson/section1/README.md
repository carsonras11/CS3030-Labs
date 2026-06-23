Section 1

The sentinel script checks if a particular directory exists
and will let you know by saying success or error. and then
since we copied it into the bin and added the correct path
we are able to run it out of any forlder not just the 
original.

ls - I used this a ton throughout this entire assignment
to check that everything was in the right place and what
was in each folder itself.

cd - i like that just typing it in itself sends you back 
to the previous directory. also nice when you are trying to
change into a directory that is a few folders deep so you
can get to the exact one you want.

chmod - this one took me a second to understand how to 
change permissions correctly and making scripts executable. 

to make a vm inside section1 you need to run

python3 -m venv .venv    

then run this in order to activate it

source .venv/bin/activate

you will see the .venv at the beginning of the your line 
and then from there you you need to install dependencies 
which makes things just more universal and uniform.
