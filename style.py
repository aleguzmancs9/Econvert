shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
)
main_container_style = dict(
    bg="#faf0e6",  
)
# Set specific styles for questions and answers.
question_style = message_style | dict(
    bg="#ffffff", margin_left=chat_margin
)
answer_style = message_style | dict(
    bg="#D9DADB", margin_right=chat_margin
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow, color = "red"
)
button_style = dict(
    bg="#7F2A3C",  # Primary color
    color="#000000",  # Text color
    border="none",
    padding="0.5em 2em",
    border_radius="5px",
    cursor="pointer",
    transition="background-color 0.2s",
)
