# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    },
    entry_points='''
        [ckan.plugins]
        nadit=ckanext.nadit.plugin:NaditPlugin
        nadit_ckan_harvester=ckanext.nadit.harvesters.ckan_nadit_harvester:NaditCKANHarvester
    '''
)
