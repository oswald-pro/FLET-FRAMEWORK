import flet
from flet import Page, Switch, theme, Text, TextField, RadioGroup, Radio, Column, Checkbox, Row, ElevatedButton, \
    Dropdown, dropdown, ProgressBar, ButtonStyle, colors, IconButton, icons
from time import sleep


def main(page: Page):
    page.title = "SAMPLE FORM ONE"

    # -------Page Theme Mode---
    def theme_changed(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        c.label = "Light theme" if page.theme_mode == "light" else "Dark theme"
        page.update()

    page.theme_mode = "light"
    c = Switch(label="Light theme", on_change=theme_changed)
    page.add(c)
    # -------End Page Mode--------------

    def register_clicked(e):

        # -------ProgressBar Function-------------
        # page.splash = ProgressBar()
        page.splash = ProgressBar()
        send.disabled = True
        page.update()
        sleep(3)
        page.splash = None
        send.disabled = False
        page.update()
        # -------End ProgressBar -------

    # -------Form Section --------------------------------
    form = Column()
    text = Text(value="OMIT REGISTRATION FORM", style="headlineMedium")

    firstname = TextField(label="First Name", hint_text="Your first name...", width=300, text_align="center")
    lastname = TextField(label="Last Name", hint_text="Your last name...", width=300, text_align="center")

    email = TextField(label="Email", hint_text="Your email address...", width=300, text_align="center")
    whatsapp = TextField(label="WhatsApp", hint_text="Your whatsapp number...", width=300, text_align="center")

    gender = Dropdown(
        label="Gender", hint_text="Select gender...",
        width=300,
        options=[
            dropdown.Option("Male"),
            dropdown.Option("Female")
        ]
    )
    address = TextField(label="Address", hint_text="Your Address...", width=300, text_align="center")
    send = ElevatedButton("Register Now", on_click=register_clicked)
    # -------End of form--------------------------------

    page.add(
             Row(alignment="center", controls=[text]),
             Row(alignment="center", controls=[firstname, lastname]),
             Row(alignment="center", controls=[email, whatsapp]),
             Row(alignment="center", controls=[gender, address]),
             Row(alignment="center", controls=[send])
             )


flet.app(target=main)
