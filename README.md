# Laboratorio 5 Topicos Especiales en telemática 

Este repositorio contiene las evidencias del desarrollo del laboratorio 5 de la materia Topicos Especiales en Telematica 

## Primera parte, Cluster EMR
El primer paso para esto fue crear el bucket que servirá como datalake para el cluster que crearemos dentro del servicio S3 de AWS así:
![image](https://user-images.githubusercontent.com/71454879/169939179-dece8274-9962-43ad-9be2-390efbaf3b14.png)
![image](https://user-images.githubusercontent.com/71454879/169939202-98973ff3-09b3-43e4-b19c-d4f3e80a81ea.png)
Es importante que el bucket sea de acceso publico para este caso.

Una vez creado el bucket, se creara en su interior una carpeta llamada "raw" será donde estarán los archivos:
![image](https://user-images.githubusercontent.com/71454879/169939918-3f7180f6-5bbf-4113-80ab-fc1a606240e2.png)
Ahora, en esta carpeta se subirán los datasets que fueron dados por el profesor usando la función de upload, simplemente se arrastran
![image](https://user-images.githubusercontent.com/71454879/169939989-f2c8903e-9b7c-40f1-a9f7-1bda8834f690.png)

Ahora se pasará a crear el cluster EMR, usando la opción crear cluster dentro del servicio EMR de AWS, dentro de este tendremos que 
tener la siguiente configuración:
![image](https://user-images.githubusercontent.com/71454879/169942034-531c139f-b2bf-47b0-8e3b-17a17372e46a.png)
![image](https://user-images.githubusercontent.com/71454879/169942069-7671f2ee-b362-4a72-85be-346cf32d97de.png)
![image](https://user-images.githubusercontent.com/71454879/169942079-6d46af09-cbba-4fec-ba49-03b0d9e91bdc.png)
![image](https://user-images.githubusercontent.com/71454879/169942106-e175ed03-4b92-4cb0-bda7-af1d49fd6edd.png)
