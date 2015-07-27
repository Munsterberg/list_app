from selenium import webdriver
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

    # user notices the page title
    self.assertIn('To-Do', self.broswer.title)
    self.fail('Finish the test!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')