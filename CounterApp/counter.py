import flet
from flet import Page, TextField, Row, IconButton, icons

def main(page: Page):
    page.title = "COUNTER APP"
    page.vertical_alignment = "center"

    txt_field = TextField(value="0", width=500, text_align="center")

    def minus_clicked():
        txt_field.value = int(txt_field.value) - 1
        page.update()

    def plus_clicked(e):
        txt_field.value = int(txt_field.value) + 1
        page.update()

    page.add(Row([
        IconButton(icons.REMOVE, on_click=minus_clicked),
        txt_field,
        IconButton(icons.ADD, on_click=plus_clicked),
    ], alignment="center", auto_scroll=True))


flet.app(target=main, view=flet.WEB_BROWSER)
