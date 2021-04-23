from centos:7

RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

RUN yum install -y https://research.cs.wisc.edu/htcondor/repo/8.8/el7/release/htcondor-release-8.8-1.el7.noarch.rpm

RUN yum install -y condor

RUN yum install -y yum-utils

RUN yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

RUN yum install -y docker-ce docker-ce-cli containerd.io

COPY initialize.sh /home/initialize.sh

RUN chmod +x /home/initialize.sh

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["/home/initialize.sh"]