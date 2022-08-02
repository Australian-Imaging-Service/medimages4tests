Medimage4tests
==============

Generates dummy medical images, with junk image data but realistic headers,
to test imaging handling pipelines

Installation
------------

Medimage4tests is available on PyPI so to install, simply use pip

.. code-block:: bash

    $ pip3 install medimage4tests
    
or include in your package's ``test_requires``.


Usage
-----

.. code-block:: python

    # Import medimage4tests generator functions
    from medimage4tests.dicom.dwi import siemens_skyra_dwi_sample_image

    # Return generated images in pytest fixtures (or alternative test framework)
    @pytest.fixture(scope='session')
    def siemens_skyra_dwi_dicom():
        return siemens_skyra_dwi_sample_image()
