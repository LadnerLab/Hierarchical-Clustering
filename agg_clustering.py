#!/usr/bin/env python3
import sys
import optparse

import protein_oligo_library as oligo

def main():

    usage = "usage: %prog [options]"
    option_parser = optparse.OptionParser( usage )
    add_program_options( option_parser )
    options, arguments = option_parser.parse_args()


    if options.query is None:
        print( "ERROR: Fasta query file must be provided." )
        sys.exit( 0 )

    names, sequences = oligo.read_fasta_lists( options.query )
    names, sequences = oligo.sort_sequences_by_length( names, sequences )

    # Get the sequences sorted in increasing order
    names.reverse()
    sequences.reverse()

    out_seqs = oligo.create_distance_matrix_of_sequences( sequences[0:10], options.XmerWindowSize, 1 )

    for index in out_seqs:
        print( index )
            

def add_program_options( options ):
    options.add_option( '-q', '--query', help = "Fasta query file to perform calculations on. [None, required]" )

    # TODO: Add description of format of output file  
    options.add_option( '-o', '--output', help = "File to write program output to. [out.txt]", default = "out.txt" )

    options.add_option( '-x', '--XmerWindowSize', help = "Size of xmers to grab from each sequence to do the comparisons [19]", type = int,
                        default = 19 )


    
if __name__ == '__main__':
    main()

