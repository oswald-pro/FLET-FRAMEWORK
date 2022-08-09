import flet
from flet import Page, TextField, FloatingActionButton, Column, Row, Text, IconButton, icons, OutlinedButton, Tabs, \
    Theme, Tab, UserControl, colors, Checkbox


class Task(UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.display_task = Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_cliced,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            icon_color=colors.RED,
                            tooltip="delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ]

                ),

            ],

        ),

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        ),

        return Column(controls=[self.display_view, self.edit_view])

    def edit_cliced(self, e):
        self.edit_name.value =self.display_task.label
        self.display_view.visible = False,
        self.edit_view.visible = True,
        self.update()

    def edit_cliced(self, e):
        self.edit_name.value =self.display_task.label
        self.display_view.visible = False,
        self.edit_view.visible = True,
        self.update()


class MyTodoApp(UserControl):
    def build(self):
        self.new_task = TextField(hint_text="Add a new task here...", expand=True, width=500, text_align="center")
        self.tasks = Column()

        return Column(
            width=700,
            controls=[
                Row([Text(value="OMIT ToDos", style="headlineMedium")], alignment="center"),
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.tasks,
                        #Row(
                        #    alignment="spaceBetween",
                        #    vertical_alignment="center",
                        #    controls=[
                        #        self.items_left,
                        #        OutlinedButton(
                        #            text="Clear completed", on_click=self.clear_clicked
                        #        ),
                        #    ],
                        #),
                    ],
                ),
            ],
        )

    def add_clicked(self, e):
        print("Add clicked")

    def clear_clicked(self, e):
        print("Clear clicked")


def main(page: Page):
    page.title = "TODO APP"
    page.horizontal_alignment = "center"

    # create a TODO app instance
    app = MyTodoApp()

    page.add(app)


flet.app(target=main)
