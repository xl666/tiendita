FROM python:3.6.7
RUN pip install django==1.11
RUN pip install pymysql
RUN pip install djangorestframework
RUN mkdir "/code" 
RUN mkdir "/system"
COPY iniciarServidor.sh "/system"
WORKDIR "/code"
ENV PUERTO "8000"
ENV DOMINIO "0.0.0.0"
RUN chmod 755 "/system/iniciarServidor.sh"
CMD /bin/bash -c '/system/iniciarServidor.sh "$DOMINIO" "$PUERTO"'