FROM ubuntu

RUN apt update -y
RUN apt install -y time
RUN apt install -y xz-utils
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install pandas

WORKDIR /home

COPY allprot0129.fasta.tar.xz allprot0129.fasta.tar.xz
COPY all_replacements.csv all_replacements.csv

RUN tar -xvf allprot0129.fasta.tar.xz

RUN mkdir /home/bin
WORKDIR /home/bin

COPY bin/csv_sorter.sh csv_sorter.sh
RUN chmod +x csv_sorter.sh
COPY bin/database_indexer.py database_indexer.py
RUN chmod +x database_indexer.py
COPY bin/database_purifier.py database_purifier.py
RUN chmod +x database_purifier.py
COPY bin/fasta_mutations.py fasta_mutations.py
RUN chmod +x fasta_mutations.py
COPY bin/pre_mutational_assignment.py pre_mutational_assignment.py
RUN chmod +x pre_mutational_assignment.py
COPY bin/mutational_assignment.py mutational_assignment.py
RUN chmod +x mutational_assignment.py
COPY bin/protein_extractor.sh protein_extractor.sh
RUN chmod +x protein_extractor.sh
COPY bin/sequence_reducer.py sequence_reducer.py
RUN chmod +x sequence_reducer.py
COPY bin/wrapper.sh wrapper.sh
RUN chmod +x wrapper.sh

ENV PATH="/home/bin:/bin:/usr/bin:$PATH"