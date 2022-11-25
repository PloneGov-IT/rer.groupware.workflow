Changelog
=========

4.0.1 (2022-11-25)
------------------

- fix problem with room copy/paste and WorkflowPolicy
  configuration
  [lucabel]

4.0.0 (2022-07-15)
------------------

- major refactoring for python 3.8 and plone 5.2.
  [reflab]


3.0.1 (2020-05-22)
------------------

- We need to allow owner to 'Modify portal content' in
  groupware_workflow, like simple_publication_workflow
  [lucabel]


3.0.0 (2017-10-11)
------------------

- Plone 5 compatibility
  [cekk]

2.2.0 (2015-03-09)
------------------

- Editors can't delete/edit folders in Areas [cekk]


2.1.1 (2014-04-18)
------------------

- EditorAdv can now delete Forum comments [cekk]


2.1.0 (2013-11-05)
------------------

- Changed placeful workflow name, because was the same of the site [andrea]
- Fixed groupware_forum_workflow. Now has only 2 states and fixed permissions [andrea]

2.0.0 (2013-06-24)
------------------

Plone 4 version

- support for z3c.autoinclude [keul]
- removed extreme management workflows definitions [andrea]
- removed "groupware_portletpage_topics_workflow" [keul]
- groupware_folders_workflow workflow moved to rer.groupware.room [keul]
- removed deprecated i18n folder for Plone domain [keul]
- added Site Aministrators role support [andrea]
- removed forum workflow (conversation and comment are kept) [keul]
- workflow registered as a local policy [keul]
- workflow for folders [keul]

1.1.1 (2012-10-03)
------------------

- Fixed forum workflow translations [andrea]

1.1.0 (2012-10-02)
------------------

* removed private and memberposting states from ploneboard workflows [andrea]

1.0.7 (2012-02-06)
------------------

* fixed groupware ploneboard workflows [andrea]

1.0.6 (2012-01-16)
------------------

* fixed Ploneboard: Approve Comment in groupware_forum_workflow [andrea]

1.0.5 (2011-12-19)
------------------

* fixed permission "View" in groupware_workflow [andrea]

1.0.4 (2011-04-05)
------------------

* set folders with groupware_workflow [andrea]

1.0.3 (2011-01-24)
------------------

* fixed XM workflows [andrea]

1.0.2 (2011-01-19)
------------------

* fixed workflows [andrea]

1.0.1 (2011-01-14)
------------------

* set initial state "published" in groupware_workflow [andrea]

1.0.0 (xxxx-xx-xx)
------------------

* Initial release
