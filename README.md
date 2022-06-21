# Housing_price_app


# What?
<br> 1. Create a manifest file for kubernetes deployment object and include flask app docker image in the container config.
<br> 2. Add necessary labels to map the deployment with service for exposing the app to the internet.
<br> 3. Create a manifest file for kubernetes service object and map the service to the deployment.
<br> 4. App should be accessible only from tiger vpn (Important). Make necessary firewall settings.
<br> 5. Test the app from your local

PS: Deploy the app in the kubernetes cluster (AKS)

# How to Deploy
<br> 1. After creating the deployment.yaml file login to az using ```az login``` command.
<br> 2. connect to aks cluster using the below commands:```az account set --subscription 8cbfc19a-ed09-496d-8b87-3f3a46f7b9a5```
<br>     ```az aks get-credentials --resource-group rg-pvtendpt-test --name cdpipeline-azfunctest```
<br> 3. After connecting to the cluster deploy the app using deployment.yaml file. command used:```kubectl create -f deployment.yaml```
<br> 4. Once the app is deployed on the cluster use the external IP assigned to run the app.(url given below)



# Screenshots

![Screenshot (36)](https://user-images.githubusercontent.com/92777791/174748778-f4f79da3-08cf-4366-ad37-55361d2da519.png)




![Screenshot (37)](https://user-images.githubusercontent.com/92777791/174748801-b448a5ce-73c5-4ef1-9374-a975892fb41a.png)





![Screenshot (38)](https://user-images.githubusercontent.com/92777791/174748884-33256bce-96cb-4a41-a827-0b04f231650a.png)




# Flask App URL
http://20.237.8.255:5000/

