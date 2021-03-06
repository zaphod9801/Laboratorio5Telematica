# Laboratorio 5 Topicos Especiales en telemática 

Este repositorio contiene las evidencias del desarrollo del laboratorio 5 de la materia Topicos Especiales en Telematica 

## Primera parte (5-1), Cluster EMR
El primer paso para esto fue crear el bucket que servirá como datalake para el cluster que crearemos dentro del servicio S3 de AWS así:
![image](https://user-images.githubusercontent.com/71454879/169939179-dece8274-9962-43ad-9be2-390efbaf3b14.png)
![image](https://user-images.githubusercontent.com/71454879/169939202-98973ff3-09b3-43e4-b19c-d4f3e80a81ea.png)
Es importante que el bucket sea de acceso publico para este caso.

Una vez creado el bucket, se creara en su interior una carpeta llamada "raw" será donde estarán los archivos:
![image](https://user-images.githubusercontent.com/71454879/169939918-3f7180f6-5bbf-4113-80ab-fc1a606240e2.png)
Ahora, en esta carpeta se subirán los datasets que fueron dados por el profesor usando la función de upload, simplemente se arrastran
![image](https://user-images.githubusercontent.com/71454879/169939989-f2c8903e-9b7c-40f1-a9f7-1bda8834f690.png)
(el link de acceso al bucket es https://jsruizadatalake2.s3.amazonaws.com/raw/)

Ahora se pasará a crear el cluster EMR, usando la opción crear cluster dentro del servicio EMR de AWS, dentro de este tendremos que 
tener la siguiente configuración:
![image](https://user-images.githubusercontent.com/71454879/169942034-531c139f-b2bf-47b0-8e3b-17a17372e46a.png)
![image](https://user-images.githubusercontent.com/71454879/169942069-7671f2ee-b362-4a72-85be-346cf32d97de.png)
![image](https://user-images.githubusercontent.com/71454879/169942079-6d46af09-cbba-4fec-ba49-03b0d9e91bdc.png)
![image](https://user-images.githubusercontent.com/71454879/169942106-e175ed03-4b92-4cb0-bda7-af1d49fd6edd.png)

Una vez esté listo veremos algo como esto:
![image](https://user-images.githubusercontent.com/71454879/169944182-08b88d03-d64b-4d17-bf70-a6ae2fb6a070.png)
Ahora podemos conectarnos al cluster usando la opción de "Connect to the Master Node Using SSH" que veremos al entrar en el cluster:
![image](https://user-images.githubusercontent.com/71454879/169944258-37ba1037-1e71-42ef-ae47-20230be352e8.png)
Usaremos el comando SSH que nos especifica dentro del apartado Mac/Linux (teniendo previamente las claves.pem en la ruta correcta y abierto
el puerto 22 por SSH en el security group del nodo maestro):
![image](https://user-images.githubusercontent.com/71454879/169945048-160f727a-b211-4bfd-9b5a-b28929dfecde.png)

Si la conexión es exitosa veremos algo así:
![image](https://user-images.githubusercontent.com/71454879/169945140-41aceb5e-a898-4a1e-a6b9-bcfe89481fda.png)
Una vez dentro crearemos un usuario llamado "hadoop" con:
```shell
sudo su hadoop
```
Después de esto podremos ver los directorios del hdfs usando:
```shell
hdfs dfs -ls /
```
Veremos algo como esto:
![image](https://user-images.githubusercontent.com/71454879/169945354-c3d586ee-ccbb-4d3c-850d-04f3754c292c.png)
Además podemos ver que contiene instalado (lo que seleccionamos en el primer paso de la creación del cluster) usando:
```shell
hdfs dfs -ls /user
```
Viendo algo como esto:
![image](https://user-images.githubusercontent.com/71454879/169945563-0af574a3-5176-4548-8af0-31ff7ca4b7f3.png)

Ahora podemos intentar conectarnos mediante la interfaz gráfica de Hue, para esto debemos agregar los puertos: 8888, 8890 y 9443 al 
Security group y además a las excepciones de "Public Access" de EMR. 
Para conectarnos usamos la opción "Application user interfaces" del cluster:
![image](https://user-images.githubusercontent.com/71454879/169946774-603b87d4-ae63-4cce-b8ff-a370f7202e73.png)
Ahi tendremos la URL para varias aplicaciones, en este caso nos interesa la de Hue:
![image](https://user-images.githubusercontent.com/71454879/169946823-c2c23aff-cd94-4ff8-84ed-fc4bc25f4fb9.png)
Al entrar veremos esto:
![image](https://user-images.githubusercontent.com/71454879/169946927-dfaf638b-4b6f-4ca3-b17c-0f660403876a.png)
Tras completar el registro veremos esto:
![image](https://user-images.githubusercontent.com/71454879/169947011-3932a6da-5acf-47bf-b2cd-4a6b705a25f2.png)


## Segunda parte (5-2) Gestión de archivos en HDFS y S3

En este punto podremos manejar archivos tanto desde la terminal del nodo maestro como desde la interfaz gráfica de Hue

Podemos explorar archivos:
![image](https://user-images.githubusercontent.com/71454879/169947642-f713a7fc-0cde-48e7-b184-124c5e043c04.png)

Crear carpetas:
![image](https://user-images.githubusercontent.com/71454879/169947726-a89de8b5-91c6-43e3-ab12-15b31dd0fec4.png)
![image](https://user-images.githubusercontent.com/71454879/169947779-2b509f4c-7ab1-4a8c-9d5b-bcadad36e546.png)
![image](https://user-images.githubusercontent.com/71454879/169947793-678b1caf-6108-4179-a9f6-59f7b1447cd5.png)

Subir archivos:
![image](https://user-images.githubusercontent.com/71454879/169947902-5815cbe7-952d-4850-8c10-5376ab07a3c2.png)

Ver el contenido de un archivo:
![image](https://user-images.githubusercontent.com/71454879/169947941-c6530e74-789e-4d36-a66f-0ecbbac22c68.png)

Todo esto también puede hacerse desde la terminal de nuestro nodo maestro, desde el usuario "hadoop"

Podemos ver que tenemos una carpeta previamente creada llamada datasets, para verla usamos:
```shell
hdfs dfs -ls /user/hadoop
```
O si aun no existe podemos crearla con:
```shell
hdfs dfs -mkdir /user/hadoop/datasets
```
![image](https://user-images.githubusercontent.com/71454879/169948392-4ce270e4-5129-46f1-9681-1733aff28c05.png)

Podemos traer los contenidos de un bucket S3 dentro del hdfs usando:
```shell
hadoop distcp s3://jsruizadatalake2/datasets/raw /tmp/
```
![image](https://user-images.githubusercontent.com/71454879/169950594-69ec890f-181b-44ba-a1b6-f32a507cca9c.png)
Podemos verlos con:
```shell
hdfs dfs -ls /tmp/raw
```
![image](https://user-images.githubusercontent.com/71454879/169950691-e97e3071-b8dd-4ae8-bb9f-c9ff6dea69e9.png)

También podemos hacerlo desde el hdfs al directorio creado en Hue:
![image](https://user-images.githubusercontent.com/71454879/169952008-6c61da70-8cbb-4dff-9964-baf46152623f.png)
![image](https://user-images.githubusercontent.com/71454879/169952051-53d1a69d-f62c-46bb-a825-e012fe434034.png)
