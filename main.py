from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
import plyer


class GeoLocationApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        layout = MDBoxLayout(orientation='vertical', padding=20)

        # Добавляем кнопки и метки
        label_text = "Нажмите кнопку ниже, чтобы увидеть ваше текущее местоположение."
        self.location_label = MDLabel(text=label_text, halign="center")
        location_button = MDRaisedButton(
            text="Получить координаты",
            on_release=self.get_location,
            pos_hint={'center_x': 0.5}
        )

        layout.add_widget(self.location_label)
        layout.add_widget(location_button)

        return layout

    def request_permissions(self):
        """Запрашиваем необходимые разрешения"""
        try:
            from android.permissions import Permission, request_permissions

            permissions = [
                Permission.ACCESS_FINE_LOCATION,
                Permission.ACCESS_COARSE_LOCATION
            ]

            request_permissions(permissions)
        except ImportError:
            pass  # Для запуска на ПК игнорируем ошибку отсутствия модуля android

    def get_location(self, instance):
        """Обрабатываем нажатие кнопки и получаем координаты"""
        if not hasattr(plyer.gps, 'start'):
            toast("GPS недоступен.")
            return

        self.request_permissions()

        def on_location(**kwargs):
            lat = kwargs['lat']
            lon = kwargs['lon']
            result = f"Ваше текущее положение:\nШирота: {lat}\nДолгота: {lon}"
            self.location_label.text = result

        def on_status(status_type, status_message):
            print(f"GPS статус: {status_type}, сообщение: {status_message}")

        plyer.gps.configure(on_location=on_location, on_status=on_status)
        plyer.gps.start(minTime=1000, minDistance=0)


if __name__ == '__main__':
    app = GeoLocationApp()
    app.run()