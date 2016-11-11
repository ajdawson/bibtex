Personal BibTeX Repository
==========================

My personal BibTeX repository.


Structure
---------

* ``bibliography.bib``: Main bibliography file
* ``*_rawdoi.bib``: Bibliography file(s) containing un-escaped DOI fields
* ``journall.bib``: Full journal names
* ``journals.bib``: Short journal names


Programs
--------

Two programs are provided for working with the bibliography files:

* ``escdoi.py``: Escape restricted characters in DOI fields
* ``rmfield.py``: Remove selected fields from bibliography entries

Both programs accept input from file or stdin and write output to stdout
(so they can be used in pipes). For example, to escape all DOIs and produce
bibliography entries that omit the number and pages fields from the papers
and tech reports bibliographies:

.. code-block:: sh

   cat papers_rawdoi.bib techreports_rawdoi.bib | ./escdoi.py | ./rmfield.py number,pages

