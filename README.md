# Flask Application

This repository contains a Flask application that serves as a web application backend. The application is designed to demonstrate the deployment process using AWS Elastic Beanstalk and implement CI/CD using AWS CodePipeline.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Deployment to AWS Elastic Beanstalk](#deployment-to-aws-elastic-beanstalk)
- [Setting Up CodePipeline for CI/CD](#setting-up-codepipeline-for-cicd)
- [Usage](#usage)

## Prerequisites
- Python 3.x
- Flask
- AWS Account
- AWS CLI
- Elastic Beanstalk CLI

## Deployment to AWS Elastic Beanstalk
1. Install the Elastic Beanstalk Command Line Interface (EB CLI) if you haven't already.
   ```bash
   pip install awsebcli
   ```
2. Initialize your Elastic Beanstalk application:
   ```bash
   eb init -p python-3.x your-app-name
   ```
3. Create your environment and deploy your application:
   ```bash
   eb create your-environment-name
   eb deploy
   ```
4. Open your application in a web browser:
   ```bash
   eb open
   ```

## Setting Up CodePipeline for CI/CD
1. Navigate to the AWS CodePipeline service in your AWS Management Console.
2. Create a new pipeline and link your GitHub repository.
3. Choose the source stage as GitHub. You may need to connect your GitHub account.
4. Add a build stage. You can use AWS CodeBuild to build and test your application.
5. Add a deploy stage that uses Elastic Beanstalk to deploy your application.

## Usage
1. Clone this repository.
   ```bash
   git clone https://github.com/Manishpandey18th/cicd-test.git
   ```
2. Change into the project directory and run the application:
   ```bash
   cd cicd-test
   python app.py
   ```
3. Visit `http://127.0.0.1:5000` in your web browser to see the application in action.

## Conclusion
This setup provides a scalable way to deploy Flask applications using AWS services. You can leverage the CI/CD pipeline to automate testing and deployment for faster development cycles.