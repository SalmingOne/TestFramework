import allure

from pages.contacts_page import ContactsPage


class TestContactsPage:

    @allure.title("Проверка содержания страницы Контакты")
    def test_view_contacts_page(self, driver, open_site):
        contacts_page = ContactsPage(driver)
        contacts_page.go_to_page()
        title, description_1, description_2 = contacts_page.get_text_on_page()
        assert title == 'контакты', "Неправильное название секции"
        assert description_1 == 'Остались вопросы?\nОставьте заявку\nна консультацию', ('Неверный текст первой части '
                                                                                        'описания')
        assert description_2 == 'или свяжитесь любым удобным способом', 'Неверный текст второй части описания'
