# coding: utf-8

"""
    WebScraping.AI

    WebScraping.AI scraping API provides GPT-powered tools with Chromium JavaScript rendering, rotating proxies, and built-in HTML parsing.

    The version of the OpenAPI document: 3.1.3
    Contact: support@webscraping.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from webscraping_ai.models.error import Error

class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Error:
        """Test Error
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Error`
        """
        model = Error()
        if include_optional:
            return Error(
                message = '',
                status_code = 56,
                status_message = '',
                body = ''
            )
        else:
            return Error(
        )
        """

    def testError(self):
        """Test Error"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()