import SaveToPack
from tkinter import Tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import StringVar
path = None
def mod_select():
    global ms
    ms = filedialog.askopenfilename(title="Select the mod jar", filetypes=[("jar", "*.jar")])
    global window, path
    if path:
        path.destroy()
    path = ttk.Label(window, text=ms)
    path.pack()

    
window = Tk()
select_mod = ttk.Button(window, text="Select Mod", command = mod_select)
select_mod.pack()
mc_languages = ["en_us", "de_de", "es_es", "fr_fr", "it_it", "ja_jp", "ko_kr", "pt_br", "zh_cn", "zh_tw"]
source_lang_prompt = StringVar(value="Select a source language...")
source_lang = ttk.Combobox(window, values=mc_languages, textvariable=source_lang_prompt)
source_lang.pack()
target_lang_prompt = StringVar(value="Select a target language...")
target_lang = ttk.Combobox(window, values=mc_languages, textvariable=target_lang_prompt)
target_lang.pack()
namespace_prompt = StringVar(value="Enter the mod namespace...")
namespace = ttk.Entry(window, textvariable=namespace_prompt)
namespace.pack()
commit = ttk.Button(window, text="Commit", command=EditView)
commit.pack()
window.mainloop()
