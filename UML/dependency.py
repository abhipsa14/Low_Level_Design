class Document:
    def __init__(self,title:str,content:str, pages:int)->None:
        self.__title:str=title
        self.__content:str=content
        self.__pages:int=pages
    def get_title(self)->str:
        return self.__title
    def get_content(self)->str:
        return self.__content
    def get_pages(self)->int:
        return self.__pages

# Printer class
class Printer:
    def __init__(self,printer_name:str, printer_type:str)->None:
        self.__printer_name:str=printer_name
        self.__printer_type:str=printer_type
    def print_document(self,document:Document)->None:
        # Printer uses Document object temporarily through method parameter
        # After printing, Printer doesn't keep the Document
        print(f"\n{'='*50}")
        