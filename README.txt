----- Description ----------------------------------------------------------

Homebrew github repository for the control of a cluster computer home lab.

----------------------------------------------------------------------------
Files in repository:
----------------------------------------------------------------------------
1) rmn_test.py
    Python script for training an ADAM optimized machine learning model, with the MINST dataset.
        - Requires python TensorFlow libraries. --> Works well with Nvidia CUDA tools should your lab be equipped with GPUs

2) gitUpdate.py
    Python script to update to the latest version of the repository. Copys the current branch to ~/pyPiperOld/ then deletes the current build and 
    retrieves the latest github repository.
    !! This should be replaced with a shell script later !!

3) TensorFlow_ARM.txt
    A small file for instructions on how to deploy the Python3 TensorFlow 2.0 Library for ARM processors.
    Originally intended for the Raspberry Pi (developed on a Pi 3B v1.2) to make a low cost prototype cluster.


----------------------------------------------------------------------------
Notes:
----------------------------------------------------------------------------
The main purpose of this repository is for a more simple deployment method for pushing new scripts and files to a home lab cluster.

Much of the development is done in Python3 for deployment on a cluster of networked Raspberry Pis. This is a low cost prototype for a larger, more complex 
    cluster of more powerful hardware. More scripts will be branched in at a later date for deployment on the full cluster.