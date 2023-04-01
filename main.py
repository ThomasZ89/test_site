import flet as ft


def main(page: ft.Page):
    page.title = "AlertDialog examples"

    #page.dark_theme = ft.theme.Theme(color_scheme_seed="orange")
    #page.theme_mode = ft.ThemeMode.DARK

    dlg = ft.AlertDialog(
        title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    scoreBtn = ft.ElevatedButton(content=ft.Text(value="120 Points", size=25),
                                 height=200,
                                 style=ft.ButtonStyle(shape=ft.CircleBorder()
                                                      ),
                                 )

    goBackBtn = ft.ElevatedButton(content=ft.Text(value="Go Back", size=25),
                                  bgcolor=ft.colors.RED, color=ft.colors.BLACK,
                                  height=160, width=110, style=ft.ButtonStyle(
        shape={
            ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=0)}
    ))

    continueBtn = ft.ElevatedButton(content=ft.Text(value="Continue", size=25),
                                    bgcolor=ft.colors.GREEN, color=ft.colors.BLACK,
                                    height=160, width=450,
                                    style=ft.ButtonStyle(
        shape={
            ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=0)}
    )
    )

    dlg_modal = ft.AlertDialog(
        content=ft.Container(
            ft.Column(controls=[scoreBtn,
                                ft.Row(controls=[goBackBtn,
                                                 continueBtn], spacing=0
                                       )],
                      horizontal_alignment="CENTER",
                      alignment="END",
                      spacing=100
                      ),
            padding=0,
            width=670,
            height=500,
            bgcolor=ft.colors.TRANSPARENT

        ),
        open=False,
        modal=True,
        content_padding=0,
        shape = ft.CountinuosRectangleBorder(radius=0),
        actions_padding=0
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dlg),
        ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    )


ft.app(target=main)
