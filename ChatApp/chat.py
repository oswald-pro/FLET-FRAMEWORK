import flet
from flet import Page, CircleAvatar, Stack, Column, Row, Text, TextField, ElevatedButton, alignment, colors
from flet.container import Container


def main(page: Page):
    page.title = "OMIT CHAT APP"

    # subscribe to broadcast messages
    def on_message(msg):
        messages.controls.append(Text(msg))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f"{avatar}{username.value}: {message.value}")
        # clean up the form
        message.value = ""
        page.update()

    messages = Column()

    # avatar with online status
    avatar = Stack([
        CircleAvatar(
            background_image_url="https://afritservice.com/wp-content/uploads/2020/04/greg.jpg"
        ),
        Container(
            content=CircleAvatar(bgcolor=colors.GREEN, radius=5),
            alignment=alignment.bottom_left,
        ),
    ],
        width=40,
        height=40
    ),
    username = TextField(hint_text="Your name", width=150)
    message = TextField(hint_text="Your message...", expand=True) # fill all the space
    send = ElevatedButton("Send", on_click=send_click)
    page.add(messages,Row(
        controls=[avatar, username, message, send]
    ))


# flet.app(target=main)
flet.app(target=main, view=flet.WEB_BROWSER)