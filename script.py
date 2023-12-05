from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio.Align.Applications import ClustalOmegaCommandline

# Ścieżka do pliku z sekwencjami wygenerowanymi przez Clustal Omega
clustal_output_file = "sciezka/do/pliku/clustal_output.fasta"

# Wczytanie sekwencji z pliku FASTA
sequences = list(SeqIO.parse(clustal_output_file, "fasta"))

# Wyświetlenie wczytanych sekwencji
for seq_record in sequences:
    print(seq_record.id)
    print(seq_record.seq)

# Stworzenie alignacji sekwencji
alignment = MultipleSeqAlignment(sequences)

# Wyświetlenie alignacji
print("\nMultiple Sequence Alignment:")
print(alignment)

# Przykład zapisu alignacji do pliku
alignment_file = "alignment_output.fasta"
SeqIO.write(alignment, alignment_file, "fasta")
print(f"Alignment saved to {alignment_file}")
