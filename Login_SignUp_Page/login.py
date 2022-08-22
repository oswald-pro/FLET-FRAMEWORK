import flet
from flet import Page, AppBar, TextField, Text, Row, ElevatedButton, Switch, WEB_BROWSER, Column, ProgressBar, \
    ProgressRing, TextButton, View, colors, Dropdown, dropdown
from time import sleep

import sqlite3

conn = sqlite3.connect('connect.db')
c = conn.cursor()


# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS logintable(username TEXT, password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO logintable(name,role,gender,username,password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM logintable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


status_text = Text(None)


def main(page: Page):
    page.title = "App Login Page"

    # -------Page Mode-------------
    def theme_changed(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        c.label = "Light Mode" if page.theme_mode == "light" else "Dark Mode"
        page.update()

    page.theme_mode = "light"
    c = Switch(label="Light Mode", on_change=theme_changed)
    page.add(c)

    def login_button_clicked(e):
        # -------ProgressBar Function-------------
        page.splash = ProgressBar()
        login_btn.disabled = True
        page.update()
        sleep(3)
        page.splash = None
        login_btn.disabled = False
        page.update()
        # -------End ProgressBar -------

    def signup_button_clicked(e):
        # -------ProgressBar Function-------------
        page.splash = ProgressBar()
        login_btn.disabled = True
        page.update()
        sleep(3)
        page.splash = None
        login_btn.disabled = False
        page.update()
        # -------End ProgressBar -------

    def route_change(route):
        global login_btn
        # -------------------------Sign IN Form--------------------------------
        text = Text(value="Conn PAGE", size=40, text_align="center", weight="w900", color="BLUE")
        username = TextField(label="Username", hint_text="Your username...", width=350, text_align="center",
                             border_radius=30, prefix_icon="AVATAR")
        password = TextField(label="Password", hint_text="Enter your password", width=350, text_align="center",
                             border_radius=30, prefix_icon="OPEN_LOCK")
        login_btn = ElevatedButton("Sign in", on_click=login_button_clicked)
        password_forgot = TextButton("Password Forgot!", icon="LOCK")
        # -------------------------End Sign IN Form--------------------------------

        # -------------------------Sign UP Form--------------------------------
        new_text = Text(value="SIGNUP PAGE", size=40, text_align="center", weight="w900", color="BLUE")
        new_username = TextField(label="Username", hint_text="Your username...", width=350, text_align="center",
                                 border_radius=30)
        firstname = TextField(label="First Name", hint_text="Your firstname...", width=350, text_align="center",
                              border_radius=30)
        lastname = TextField(label="Last Name", hint_text="Your lastname...", width=350, text_align="center",
                             border_radius=30)
        email = TextField(label="Email", hint_text="Your email address...", width=350, text_align="center",
                          border_radius=30)
        gender = Dropdown(
            label="Gender", hint_text="Select gender...",
            width=350, border_radius=30,
            options=[
                dropdown.Option("Male"),
                dropdown.Option("Female")
            ]
        )
        new_password = TextField(label="Password", hint_text="Enter your password", width=350, text_align="center",
                                 border_radius=30)
        signup = ElevatedButton("Sign Up", on_click=signup_button_clicked)

        # -------------------------End Sign UP Form--------------------------------

        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    Row(alignment="center", controls=[text]),
                    Row(alignment="center", controls=[username]),
                    Row(alignment="center", controls=[password]),
                    Row(alignment="center",
                        controls=[login_btn, ElevatedButton("Sign Up", on_click=lambda _: page.go("/signup"))]),
                    Row(alignment="center", controls=[password_forgot]),
                ],
            )
        )
        if page.route == "/signup":
            page.views.append(
                View(
                    "/signup",
                    [
                        AppBar(title=Text("Back"), bgcolor=colors.SURFACE_VARIANT),
                        Row(alignment="center", controls=[new_text]),
                        Row(alignment="center", controls=[firstname, lastname]),
                        Row(alignment="center", controls=[new_username, gender]),
                        Row(alignment="center", controls=[email, new_password]),
                        Row(alignment="center", controls=[signup, ElevatedButton("Go Login", on_click=lambda _: page.go("/"))]),

                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


#flet.app(target=main)
flet.app(target=main, view=WEB_BROWSER)
