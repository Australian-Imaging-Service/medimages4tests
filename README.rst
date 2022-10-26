Medimages4tests
===============

.. image:: https://github.com/australian-imaging-service/medimages4tests/actions/workflows/test.yml/badge.svg
   :target: https://github.com/australian-imaging-service/medimages4tests/actions/workflows/test.yml
.. image:: https://codecov.io/gh/australian-imaging-service/medimages4tests/branch/main/graph/badge.svg?token=UIS0OGPST7
   :target: https://codecov.io/gh/australian-imaging-service/medimages4tests
.. image:: https://img.shields.io/pypi/pyversions/medimages4tests.svg
   :target: https://pypi.python.org/pypi/medimages4tests/
   :alt: Supported Python versions
.. image:: https://img.shields.io/pypi/v/medimages4tests.svg
   :target: https://pypi.python.org/pypi/medimages4tests/
   :alt: Latest Version

Generates dummy medical images, with junk image data but realistic headers,
to test imaging handling pipelines

Installation
------------

Medimage4tests is available on PyPI so to install, simply use pip

.. code-block:: bash

    $ pip3 install medimages4tests
    
or include in your package's ``test_requires``.


Usage
-----

Create a pytest fixture consisting of a dummy image with field-map metadata in DICOM format

.. code-block:: python

    # Import medimages4tests generator functions
    from medimages4tests.dummy.dicom.mri.fmap.ge.discovery_mr888.dv26_0_r05_2008a import get_image

    # Return generated images in pytest fixtures (or alternative test framework)
    @pytest.fixture()
    def ge_dicom_fmap():
        return get_image()

Create a dummy NIfTI image

.. code-block:: python

    import numpy
    # Import `get_image` function
    from medimages4tests.dummy.nifti import get_image

    # Create dummy nifti image of 10x10x10 containing all ones
    @pytest.fixture()
    def ones_nifti():
        return get_image(
            data=numpy.ones((10, 10, 10))
        )
        
 Access real T1-weighted from OpenNeuro.org

.. code-block:: python


    from medimages4tests.mri.neuro.t1w import get_image

    @pytest.fixture()
    def ones_nifti():
        return get_image(sample="ds004130-ON01016")
