import flet
from flet import Page, Card, Image, Container, Switch, Text, TextField, Column, Row, ElevatedButton, Dropdown, \
    dropdown, ProgressBar, ButtonStyle, icons, Icon, ListTile, TextButton, WEB_BROWSER
from time import sleep


def main(page: Page):
    page.title = "USER PROFILE CARD APP"

    img = Image(
        src=f"https://omitcg.com/wp-content/uploads/2021/06/1-1-180x190.png",
        width=120,
        height=120,
        fit="contain",
    )
    #images = Row(expand=1, wrap=False, scroll="always")

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

    # ---------------Card Section--------------------------------
    profile = Column()
    userCard = Card(
        content=Container(
            content=Column(
                [
                    ListTile(
                        leading=img,
                        title=Text("Ing. Oswald MBOUSSA"),
                        subtitle=Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
                    ),
                    Row(
                        [ListTile(
                            leading=Icon(icons.PHONE),
                            title=Text("+242 06 909 6565")
                        )],
                    ),
                    Row(
                        [ListTile(
                            leading=Icon(icons.EMAIL),
                            title=Text("oswaldmboussa1@gmail.com")
                        )]
                    ),
                    Row(
                        [ListTile(
                            leading=Icon(icons.WEB_ROUNDED),
                            title=Text("www.oswaldmboussa.com")
                        )]
                    ),
                    Row(
                        [TextButton("View More...")], alignment="end"
                    ),
                ],
                width=400,
            )
        )
    )

    textForm = Text(value="PUBLISH YOUR PROFILE", style="headlineMedium")

    name = TextField(label="Name", hint_text="Your first name...", width=300, text_align="center")
    bio = TextField(label="Bio", hint_text="Your Biography...", width=610, max_length=50)
    tel = TextField(label="Telephone", hint_text="Your telephone number...", width=300, text_align="center")
    web = TextField(label="Website", hint_text="Your website...", width=300, text_align="center")
    email = TextField(label="Email", hint_text="Your email address...", width=300, text_align="center")
    send = ElevatedButton("Publish Now", on_click=register_clicked)

    page.add(
        Row(alignment="center",
            controls=[userCard, userCard, userCard]
        ),
        Row(alignment="center",
            controls=[textForm]
            ),
        Row(alignment="center",
            controls=[name, tel]
            ),
        Row(alignment="center",
            controls=[web, email]
            ),
        Row(alignment="center",
            controls=[bio]
            ),
        Row(alignment="center",
            controls=[send]
            ),

    )


#flet.app(target=main)
flet.app(target=main, view=WEB_BROWSER)