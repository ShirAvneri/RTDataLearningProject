

from Project.UI.CommonWidgets.CommonButtons import RadioButtonsGroup



def create_buttons_group(invoke_on_click, click_signal, x_pos, y_pos, buttons_names):
    return RadioButtonsGroup(invoke_on_click, click_signal, x_pos, y_pos, buttons_names)
