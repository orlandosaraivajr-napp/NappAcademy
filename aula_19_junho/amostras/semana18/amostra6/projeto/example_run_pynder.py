from pynder.finder import Pynder

if __name__ == "__main__":
    myFinder = Pynder()

    myFinder.search_all_files(
        text='napp',
        extension='txt',
        path='./',
    )

    myFinder.search_in_file(
        file_name='./diretorio5/arquivo4.txt',
        text='Napp',
        extension='txt'
    )
