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
        margin_y="1em",
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
        rx.text("Econvert", font_size="3.0em", color = "#7F2A3C"),  # Add the "Econvert" text
        rx.text("Convert from USD to any currency(Yen, Bitcoin, Vbucks, Shell Money, etc.)", font_size="1em", color = "#7F2A3C"),  
        rx.hstack(
            rx.input(
                value=State.question,
                placeholder="Currency for Conversion",
                on_change=State.set_question,
                # style=style.input_style,
                color = "black", 
            ),
            rx.input(
                value=State.amount,
                placeholder="USD$",
                on_change=State.set_amount,
                # style=style.input_style,
                color = "black", 
            ),
            rx.button(
                "Convert",
                on_click=State.answer,
                style=style.button_style,
            ),
            style={"display": "flex", "flex-direction": "row"},
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
