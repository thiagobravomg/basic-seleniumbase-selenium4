from seleniumbase import BaseCase

class MainTests(BaseCase):

    def setUp(self):
        super().setUp()
        self.open("website_url_account")
        self.add_text("username_field", "username_value")
        self.add_text("password_field", "password_value")
        self.click("btn_login")
        self.assert_text("succes_login_value", "success_login_el")

    def tearDown(self):
        super().tearDown()
        self.open("website_url_account")
        self.click("btn_logout")
        self.assert_element_visible("btn_login")

    def test_home_page(self):
        self.open("website_url_home")
        self.assert_title("page_title")
        self.assert_element("specific_el")
        self.click("specific_link_btn")
        current_url = self.get_current_url()
        self.assert_equal(current_url, "link_test")
        self.assert_true("link_test_slice" in current_url)

    def test_menu(self):
        links_corretos = ['item1', 'item2', 'item3']
        menu_links = self.find_elements("itens_menu")
        for index,x in enumerate(menu_links):
            print(index, x.text)
            self.assertEqual(links_corretos[index],x.text)

    def contact_form(self):
        self.open("website_url_contact")
        self.scroll_to("form_el")
        self.save_screenshot("screenshot_name", "screenshot_folder")
        self.send_keys("form_field_1_el", "form_field_1_value")
        self.send_keys("form_field_2_el", "form_field_2_value")
        self.send_keys("form_field_3_el", "form_field_3_value")
        self.click("submit_link_el")
        self.assert_text("succes_value", "succes_el")

    def upload_files(self):
        self.open("website_url_upload")
        file_path = ""
        remove_hidden_class = "js_code"
        self.add_js_code(remove_hidden_class)
        self.choose_file("file_upload_el",file_path)
        self.click("file_submiel")
        self.assert_text("succes_upload_value", "succes_uplaod_el")
        