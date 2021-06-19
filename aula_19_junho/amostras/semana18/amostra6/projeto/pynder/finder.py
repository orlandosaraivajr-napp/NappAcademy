import time
import glob
from pynder.io_getter import GenericIoGetter


class Pynder():
    def __init__(self) -> None:
        self.extension_getters = {
            'csv': GenericIoGetter(),
            'txt': GenericIoGetter()
        }

    def search_in_file(self, file_name: str, text: str, extension: str):
        t_start = time.time()

        if extension not in self.extension_getters:
            raise NotImplementedError(
                f'{extension} Extension Not Implemented in Getter values')

        file_opend = self.extension_getters[extension].get_io(file_name)

        findInLines = list()
        for line_number, line in enumerate(file_opend):
            if text.lower() in line.lower():
                findInLines.append(line_number+1)

        if findInLines:
            print(f'"{file_name}" {len(findInLines)} results for "{text}"', 'Found at lines',
                  findInLines, 'in', time.time() - t_start, 'seconds\n')

        return dict(file_name=file_name, text=text, findInLines=findInLines)

    def search_all_files(self, text: str, extension: str, path: str, recursive=True):
        results = list()
        looking_for = f'{path}/**/*.{extension}'
        matcheds_files = glob.glob(looking_for, recursive=recursive)

        if extension not in self.extension_getters:
            raise NotImplementedError(
                f'{extension} Extension Not Implemented in Getter values')

        for file in matcheds_files:

            results.append(self.search_in_file(
                file_name=file, text=text, extension=extension
            ))

        return results
