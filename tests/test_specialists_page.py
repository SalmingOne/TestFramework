import allure

from pages.specialists_page import SpecialistsPage


@allure.suite("Страница Специалисты")
class TestSpecialistsPage:

    @allure.title("Проверка содержания страницы Специалисты")
    def test_view_specialists_page(self, driver, open_site):
        specialists_page = SpecialistsPage(driver)
        specialists_page.go_to_page()
        title = specialists_page.get_text_on_page()
        assert title == 'Наш стек', "Неправильное название секции"
        assert ['Android (нативная разработка)\n'
                'Языки программирования - Java, Kotlin\n'
                'Фреймворки - Android SDK, Dagger2, Coroutines, Clean Architecture, MVVM, '
                'MVP, RX, DeepLinks, Push Notifications, Flow, CustomView',
                'iOS (нативная разработка)\n'
                'Языки программирования - Swift, ObjectiveC\n'
                'Фреймворки - iOS SDK, Swinject, Clean Architecture, Viper, SwiftRX, '
                'DeepLinks, Push Notifications, UIKit, SwiftUi',
                'Flutter (кросплатформенная разработка)\n'
                'Язык программирования - Dart\n'
                'Фреймворки - Flutter SDK, get_it, Clean Architecture, MVVM, Bloc, DartRX, '
                'DeepLinks, Push Notifications, Retrofit'] == specialists_page.get_stack_items(), ("Неправильный "
                                                                                                   "список технологий")
