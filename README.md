# bds-project-assignment-3
Jedná se o poslední projekt v předmětu BDS
Projekt je realizován pomocí programovacího jazyk Python ve frameworku Django 4.0

## Quickstart
Po naklonování repozitáře musíte nejdříve vytvořit virtualní prostředí pokud nemáte nainstalovaný modul použijte tento příkaz:
```shell
pip install venv
```
Pro aktivaci a nainstalování potřebných knihoven zadejte příkazy
```shell
python -m venv myvenv
cd .\venv\Scripts\activate
(venv) PS D:(your repository)> pip install -r requirements.txt 
```
Nyní se stáhnout všechny potřebné knihovny jáké jsou staženy zjistíte pomocí příkazu
```shell
pip freeze
```
Nebo je můžete naleznout v souboru LICENSES.md
Nyní se můžeme pustit do spuštění projektu
```shell
(venv) PS D:(your repository)> cd .\fastfood\
(venv) PS D:(your repository)> python manage.py runserver
```
Nyní by mělo vše fungovat dále se o projektu můžete dozvědět ze souboru howto.pdf
