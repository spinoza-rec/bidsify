BidsConverter - converts your (raw) data to the BIDS-format
=============================================================

.. _BIDS: http://bids.neuroimaging.io/
.. _here: http://www.jsoneditoronline.org/?id=97c57fc33cac9b65f6d010c49b5087d7.

This package offers a tool to convert your raw (f)MRI data to the
"Brain Imaging Data Structuce" (BIDS_) format. Using only a 
simple json config-file, it renames, reformats, and restructures 
your files such that it fits the BIDS naming scheme and conforms 
to file-formats specified by BIDS.

The config.json file
--------------------
The BidsConverter only needs a config.json file in which 'mappings' 
between files and file-types are specified. Additionally, this config 
file may contain some options (e.g. concerning backups, parallel processing, 
etc.). All options have sensible defaults. An example of a config.json 
file can be found here_.

Installing BidsConverter
------------------------
For now, it can only be installer from Github, by either cloning 
this repository directory or installing it using `pip`::

    $ pip install git+https://github.com/lukassnoek/BidsConverter.git@master