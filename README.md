### INSTALLATION

$ python -m pip install --upgrade --user pip setuptools virtualenv

$ python -m virtualenv ~/kivy_venv

$ source ~/kivy_venv/bin/activate

$ python -m pip install kivy

$ python -m pip install kivy_examples

$ python -m pip install ffpyplayer


### NAMING CONVENTION 

For .kv files, where style will be written as it would be in a 
CSS file, just name it all lowercase with the class name of the
created app, removing the word "App" if it is contained in it.

For instance, if the class name of the app is MyApp, create a 
"my.kv" file, for "MyFavApp", "myfav.kv"