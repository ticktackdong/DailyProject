from .base import FunctionTest


class LayoutAndStylingTest(FunctionTest):

    def test_layout_and_styling(self):
        self.browser.get(self.server_url)
        self.browser.set_window_size(1920, 1080)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            960,
            delta=7
        )
