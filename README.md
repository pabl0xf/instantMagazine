# instantMagazine
A simple script to convert pdf files in a html5 flip magazine ready to publish. There are several commercial tools with tons of options available to purchase on internet, people with skills in development can for sure figure out a way to wire up some of the existing OSS libraries and tools to get the same result, instantMagazine can do that for you without requiring any specific computer skill in the process.

# Requeriments: Linux / OSx
- `Python`: 3.x
- `Poppler-utils`: or at least be able to run pdftoppm and pdfinfo commands

# Requeriments: Windows
An all in one binary generate by pyinstaller can be obtain here. Unzip the files and run instantmagazine.exe

# Setup from source and usage:
```bash
$ python setup.py install
$ python instantmagazine
```

# TODO
- `Select scale`: use an smaller or bigger resolution to generate the source images.
- `Choose beetween different libraries`: the script is using wowbook with some tweaks as a viewer library. There are some project that may have some advantages, ideally the user will be able to use the default library or choose between a few options.
- `Customize controls`: the control bar where the final user can navigate through the magazine is always fix on top. Allow the user select the position and maybe disable/enable options and change colors/styles will be nice to have.
