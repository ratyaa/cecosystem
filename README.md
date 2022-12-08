# Cecosystem, closed ecosystem model

Интерактивная симуляция закрытой экосистемы.

## Запуск программы

Для запуска требуются `Python >= 3.9` и `GNU Make`.
```
make init
```
инициализирует виртуальное окружение `Python` и устанавливает необходимые пакеты,
```
make run
```
запускает программу. Для вывода возможных опций выполните `make` без аргументов,
или `make help`.


#### Windows

`GNU Make` можно установить с помощью пакетного менеджера `winget` в `Powershel`:
```
winget install GnuWin32.Make
winget install python
```
или с официального [веб-сайта](https://gnuwin32.sourceforge.net/packages/make.htm).
Работа с `make` производится в консоли `git-bash`.

#### NixOS
В NixOS, из-за особенностей дистрибутива, пакеты, установленные с помощью `pip`
зачастую не работают, требуется устанавливать их с помощью системного пакетного
менеджера. Также не имеет смысла работа с `python venv`, т.к. `pip` не работает,
а `nix-shell` уже предоставляет универсальную виртуальную среду, которая описана
в файле `shell.nix`. Для запуска проекта активируйте `nix-shell` без аргументов
и измените значение переменной `nixos` в `Makefile` на `true`.


	
