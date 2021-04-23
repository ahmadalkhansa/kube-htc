FROM htcondor/base:8.9.7-el7

RUN yum install -y docker-io

RUN usermod -aG dockerroot condor

RUN usermod -aG wheel condor

RUN chown -R condor /var/lib/condor/execute

RUN chown -R condor /root/

RUN chmod -R g+rwx /root/

#RUN yum install -y which
#
#RUN yum install -y iptables-services
#
#RUN echo 'user.max_user_namespaces=28633' >> /etc/sysctl.conf
#
#RUN adduser less
#
#USER less
#
#RUN curl -fsSL https://get.docker.com/rootless | sh
#
#RUN chmod -R g+rx /home/less
#
#USER root
#
#RUN usermod -aG less condor
#
#RUN mkdir /home/mount_dir

RUN curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose

RUN chmod +x /usr/local/bin/docker-compose
