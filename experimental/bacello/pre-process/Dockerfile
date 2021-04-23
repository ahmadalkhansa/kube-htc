FROM psi_blast:latest
WORKDIR /home
COPY db_index.sh db_index.sh
RUN chmod +x db_index.sh
COPY separator.py separator.py
RUN chmod +x separator.py
COPY elimination.sh elimination.sh
RUN chmod +x elimination.sh
COPY singleline.sh singleline.sh
RUN chmod +x singleline.sh
COPY rotation.sh rotation.sh
COPY check_lenght.sh check_lenght.sh
COPY psi_blast.sh psi_blast.sh
RUN chmod +x psi_blast.sh
COPY wrapper.sh wrapper.sh
RUN chmod +x rotation.sh
RUN chmod +x check_lenght.sh
RUN chmod +x wrapper.sh
ENTRYPOINT ["/bin/bash", "-c", "time ./wrapper.sh"]
~                                                    
