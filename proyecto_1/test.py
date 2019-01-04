from proyecto_1 import File_Manager, Text_Procesing

if __name__ == '__main__':
    fm = File_Manager.File_Manager(path='/home/xiao/Documents/proyecto_Comp1/dataset_entrenamiento/buenas/')
    reviews = fm.extract_data_from_files()
    tp = Text_Procesing.Text_Processing(reviews)
    processed_reviews = tp.process_reviews()
    print(processed_reviews)