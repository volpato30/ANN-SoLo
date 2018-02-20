import logging

import spectral_library
import writer
from config import config


if __name__ == '__main__':
    # initialize logging
    logging.basicConfig(
            format='%(asctime)s [%(levelname)s/%(processName)s] '
                   '%(module)s.%(funcName)s : %(message)s',
            level=logging.DEBUG)

    # load the config
    config.parse()

    # execute the search
    if config.mode == 'bf':
        spec_lib = spectral_library.SpectralLibraryBf(
                config.spectral_library_filename)
    elif config.mode == 'ann':
        spec_lib = spectral_library.SpectralLibraryAnnoy(
                config.spectral_library_filename)

    identifications = spec_lib.search(config.query_filename)
    with spec_lib._library_reader as lib_reader:
        writer.write_mztab(identifications, config.out_filename, lib_reader)
    spec_lib.shutdown()

    logging.shutdown()
