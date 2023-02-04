**Prerequisites For API deployment**:
Docker must be installed on your system.
The code must be cloned or downloaded to your local machine.

----------------------------------------------
**Building the solution locally**:

1.
Open your terminal and navigate to the directory where the code has been saved.

2.
Run the following command to build the Docker image:

docker build -t <image_name> .

Replace <image_name> with the desired name for the Docker image.

3.
After the image has been built, run the following command to start a container from the image:

docker run -p 8000:8000 <image_name>

This will start a container and map the host machine's port 8000 to the container's port 8000.

4.
You can now access the application in your web browser by visiting http://localhost:8000/jumble/{word}, where {word} is the word you want to jumble.

To access the audit api, in your web browser visit http://localhost:8000/audit

The audit will return the last 10 api calls.

----------------------------------------------
**Updating the solutio**n:

Make the necessary changes to the code on your local machine.

Repeat steps 2 and 3 from the Building the solution locally section to apply the changes.

The updated solution should now be accessible at http://localhost:8000/jumble/{word}.

-----------------------------------------------
**Prerequisites For Deploying the application on Minikube through helm**:
Minikube must be installed on your system.
The code must be cloned or downloaded to your local machine.
A Docker image of the application must be built.
Helm must be installed on your system.

-----------------------------------------------
**Deploying the application**

1.
Start Minikube by running the following command in your terminal:

minikube start

2.
Create a Helm chart for the application by running the following command:

helm create <chart_name>

Replace <chart_name> with the desired name for the Helm chart.

3.
Modify the values.yaml file in the chart to include the Docker image details (line #8 repository:) and other configuration options. 

4. 
Install the Helm chart on the target cluster by running the following command:

helm install <release_name> <chart_path>

Replace <release_name> with the desired name and chart_path with the path for the Helm chart.

5.
To access the application, run the following command:

kubectl expose deployment {{ .Release.Name }}-deployment --type=LoadBalancer

Replace {{ .Release.Name }} with the actual name of the release.

6.
To access the applcation, run the following command:

minikube service {{ .Release.Name }}-service

Replace {{ .Release.Name }} with the actual name of the release.

The above command opens the application in the web browser.
