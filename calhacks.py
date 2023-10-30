import reflex as rx
from calhacks import style
from calhacks.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="3em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.vstack(  # Change from rx.hstack to rx.vstack to stack elements vertically
        rx.text("Econvert", font_size="3.0em", color = "green"),  # Add the "Econvert" text
        rx.text("The best money converter for video games", font_size="1.5em", color = "green"),  
        rx.hstack(
            rx.input(
                value=State.question,
                placeholder="Enter Game Currency",
                on_change=State.set_question,
                style=style.input_style,
            ),
            rx.button(
                "Convert",
                on_click=State.answer,
                style=style.button_style,
            ),
        ),
    )

def index() -> rx.Component:
    return rx.container(
        action_bar(),
        chat(),
        style=style.main_container_style,  # Apply the main container style
    )


app = rx.App()
app.add_page(index)
app.compile()

