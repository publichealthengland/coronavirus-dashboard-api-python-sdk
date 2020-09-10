Timestamps
..........

There are two options to get the timestamp for the last update:

- Using the ``.last_update`` property.
- Using the ``.get_release_timestamp()`` (static) method.

.. note::

    The timestamp produced by the ``.last_update`` property is not the
    same as the which is produced by the ``.get_release_timestamp()`` method. The former
    supplies the API timestamp - i.e. the time at which the data were deployed to the
    database - whilst the latter supplies the time at which the data were **released** to
    the API and by extension the website.

    There will always be a difference lag between
    the two timestamps as the data undergo a quality assurance process before they are
    released to the API / website.


.. note::

    The ``.last_update`` timestamp is produced if and *only* if the ``Cov19API``
    object is instantiated - i.e. when specific ``filters`` and ``structure`` parameters have
    been set. On the other hand, ``.get_release_timestamp()`` is a static method and therefore
    independent of parameters. This is because the ``.last_update`` timestamp is specific to
    a set of query metrics and is extracted from the ``HEAD`` of an API request. The
    ``.get_release_timestamp()`` method is, however, extracted from a static file which is
    generated a the precise moment when the data is released.


Latest API timestamp
~~~~~~~~~~~~~~~~~~~~

.. py:attribute:: last_update

    We use the ``.last_update`` property to extract the latest API timestamp.

.. hint::
    The :attr:`Cov19API.last_update` property only works if the the :class:`Cov19API`
    has been instantiated. This means that the timestamp produced using this property
    is associated with a specific combination of ``filters`` and ``structure``.

.. code-block:: python

    from uk_covid19 import Cov19API

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
        "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
    }

    england_only = [
        'areaType=nation',
        'areaName=England'
    ]

    # Instantiating the API object
    api = Cov19API(filters=england_only, structure=cases_and_deaths)

    # Request the API timestamp
    api_timestamp = api.last_update

    print(api_timestamp)

::

    2020-07-28T14:34:31.000000Z



Latest website timestamp
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:staticmethod:: get_release_timestamp()

    We use the ``.get_release_timestamp()`` static method to extract the latest API
    timestamp.

.. hint::

    A static method does not require instantiation of the API object. This
    means that the timestamp is independent of query metrics and filters.



.. warning::

    It may take up to 60 seconds for the data to be updated when the *release timestamp*
    (``.get_release_timestamp()``) is updated. This is because the cache must refresh before
    the new data becomes available. The **API timestamp** (``.last_update``), however, is only
    updated when the cache has been refreshed. This means that you can only be certain that
    you are receiving the most up-to-data data when the ``.last_update`` timestamp for your
    specific parameters have been updated.




.. code-block:: python

    from uk_covid19 import Cov19API


    release_timestamp = Cov19API.get_release_timestamp()

    print(release_timestamp)

::

    2020-07-28T15:00:00.431323Z

