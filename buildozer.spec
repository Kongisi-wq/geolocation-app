[app]

# (str) Название приложения
title = Mobile App 001

# (str) Имя пакета (уникальное)
package.name = mobileapp001

# (str) Домен (рекомендуется org.вашеимя)
package.domain = org.wiseplat

# (str) Путь к исходникам
source.dir = .

# (str) Главный Python-файл
source.main = main.py

# (str) Версия приложения
version = 0.3

# (list) Зависимости
# Обязательно: python3, kivy, kivymd, plyer — для GPS
requirements = python3==3.10,hostpython3==3.10,kivy==2.1.0,kivymd@git+https://github.com/kivymd/KivyMD.git@master,plyer

# (list) Какие файлы включать
source.include_exts = py,kv,png,jpg,jpeg,atlas,ttf,txt,otf

# (str) Ориентация: all = портрет + ландшафт
orientation = all

# (bool) Полноэкранный режим (0 = нет, 1 = да)
fullscreen = 0


# -----------------------------------------------------------------------------
# Настройки Android
# -----------------------------------------------------------------------------

# (list) Разрешения
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# (int) Целевой API (рекомендуется 33)
android.api = 33

# (int) Минимальный API (поддержка с Android 5.0+)
android.minapi = 21

# (str) Версия NDK — r23b стабильно скачивается
android.ndk = r23b

# (int) NDK API — должен совпадать с minapi
android.ndk_api = 21

# (list) Архитектуры (поддержка большинства устройств)
android.archs = armeabi-v7a

# (bool) Разрешить резервное копирование
android.allow_backup = True

# (str) Формат отладочного APK
android.debug_artifact = apk


# -----------------------------------------------------------------------------
# Настройки Buildozer
# -----------------------------------------------------------------------------

[buildozer]

# (int) Уровень логов: 2 = полный отладочный вывод
log_level = 2

# (int) Предупреждать, если запущено от root
warn_on_root = 1
