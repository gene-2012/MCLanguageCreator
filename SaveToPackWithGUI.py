# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from SaveToPack import PackSaver

# Define the PackSaverGUI class
class PackSaverGUI:
    def __init__(self, root):
        # Initialize the root window and set its title
        self.root = root
        self.root.title("MC Mod Internationalization Tool")
        
        # Declare string variables for paths and languages
        self.jar_path = tk.StringVar()
        self.namespace = tk.StringVar()
        self.source_language = tk.StringVar(value="en_us")
        self.target_language = tk.StringVar(value="zh_cn")
        
        # Initialize PackSaver instance
        self.pack_saver = None
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Widgets for selecting JAR path, namespace, and languages
        tk.Label(self.root, text="JAR Path:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.jar_path, width=50).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_jar_zip).grid(row=0, column=2)
        
        tk.Label(self.root, text="Namespace:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.namespace).grid(row=1, column=1)
        
        tk.Label(self.root, text="Source Language:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.source_language).grid(row=2, column=1)
        
        tk.Label(self.root, text="Target Language:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.target_language).grid(row=3, column=1)
        
        tk.Button(self.root, text="Load Language", command=self.load_language).grid(row=4, column=0)
        tk.Button(self.root, text="Save as Resource Pack", command=self.save_resource_pack).grid(row=4, column=2)

    def browse_jar_zip(self):
        # Function to open file dialog for selecting a JAR file
        jar_path = filedialog.askopenfilename(title="Select Mod or Resource Pack", filetypes=[("JAR Files", "*.jar"), ("ZIP Resource Packs", "*.zip")])
        if jar_path:
            self.jar_path.set(jar_path)

    def load_language(self):
        # Load language data from the specified JAR file
        mod_path = self.jar_path.get()
        namespace = self.namespace.get()
        source_lang = self.source_language.get()
        target_lang = self.target_language.get()
        
        try:
            self.pack_saver = PackSaver(mod_path, namespace, source_lang, target_lang, 4)
            self.pack_saver.LoadModAndLanguageJson()
            self.display_language_content_intest()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_language_content(self):
        # Display language content in a text box (not currently used in this snippet)
        if self.pack_saver:
            lang_dict = self.pack_saver.LanguageJson()
            content = "\n".join([f"{key}: {value}" for key, value in lang_dict.items()])
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, content)
            
    def display_language_content_intest(self):
        # Display language content with editable entries inside a scrollable frame
        if self.pack_saver:
            lang_dict = self.pack_saver.LanguageJson()
            self._setup_scrollable_content(lang_dict)

    def _setup_scrollable_content(self, lang_dict):
        # Setup the scrollable frame to hold labels and entries for each language item
        scroll_frame = ttk.Frame(self.root)
        scroll_frame.grid(row=5, column=0, columnspan=3, sticky="nsew")
        
        canvas = tk.Canvas(scroll_frame, borderwidth=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        inner_frame.bind("<Configure>", on_frame_configure)

        row_count = 0

        self.entries = []
        for key, value in lang_dict.items():
            label = tk.Label(inner_frame, text=f"{key}: ")
            label.grid(row=row_count, column=0, sticky=tk.W)
            
            entry = tk.Entry(inner_frame, width=50)
            entry.insert(tk.END, value)
            entry.grid(row=row_count, column=1, sticky=tk.W)

            self.entries.append((key, entry))
            
            row_count += 1


        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(5, weight=1)

    def save_resource_pack(self):
        if self.pack_saver:
            # 在保存前，遍历所有条目并更新LanguageJson
            for key, entry in self.entries:
                new_value = entry.get()
                self.pack_saver.EditLanguageJson(key, new_value)  # 假设EditLanguageJson方法接受键值对来更新
            
            pack_path = filedialog.asksaveasfilename(title="Save Resource Pack", defaultextension=".zip", filetypes=[("ZIP Files", "*.zip")])
            if pack_path:
                self.pack_saver.SaveToPack(pack_path)
                messagebox.showinfo("Success", f"Resource pack saved successfully at {pack_path}")
        else:
            messagebox.showwarning("Warning", "No language data loaded. Please load language first.")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = PackSaverGUI(root)
    root.mainloop()