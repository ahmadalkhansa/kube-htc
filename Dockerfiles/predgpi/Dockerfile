FROM mapoferri/traineership:pred_app1
#FROM ubuntu_predgpi:latest

WORKDIR /home/predgpi_app

COPY move.sh move.sh
RUN chmod +x move.sh
COPY separator.py separator.py
RUN chmod +x separator.py
COPY elimination.sh elimination.sh
RUN chmod +x elimination.sh
COPY singleline.sh singleline.sh
RUN chmod +x singleline.sh
COPY rotation.sh rotation.sh
COPY application.sh application.sh
COPY check_lenght.sh check_lenght.sh
COPY wrapper.sh wrapper.sh
RUN chmod +x rotation.sh
RUN chmod +x check_lenght.sh
RUN chmod +x application.sh
RUN chmod +x wrapper.sh
ENV PREDGPI_HOME='/home/predgpi_app'
ENV PATH="/home/predgpi_app:/bin:/usr/bin:$PATH"
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["time wrapper.sh"]