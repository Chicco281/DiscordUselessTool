import PySimpleGUI as sg


def add_mark(text, mark, escape, both=True):
    text = list(text)
    new_text = ""

    if escape:
        text.insert(0, f"{mark}")
        text.insert(0, "\\")
        if both:
            text.insert(len(text), "\\")
            text.insert(len(text), f"{mark}")
    else:
        text.insert(0, f"{mark}")
        if both:
            text.insert(len(text), f"{mark}")

    for char in text:
        new_text += char
    return new_text


def popup(text):
    layout = [[sg.Button("<--")],
              [sg.Text("Here's your text!", text_color="yellow", font="bold", justification="center")],
              [sg.Multiline(text, disabled=True)]]

    window = sg.Window("Copy me!", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "<--":
            window.close()
            main()

    window.close()


def main():
    layout = [[sg.InputText("", key="txt")],
              [sg.Checkbox("Bold", key="bol", enable_events=True)],
              [sg.Checkbox("Italic", key="ita", enable_events=True)],
              [sg.Checkbox("Crossed", key="cro", enable_events=True)],
              [sg.Checkbox("Spoiler", key="spo", enable_events=True)],
              [sg.Checkbox("Response", key="res", enable_events=True)],
              [sg.Checkbox("Code-like", key="code", enable_events=True)],
              [sg.Text("")],
              [sg.Checkbox("Show escape characters", key="show")],
              [sg.Button("Generate text")]]

    window = sg.Window("The most useless app in existence", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "code":
            window["bol"].update(False)
            window["ita"].update(False)
            window["cro"].update(False)
            window["res"].update(False)
            window["spo"].update(False)

        elif event in ["bol", "ita", "cro", "res", "spo"]:
            window["code"].update(False)

        elif event == "Generate text":
            show = values["show"]
            text = values["txt"]
            if not text:
                text = " "

            if values["bol"]:
                text = add_mark(text, "*", show)
                text = add_mark(text, "*", show)
            if values["ita"]:
                text = add_mark(text, "_", show)
            if values["cro"]:
                text = add_mark(text, "~", show)
                text = add_mark(text, "~", show)
            if values["spo"]:
                text = add_mark(text, "||", False)
            if values["res"]:
                text = add_mark(text, "> ", False, False)
            if values["code"]:
                text = add_mark(text, "`", show)

            window.close()
            popup(text)

    window.close()


if __name__ == '__main__':
    main()