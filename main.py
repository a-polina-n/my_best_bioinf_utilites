import sys
import os


import helpers.bio_files as bf
import helpers.fastq as ft


def filter_fastq(input_fastq: str, 
                output_fastq: str,
                gc_bounds: tuple[float, float] = (0, 100), 
                length_bounds: tuple[int, int] =(0, 2**32), 
                quality_threshold: float = 0):
    """
    Filters fastq file with DNA and RNA sequences and writes a new filtered file.

    Args:
        input_fastq (str): path to the input FASTQ file
        output_fastq (str): path to the output file where filtered FASTQ file will be saved.
        gc_bounds (tuple): a tuple with GC percentage boundaries (integer or float). Default is (0, 100).
        length_bounds (tuple()): a tuple with length boundaries (only integer) Default is (0, 2**32). 
        quality_threshold (float): an integer or float number, lower boundary for mean quality. Default is 0.

    Returns: 
        None 
    """
    work_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    if not os.path.exists(os.path.join(work_dir, 'filtered')):
        os.mkdir(os.path.join(work_dir, "filtered"))
    output_path = os.path.join(work_dir, "filtered", output_fastq + ".fastq")


def convert_multiline_fasta_to_oneline(input_fasta: str, 
                                       output_fasta: str = "output.fasta"):
    """
    Converts multiline fasta to oneline.

    Args:
        input_fastq (str): path to the input FASTQ file
        output_fastq (str): output FASTQ file path, optional. If not defined, "output.fasta" name is used.

    Returns: 
        None
    """
    work_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    bf.convert_helper(input_fasta, output_fasta)
                

def parse_blast_output(input_file: str, output_file: str):
    """
    Parses BLAST results and saves the best hit description for each query.

    Args:
        input_file (str): path to the BLAST output txt file.
        output_file (str): path to the output file where protein descriptions
        will be saved.

    Returns:
        None
    """
    work_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    bf.parse_helper(input_file, output_file)
