WPS Office Linux Script
=======================

.. contents::

Summary
-------
A collection of scripts that ease the installation and removal of WPS Office on Linux.  The
installation scripts also install the missing fonts that are usually missing during a normal
installation.  There are also scripts to download extra templates from online as well as to remove
those templates.

Installation
------------
**To install WPS Office on Linux:**

1) Open a terminal
2) Navigate to a directory where you wish to clone the repository
3) Clone the repo via:

   .. code-block:: bash

      $ git clone git@github.com:pchan37/wps-office-linux-scripts

4) Navigate to the root of the repository

   .. code-block:: bash

      $ cd wps-office-linux-scripts

5) Run the installation script

   .. code-block:: bash

      $ ./install_wps_office_linux.sh

   Note: During the installation, if you are on Elementary OS or have plank installed, the script
   would prompt you if you want to create launchers on the dock (icon to launch the app).

**Optional)**

1) If you installed WPS Office on Linux and you later realize you want to dock all three
   applications to the plank (Elementary OS dock), run:

   .. code-block:: bash

      $ ./add_wps_to_plank.sh

2) Download additional templates from online (note that WPS Presentations would take a while to load
   after this)

   .. code-block:: bash

      $ ./download_templates.sh

Uninstallation
^^^^^^^^^^^^^^

**IT IS HIGHLY RECOMMENDED THAT YOU DO NOT CANCEL THIS PROCESS FOR A CLEAN REMOVAL**

To uninstall WPS Office on Linux entirely, navigate to the root of this repo and run:

.. code-block:: bash

   $ ./uninstall_wps_office_linux.sh

To remove the downloaded templates, navigate to the root of this repo and run:

.. code-block:: bash

   $ ./remove_templates.sh

Usage
-----
To open an application, search up WPS in your application launcher and select the one that you wish
to open.  Alternatively, you can pin it to the dock for easier access (if you have not already done so).

Verison History
---------------

Version 0.2
^^^^^^^^^^^
- Features full support for downloading templates from online for Writer, Presentations,
  Spreadsheets
  - Offers the option of downloading specific template categories (Missing clean interface for users)
- Wrote a script for removing templates
  - Offers the option of removing specific template categories (Missing clean interface for users)
- Updated uninstallation script to remove all remanents

Version 0.1.2
^^^^^^^^^^^^^
- Features beta support for downloading templates from online

Version 0.1
^^^^^^^^^^^
- Wrote a script for installing WPS Office on Linux
  - Included the installation of missing fonts
- Wrote a script for uninstalling WPS Office on Linux
- Wrote a script for adding WPS Office shortcuts to the plank (dock in Elementary OS)
