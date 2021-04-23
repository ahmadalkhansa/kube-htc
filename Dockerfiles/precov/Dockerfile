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
COPY bin/database_purifier.py database_purifier.py
RUN chmod +x database_purifier.py
COPY bin/protein_extractor.sh protein_extractor.sh
RUN chmod +x protein_extractor.sh
COPY bin/wrapper.sh wrapper.sh
RUN chmod +x wrapper.sh

ENV PATH="/home/bin:/bin:/usr/bin:$PATH"
ENTRYPOINT ["/bin/bash", "-c", "wrapper.sh"]