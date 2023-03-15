# fsds_resume_proj
Proof of Sample Project



Creating conda environment
''''
conda create -p venv python==3.7 -y  (-p is used so that the env is created in the same folder as the working directory)
''''
''''
conda activate venv/
''''
''''
pip install -r requirements.txt
'''


for setting up CI/CD pipeline we need three information
1. HEROKU_EMAIL = anmhatre94@gmail.com
2. HEROKU_API_KEY = fc2e4e4e-eb4f-437b-adce-e1453e9feb50
3. HEROKU_APP_NAME = <>


Steps to deploy a docker image to aws EC@ via git actions

1. create repository in github
2. create .github/workflows directory in the registory and create two files as below
        a. create aws.yml and provide details of workflow
        b. creaete task-definition.json file
                -- This can be updated once we have created the task definition.
                -- aws ecs describe-task-definition \
                        -- task-definition flask-deploy \
                        -- query taskDefinition > task-definition.json

3. Review  the role created to access AWS account from Github.
4. Create Repository in AWS to store image5. Create task definition -- public.ecr.aws/b6p7q1d9/flask-deploy
6. Create cluster and service
7. Create dockerfile for sample app
8. update the docker file in github repo
9. check if the sample app is deplyed in the ECS or not?



"""""""""
firebase key - 1//0g7JxOfAVu6N1CgYIARAAGBASNwF-L9Ir13k-J6Ul98E7MDuzDoNKpiN0GM9eDVrRF5GuOQzztrR2mKSWp6jFVZxx3ZC0Db-LPIM
"""""""""
