"""
    DOC STRING
"""
# !/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest import skip
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    """
    DOC STRING
    """

    def test_cannot_add_empty_list_items(self):

        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits ENter on the empty input box

        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The home page refreshes, adn there is an error message saying

        # that list items cannot be blank

        self.wait_for(lambda: 
            self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))
        # She tries again with some text for the item, which now works

        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')

        # Perversely, She now decides to submit a second blank list item 

        self.get_item_input_box().send_keys(Keys.ENTER)

        # She receives a simlier warning on the list page

        self.wait_for(lambda: 
            self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # And She can correct it by filling some text in 

        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('2: Make tea')

        self.fail("finish this test!")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
