from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # user opens browser and navigates to URL
    self.browser.get('http://localhost:8000')

    # user notices the page titles
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # user is invited to enter a todo item
    inputbox = self.browser.find_element_by_id('new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item',
    )

    # user types 'Buy penicls' into the text box
    inputbox.send_keys('Buy pencils')

    # user hits enter and page updates
    inputbox.send_keys(Keys.ENTER)

    table = self.browser.find_element_by_id('list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
      any(row.text == '1: Buy pencils' for row in rows),
      "New to-do item did not appear in the table"
    )

    # Finish test indication
    self.fail('Finish the test!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')