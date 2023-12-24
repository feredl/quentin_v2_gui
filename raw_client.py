""" Simple client code example"""

from quentin import Quentin

appendix_vergiliana = Quentin("v3_input.xlsx", skip_zeros=False)
appendix_vergiliana.show_stemma()