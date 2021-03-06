"""
    DOC STRING
"""
# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import unittest
import time

# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


MAX_WAIT = 2


class FunctionalTest(StaticLiveServerTestCase):
    """
    Something Special Doc String
    """

    def setUp(self):
        self.browser = webdriver.Chrome()
        staging_server = os.environ.get('STATING_SERVER')
        if staging_server:
            self.live_server_url = "http://" + staging_server

    def tearDown(self):
        self.browser.quit()

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def check_for_row_in_list_table(self, row_text):
        """
        Doc String
        """
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def wait_for(self, fn):

        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for_row_in_list_table(self, row_text):
        """
        Doc String
        """

        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
