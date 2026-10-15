import sys
import os

import helpers.bio_files as bf
import helpers.fastq as ft

def filter_fastq(input_fastq: str, 
                output_fastq: str,
                gc_bounds: tuple(float, float) = (0, 100), 
                length_bounds: tuple(int, int) =(0, 2**32), 
                quality_threshold: float = 0):
    """
    Filters fastq file with DNA and RNA sequences and writes a new filtered file.

    Args:
        input_fastq (str): the path to the input FASTQ file
        output_fastq (str): output FASTQ file name
        gc_bounds (tuple): a tuple with GC percentage boundaries (integer or float). Default is (0, 100).
        length_bounds (tuple()): a tuple with length boundaries (only integer) Default is (0, 2**32). 
        quality_threshold (float): an integer or float number, lower boundary for mean quality. Default is 0.

    Returns: None
        
    """
    work_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    if not os.path.exists(os.path.join(work_dir, 'filtered')):
        os.mkdir(os.path.join(work_dir, "filtered"))
    output_path = os.path.join(work_dir, "filtered", output_fastq)

    with open(input_fastq, "r") as inp, open(output_path, "w") as out:
                while True:
                    header = inp.readline()
                    if not header:
                       break
                    sequence = inp.readline()
                    sep = inp.readline()
                    quality = inp.readline()
        
                    gc = ft.calc_gc(sequence)
                    length = len(sequence)
                    mean_q = ft.calc_mean_quality(quality)
        
                    if (ft.in_gc_bounds(gc, gc_bounds) and ft.in_len_bounds(length, length_bounds) and mean_q >= quality_threshold):
                        out.write(header)
                        out.write(sequence)
                        out.write(sep)
                        out.write(quality)


filter_fastq('examples/example_fastq.fastq', 'output1', 50, 2 ** 32, 35)

def convert_multiline_fasta_to_oneline():
    ...


def parse_blast_output():
    ...


def select_genes_from_gbk_to_fasta():
    ...