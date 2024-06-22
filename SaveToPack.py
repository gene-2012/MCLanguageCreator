import zipfile
import json

class PackSaver:
    """
    This is a MC mod i18n tool. PackSaver can save the language json to the resource pack.
    """
    def __init__(self, mod_path, namespace, source_language, target_language, version_id):
        self.source_language = source_language
        self.target_language = target_language
        self.mod_path = mod_path
        self.mod_jar = None  # Initialize mod_jar attribute
        self.namespace = namespace
        self.version_id = version_id
        self.language_dict = None  # Initialize language_dict attribute
        self.LoadModAndLanguageJson()  # Call a new method to load mod and JSON in one go
        

    def LoadModAndLanguageJson(self):
        """
        Load the JAR file and the language JSON in one method to ensure the zipfile is open when needed.
        """
        try:
            self.mod_jar = zipfile.ZipFile(self.mod_path, 'r')  # Open the JAR file
            self.language_dict = self.__LoadLanguageJson()
            self.pack_mcmeta = self.__GeneratePackMeta()
            self.pack_mcmeta["pack"]["description"] = f"{self.namespace} translation pack, made by G2N's I18N tool."
        except zipfile.BadZipFile as e:
            print(f"Error loading JAR file: {e}")
        except KeyError as e:
            print(f"Error: Missing expected file in JAR - {e}")
    def __GeneratePackMeta(self):
        """
        Load the pack.mcmeta file from the opened JAR file.
        """
        if self.mod_jar:
            try:
                pack_mcmeta = self.mod_jar.read('pack.mcmeta')
                return json.loads(pack_mcmeta)
            except KeyError:
                print("Error: 'pack.mcmeta' not found in the JAR file.")
                try:
                    pack_mcmeta_json = """
                    {
                        "pack": {
                            "pack_format": {verid},
                            "description": "{desc}"
                        }
                    }
                    """
                    pack_mcmeta_json = pack_mcmeta_json.replace("{verid}", str(self.version_id))
                    pack_mcmeta_json = pack_mcmeta_json.replace("{desc}", f"{self.namespace} translation pack, made by G2N's I18N tool.")
                    return json.loads(pack_mcmeta_json)
                except Exception as e:
                    print(f"Error generating pack.mcmeta: {e}")

        else:
            print("Error: Mod JAR not loaded.")
        return {}
    def __LoadLanguageJson(self):
        """
        Load the source language JSON from the opened JAR file.
        """
        if self.mod_jar:
            try:
                language_json = self.mod_jar.read(f"assets/{self.namespace}/lang/{self.source_language}.json")
                return json.loads(language_json)
            except KeyError:
                print(f"Error: '{self.source_language}.json' not found in the specified namespace.")
        else:
            print("Error: Mod JAR not loaded.")
        return {}

    def EditLanguageJson(self, key, value):
        if self.language_dict:
            self.language_dict[key] = value
        else:
            print("Error: Language dictionary not loaded.")

    def LanguageJson(self):
        return self.language_dict
    def SaveToPack(self, pack_path):
        """
        Save the edited language JSON to a new ZIP file representing a resource pack.
        """
        if self.language_dict:
            # Create a new ZipFile object for the output resource pack
            with zipfile.ZipFile(pack_path, 'w', zipfile.ZIP_DEFLATED) as output_zip:
                # Write the translated JSON file to the output ZIP
                output_zip.writestr(f"assets/{self.namespace}/lang/{self.target_language}.json",
                                    json.dumps(self.language_dict, indent=4).encode('utf-8'))
                output_zip.writestr("pack.mcmeta", json.dumps(self.pack_mcmeta, indent=4).encode('utf-8'))
                print(f"Resource pack '{pack_path}' saved successfully.")
        else:
            print("Error: No language dictionary to save. Please edit the language first.")


    def __del__(self):
        """Destructor to ensure the zipfile is closed when the object is deleted."""
        if self.mod_jar:
            self.mod_jar.close()

# Usage example
if __name__ == "__main__":
    psv = PackSaver("D:/MC/bakaXL/.minecraft/versions/1.17.1-Fabric-0.14.8/mods/litematica-fabric-1.17.1-0.9.0.jar",
                     "litematica", "en_us", "zh_tw")
    print(psv.LanguageJson())
    psv.SaveToPack("D:/MC/test.zip")
    del psv  # Ensure resources are cleaned up