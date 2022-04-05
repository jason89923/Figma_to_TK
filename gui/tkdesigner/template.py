TEMPLATE = """
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import ctypes


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("{{ assets_path }}")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("{{ window.width }}x{{ window.height }}")
window.configure(bg = "{{ window.bg_color }}")


canvas = Canvas(
    window,
    bg = "{{ window.bg_color }}",
    height = {{ window.height }},
    width = {{ window.width }},
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


{%- for element in elements -%}
    {{ element.to_code() }}
{%- endfor -%}


ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
window.tk.call('tk', 'scaling', ScaleFactor/75)
window.resizable(False, False)
window.mainloop()

"""
