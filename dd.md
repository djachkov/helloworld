# Developing progress notes

## Day 1.

So here I decided to make my own little project and write down the process

Spend a lot of time fixing poetry installation. For some reason, it stuck with using python 3.9.13 instead of the provided by the pyenv latest 3.11.1 version.
Reinstalling the latest version of poetry seems to help with the issue and I'm able to finally add the first project dependencies.

I'm planning to use MongoDB as a database and I want to try their async driver with the project.

Prepare Dockerfile for future deployment

## Day 2

Everything works perfect, except...
```
 4.0K    ./main.py
 598MB - the size of the docker image
```
Almost 600MB for the one 4KB file? It definitely could be less.  
Reduced docker image size x2 by using multistage build
```
277MB - much better
```

Time to finally push this stuff and begin to write some code